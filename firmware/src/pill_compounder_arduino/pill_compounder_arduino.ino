#include <Arduino.h>
#include <avr/pgmspace.h>
#include <stdlib.h>
#include <string.h>

/*
  Pill Compounder: Timer1 auger + Timer2 D2 detent indexing + linear actuator
  Target: 16 MHz ATmega328P Uno / classic Nano (NOT Uno R4 or Mega).

  Auger: STEP D9, DIR D8, ENABLE D10.
  Disk:  STEP D11, DIR D12, ENABLE D4.
  Mechanical switch: COM -> GND, NO -> D2. No external voltage to D2.
  Linear actuator TMC2209: STEP D6, DIR D7, signal GND -> Arduino GND.

  Driver ALM/fault inputs are intentionally NOT used.
  INPUT_PULLUP: pressed on rim = LOW, released in detent = HIGH.

  ALL disk travel is clockwise only and uses DISK_CLOCKWISE_DIR_LEVEL.
  LOW is the current bench-tested direction level; confirm clockwise from
  ABOVE the disc with the actuator raised. NEXT advances one slot clockwise.
  DISK PREV is intentionally rejected. Slot numbers increase clockwise.

  Start manually aligned in a known detent, then send SET SLOT n.
  Identical detents do not provide automatic absolute homing.
  The Pi should raise the actuator before any disk command. Because the
  actuator now lives on this same Uno, simultaneous actuator/disk/auger motion
  is rejected. Actuator UP/DOWN position is still software-only because there
  are no actuator limit switches.

  Indexing: leave current detent -> stable pressed rim -> stable release.
  Detents are counted by the switch, NOT a fixed 800-step move.
  Step limits only detect missing/implausibly early switch transitions.
  Debouncing happens inside Timer2 ISR so serial output cannot delay it.
  Timer2 generates D11 pulses in its ISR; Timer1 still uses hardware OC1A.
  Do not use tone(), Servo, or other libraries that reconfigure these timers.

  SET SLOT requires D2 to be released and stable for 20 ms. Completion
  messages remain DONE DISK SLOT n. Disk indexing errors invalidate position.
  A completed move holds the disk enabled. STOP/DISABLE releases it.
  DISK STATUS preserves the Pi-facing protocol fields SLOT=n, AT_SLOT=YES/NO,
  SWITCH=OPEN/PRESSED, and DIRECTION=CW.

  Bench starting values, not machine-validated settings:
    1000 steps/s; expected pitch 800; allowed interval 400..1200 steps;
    leave starting detent within 400 steps; 4 ms debounce while moving.
  Mechanical switch actuation is an edge, not necessarily detent center.
  Mount for alignment or tune DISK_ALIGNMENT_OFFSET_STEPS (default 0).
  The offset is applied only after detecting the destination detent.
  It must remain inside the released portion of that detent.
*/

#if !defined(__AVR_ATmega328P__)
#error "Select an ATmega328P Uno or classic Nano; this sketch uses their AVR registers."
#endif
#if F_CPU != 16000000UL
#error "This sketch requires a 16 MHz board."
#endif

// ---------------- Pins and polarity ----------------
const uint8_t AUGER_STEP_PIN=9, AUGER_DIR_PIN=8, AUGER_ENABLE_PIN=10;
const uint8_t DISK_STEP_PIN=11, DISK_DIR_PIN=12, DISK_ENABLE_PIN=4;
const uint8_t DISK_SWITCH_PIN=2;
const uint8_t ACTUATOR_STEP_PIN=6, ACTUATOR_DIR_PIN=7;
const uint8_t DRIVER_ENABLE_LEVEL=HIGH, DRIVER_DISABLE_LEVEL=LOW;
const uint8_t DISPENSE_DIR_LEVEL=LOW;
const uint8_t DISK_CLOCKWISE_DIR_LEVEL=LOW;  // Change ONLY this if physical direction is wrong.
const uint8_t ACTUATOR_DOWN_DIRECTION_LEVEL=HIGH;
const uint8_t ACTUATOR_UP_DIRECTION_LEVEL=LOW;

// ---------------- Disk tuning ----------------
const uint8_t DISK_SLOT_COUNT=8;
const uint32_t DISK_MOTOR_FULL_STEPS_PER_REV=200UL;
const uint32_t DISK_DRIVER_MICROSTEPS=32UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR=1UL;
const uint32_t DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR=1UL;
const uint32_t DISK_STEPS_PER_SLOT=
    DISK_MOTOR_FULL_STEPS_PER_REV * DISK_DRIVER_MICROSTEPS *
    DISK_MOTOR_REVS_PER_DISK_REV_NUMERATOR /
    (DISK_SLOT_COUNT * DISK_MOTOR_REVS_PER_DISK_REV_DENOMINATOR);
const uint32_t DISK_STEP_FREQUENCY_HZ=1000UL;
const uint16_t DISK_MIN_STEPS_PER_SLOT=DISK_STEPS_PER_SLOT/2;
const uint16_t DISK_MAX_STEPS_PER_SLOT=DISK_STEPS_PER_SLOT*3/2;
const uint16_t DISK_MAX_EXIT_STEPS=DISK_STEPS_PER_SLOT/2;
const uint16_t DISK_ALIGNMENT_OFFSET_STEPS=0;
const uint16_t DISK_DEBOUNCE_MS=4;
const uint16_t DISK_IDLE_DEBOUNCE_MS=20;
const uint16_t DISK_ENABLE_SETTLE_MS=20;
const uint16_t DISK_DIRECTION_SETTLE_US=20;
const uint32_t DISK_MOVE_TIMEOUT_MS=15000UL;
const uint8_t DISK_TIMER_OCR=F_CPU/(128UL*DISK_STEP_FREQUENCY_HZ)-1UL;
const uint32_t DISK_ACTUAL_HZ=F_CPU/(128UL*(DISK_TIMER_OCR+1UL));
const uint16_t DISK_DEBOUNCE_SAMPLES=(DISK_ACTUAL_HZ*DISK_DEBOUNCE_MS+999UL)/1000UL;
static_assert(DISK_STEP_FREQUENCY_HZ>=489UL && DISK_STEP_FREQUENCY_HZ<=2000UL,
              "Disk timer tuning supports 489..2000 steps/s.");
static_assert(DISK_STEPS_PER_SLOT>=100 && DISK_STEPS_PER_SLOT<20000,
              "Check disk gearing and microsteps.");
static_assert(DISK_ALIGNMENT_OFFSET_STEPS<DISK_MIN_STEPS_PER_SLOT,
              "Offset must remain inside one detent.");

// ---------------- PER-POWDER AUGER SPEEDS - EDIT HERE ----------------
// motor_scale_control.py sends the profile number shown beside each powder.
// Hz controls speed: larger Hz = faster motor rotation.
// FINE/FINAL steps control dose size: fewer steps = less powder per pulse.
//
// Keep the profile numbers and powder order unchanged. Change only the seven
// motor values on the powder's row while calibrating. The starting values
// below preserve the old FREE/NONFREE behavior for every powder.
enum PowderProfileId : uint8_t {
  POWDER_GRANULATED_SUGAR=1,
  POWDER_TABLE_SALT=2,
  POWDER_POWDERED_SUGAR=3,
  POWDER_BAKING_SODA=4,
  POWDER_CORNSTARCH=5,
  POWDER_GROUND_CINNAMON=6,
  POWDER_ALL_PURPOSE_FLOUR=7,
  POWDER_COCOA_POWDER=8
};
const uint8_t POWDER_PROFILE_COUNT=8;

struct AugerPowderProfile {
  uint32_t maxHz;
  uint32_t turboHz;
  uint32_t normalHz;
  uint32_t fineSteps;
  uint32_t fineHz;
  uint32_t finalSteps;
  uint32_t finalHz;
};

//                                   MAX     TURBO  NORMAL  FINE steps/Hz  FINAL steps/Hz
const AugerPowderProfile AUGER_POWDER_PROFILES[] PROGMEM = {
  {30000UL, 20000UL, 2400UL,  36UL,  700UL, 24UL,  700UL}, // 1 Granulated sugar
  {30000UL, 20000UL, 2400UL,  36UL,  700UL, 24UL,  700UL}, // 2 Table salt
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}, // 3 Powdered sugar
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}, // 4 Baking soda
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}, // 5 Cornstarch
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}, // 6 Ground cinnamon
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}, // 7 All-purpose flour
  {35000UL, 20000UL, 9000UL, 200UL, 6000UL, 50UL, 2000UL}  // 8 Cocoa powder
};
static_assert(sizeof(AUGER_POWDER_PROFILES)/sizeof(AUGER_POWDER_PROFILES[0])==
              POWDER_PROFILE_COUNT, "Every powder needs one auger profile.");

const uint32_t CONTINUOUS_START_HZ=2000, RAMP_STEP_HZ=500, RAMP_UPDATE_MS=10;
const uint32_t SERIAL_WATCHDOG_MS=2000;

// ---------------- Linear actuator tuning ----------------
// Preserved from the working XIAO RP2040 actuator sketch.
const uint32_t ACTUATOR_TRAVEL_STEPS=69000UL;
const uint32_t ACTUATOR_UP_FAST_HALF_PERIOD_US=40UL;
const uint32_t ACTUATOR_DOWN_FAST_HALF_PERIOD_US=40UL;
const uint32_t ACTUATOR_DOWN_SLOW_HALF_PERIOD_US=180UL;
const uint32_t ACTUATOR_DOWN_SLOW_STEPS=ACTUATOR_TRAVEL_STEPS/4UL;
const uint32_t ACTUATOR_DOWN_FAST_STEPS=ACTUATOR_TRAVEL_STEPS-ACTUATOR_DOWN_SLOW_STEPS;
const uint16_t ACTUATOR_DIRECTION_SETTLE_US=20;

enum AugerRunMode { AUGER_STOPPED, AUGER_CONTINUOUS, AUGER_PULSE };
volatile AugerRunMode augerMode=AUGER_STOPPED;
volatile uint32_t pulseCompareMatchesRemaining=0;
volatile bool pulseFinishedFlag=false;
uint32_t currentContinuousHz=0, targetContinuousHz=0, activePulseHz=0;
uint32_t lastRampUpdateMs=0, lastSerialContactMs=0;
const char *simplifiedPulseLabel=NULL;

enum DiskPhase { DISK_EXIT, DISK_SEEK, DISK_OFFSET };
enum DiskResult { DISK_RESULT_NONE, DISK_RESULT_DONE, DISK_RESULT_NO_EXIT,
                  DISK_RESULT_NO_DETENT, DISK_RESULT_EARLY_DETENT,
                  DISK_RESULT_OFFSET_OUTSIDE };
volatile bool diskMoveActive=false;  // Remains true until completion is processed.
volatile bool diskMoveFinished=false;
volatile DiskPhase diskPhase=DISK_EXIT;
volatile DiskResult diskResult=DISK_RESULT_NONE;
volatile bool diskStepHigh=false;
volatile uint16_t diskStepsSinceDetent=0, diskStableSamples=0, diskOffsetRemaining=0;
volatile uint8_t diskSlotsRemaining=0;
uint8_t diskPendingTargetSlot=0, diskCurrentSlot=1;
bool diskPositionKnown=false, diskDriverEnabled=false;
uint32_t diskMoveStartMs=0;
bool switchRawReleased=false;
uint32_t switchChangedMs=0;

// ---------------- Linear actuator state ----------------
enum ActuatorMotionDirection : int8_t {
  ACTUATOR_MOTION_NONE=0,
  ACTUATOR_MOTION_UP=-1,
  ACTUATOR_MOTION_DOWN=1
};
enum ActuatorPosition : uint8_t {
  ACTUATOR_POSITION_UNKNOWN,
  ACTUATOR_POSITION_UP,
  ACTUATOR_POSITION_DOWN
};
ActuatorMotionDirection actuatorActiveDirection=ACTUATOR_MOTION_NONE;
ActuatorPosition actuatorPosition=ACTUATOR_POSITION_UNKNOWN;
uint32_t actuatorCompletedSteps=0;
uint32_t actuatorLastStepTransitionUs=0;
bool actuatorStepPinHigh=false;

const uint8_t COMMAND_BUFFER_SIZE=80;
char commandBuffer[COMMAND_BUFFER_SIZE];
uint8_t commandLength=0;
bool commandOverflow=false;

// Keep the first function below every custom type declaration. The Arduino
// sketch preprocessor inserts prototypes here and must already know the types.
bool loadAugerPowderProfile(uint8_t profileId, AugerPowderProfile &profile) {
  if(profileId<1 || profileId>POWDER_PROFILE_COUNT) return false;
  memcpy_P(&profile, &AUGER_POWDER_PROFILES[profileId-1], sizeof(profile));
  return true;
}

// ---------------- Switch / disk low-level helpers ----------------
void updateSwitch() {
  bool released=digitalRead(DISK_SWITCH_PIN)==HIGH;
  if (released!=switchRawReleased) {
    switchRawReleased=released;
    switchChangedMs=millis();
  }
}
bool diskAtStableDetent() {
  updateSwitch();
  return switchRawReleased &&
         (uint32_t)(millis()-switchChangedMs)>=DISK_IDLE_DEBOUNCE_MS;
}
void setDiskDriverEnabled(bool enabled) {
  digitalWrite(DISK_ENABLE_PIN,enabled ? DRIVER_ENABLE_LEVEL : DRIVER_DISABLE_LEVEL);
  diskDriverEnabled=enabled;
}
// Call with interrupts disabled, or from an ISR.
void disconnectDiskStepOutput() {
  TCCR2B=0;
  TIMSK2=0;
  PORTB &= ~_BV(PB3);  // D11 on ATmega328P.
  diskStepHigh=false;
}
void stopDiskImmediate(bool forgetPosition) {
  noInterrupts();
  disconnectDiskStepOutput();
  diskMoveActive=false;
  diskMoveFinished=false;
  diskResult=DISK_RESULT_NONE;
  interrupts();
  diskPendingTargetSlot=0;
  setDiskDriverEnabled(false);
  if (forgetPosition) diskPositionKnown=false;
}
// Timer2 stops immediately at a completed pulse, independent of the main loop.
void finishDiskFromISR(DiskResult result) {
  disconnectDiskStepOutput();
  diskResult=result;
  diskMoveFinished=true;
}

ISR(TIMER2_COMPA_vect) {
  if (!diskMoveActive || diskMoveFinished) return;
  diskStepHigh=!diskStepHigh;
  if (diskStepHigh) { PORTB |= _BV(PB3); return; }
  PORTB &= ~_BV(PB3);
  // Falling edge: one complete motor step. Sample the switch once per step.
  const bool released=(PIND & _BV(PD2))!=0;
  ++diskStepsSinceDetent;
  if (diskPhase==DISK_OFFSET) {
    if (--diskOffsetRemaining==0) {
      finishDiskFromISR(released ? DISK_RESULT_DONE : DISK_RESULT_OFFSET_OUTSIDE);
    }
    return;
  }
  if (diskPhase==DISK_EXIT) {
    if (!released) ++diskStableSamples; else diskStableSamples=0;
    if (diskStableSamples>=DISK_DEBOUNCE_SAMPLES) {
      diskPhase=DISK_SEEK;
      diskStableSamples=0;
    } else if (diskStepsSinceDetent>=DISK_MAX_EXIT_STEPS) {
      finishDiskFromISR(DISK_RESULT_NO_EXIT);
      return;
    }
  } else {
    if (released) ++diskStableSamples; else diskStableSamples=0;
    if (diskStableSamples>=DISK_DEBOUNCE_SAMPLES) {
      if (diskStepsSinceDetent<DISK_MIN_STEPS_PER_SLOT) {
        finishDiskFromISR(DISK_RESULT_EARLY_DETENT);
        return;
      }
      if (--diskSlotsRemaining==0) {
        if (DISK_ALIGNMENT_OFFSET_STEPS==0) finishDiskFromISR(DISK_RESULT_DONE);
        else { diskPhase=DISK_OFFSET; diskOffsetRemaining=DISK_ALIGNMENT_OFFSET_STEPS; }
        return;
      }
      diskStepsSinceDetent=0;
      diskStableSamples=0;
      diskPhase=DISK_EXIT;
    }
  }
  if (diskStepsSinceDetent>=DISK_MAX_STEPS_PER_SLOT)
    finishDiskFromISR(DISK_RESULT_NO_DETENT);
}

// ---------------- Timer1 auger ----------------
uint16_t frequencyToOcr(uint32_t hz) {
  if(hz<123) hz=123;
  uint32_t ocr=F_CPU/(2UL*hz)-1UL;
  if(ocr>65535UL) ocr=65535UL;
  if(ocr<1) ocr=1;
  return (uint16_t)ocr;
}
// Call with interrupts disabled. Reset the actual OC1A latch, not only PORTB,
// so every new pulse train starts LOW even after an interrupted HIGH pulse.
void disconnectStepOutput() {
  TCCR1B=0;
  TIMSK1=0;
  TCCR1A=0;
  digitalWrite(AUGER_STEP_PIN,LOW);
}
void prepareAugerTimer(uint32_t hz, bool counted) {
  disconnectStepOutput();
  TCCR1A=_BV(COM1A1);  // Force compare clears OC1A in non-PWM mode.
  TCCR1C=_BV(FOC1A);
  OCR1A=frequencyToOcr(hz);
  TCNT1=0;
  TIFR1=_BV(OCF1A);
  TCCR1A=_BV(COM1A0);
  TIMSK1=counted ? _BV(OCIE1A) : 0;
  TCCR1B=_BV(WGM12)|_BV(CS10);
}
void stopAugerImmediate(bool announceStop) {
  noInterrupts();
  disconnectStepOutput();
  pulseCompareMatchesRemaining=0;
  pulseFinishedFlag=false;
  augerMode=AUGER_STOPPED;
  interrupts();
  currentContinuousHz=targetContinuousHz=activePulseHz=0;
  simplifiedPulseLabel=NULL;
  digitalWrite(AUGER_ENABLE_PIN,DRIVER_DISABLE_LEVEL);
  if(announceStop) Serial.println(F("OK STOPPED"));
}
bool augerCanStart() {
  if(diskMoveActive) { Serial.println(F("ERR DISK MOVING")); return false; }
  if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
    Serial.println(F("ERR ACTUATOR MOVING")); return false;
  }
  return true;
}
bool startContinuous(uint32_t hz) {
  if(!augerCanStart()) return false;
  if(augerMode!=AUGER_CONTINUOUS) {
    stopAugerImmediate(false);
    digitalWrite(AUGER_DIR_PIN,DISPENSE_DIR_LEVEL);
    digitalWrite(AUGER_ENABLE_PIN,DRIVER_ENABLE_LEVEL);
    delayMicroseconds(20);
    currentContinuousHz=hz<CONTINUOUS_START_HZ ? hz : CONTINUOUS_START_HZ;
    noInterrupts();
    augerMode=AUGER_CONTINUOUS;
    prepareAugerTimer(currentContinuousHz,false);
    interrupts();
    lastRampUpdateMs=millis();
  }
  targetContinuousHz=hz;
  activePulseHz=0;
  simplifiedPulseLabel=NULL;
  Serial.println(F("OK CONTINUOUS"));
  return true;
}
bool startPulse(uint32_t steps, uint32_t hz, const char *label) {
  if(!augerCanStart()) return false;
  stopAugerImmediate(false);
  digitalWrite(AUGER_DIR_PIN,DISPENSE_DIR_LEVEL);
  digitalWrite(AUGER_ENABLE_PIN,DRIVER_ENABLE_LEVEL);
  delayMicroseconds(20);
  activePulseHz=hz;
  simplifiedPulseLabel=label;
  noInterrupts();
  pulseCompareMatchesRemaining=steps*2UL;
  pulseFinishedFlag=false;
  augerMode=AUGER_PULSE;  // Set BEFORE the first timer interrupt.
  prepareAugerTimer(hz,true);
  interrupts();
  Serial.println(F("OK PULSE"));
  return true;
}
bool startProfileContinuous(uint8_t profileId, const char *phase) {
  AugerPowderProfile profile;
  if(!loadAugerPowderProfile(profileId,profile)) {
    Serial.println(F("ERR POWDER PROFILE MUST BE 1..8")); return false;
  }

  uint32_t hz=0;
  if(strcmp(phase,"MAX")==0) hz=profile.maxHz;
  else if(strcmp(phase,"TURBO")==0) hz=profile.turboHz;
  else if(strcmp(phase,"NORMAL")==0) hz=profile.normalHz;
  else {
    Serial.println(F("ERR CONT PHASE MUST BE MAX, TURBO, OR NORMAL"));
    return false;
  }
  return startContinuous(hz);
}
bool startProfilePulse(uint8_t profileId, const char *phase, const char *label=NULL) {
  AugerPowderProfile profile;
  if(!loadAugerPowderProfile(profileId,profile)) {
    Serial.println(F("ERR POWDER PROFILE MUST BE 1..8")); return false;
  }

  if(strcmp(phase,"FINE")==0)
    return startPulse(profile.fineSteps,profile.fineHz,label);
  if(strcmp(phase,"FINAL")==0)
    return startPulse(profile.finalSteps,profile.finalHz,label);

  Serial.println(F("ERR PULSE PHASE MUST BE FINE OR FINAL"));
  return false;
}
ISR(TIMER1_COMPA_vect) {
  if(augerMode!=AUGER_PULSE || pulseCompareMatchesRemaining==0) return;
  if(--pulseCompareMatchesRemaining==0) {
    TCCR1B=0;
    TCCR1A=0;
    TIMSK1=0;
    pulseFinishedFlag=true;
  }
}
void updateContinuousRamp() {
  if(augerMode!=AUGER_CONTINUOUS) return;
  uint32_t now=millis();
  if((uint32_t)(now-lastRampUpdateMs)<RAMP_UPDATE_MS) return;
  lastRampUpdateMs=now;
  if(currentContinuousHz==targetContinuousHz) return;
  if(currentContinuousHz<targetContinuousHz) {
    currentContinuousHz+=RAMP_STEP_HZ;
    if(currentContinuousHz>targetContinuousHz) currentContinuousHz=targetContinuousHz;
  } else {
    currentContinuousHz=currentContinuousHz>RAMP_STEP_HZ ? currentContinuousHz-RAMP_STEP_HZ : targetContinuousHz;
    if(currentContinuousHz<targetContinuousHz) currentContinuousHz=targetContinuousHz;
  }
  noInterrupts();
  OCR1A=frequencyToOcr(currentContinuousHz);
  TCNT1=0;
  interrupts();
}
void updatePulseCompletion() {
  if(!pulseFinishedFlag) return;
  const char *label=simplifiedPulseLabel;
  stopAugerImmediate(false);
  Serial.print(F("DONE "));
  Serial.println(label!=NULL ? label : "PULSE");
}

// ---------------- Disk high-level commands ----------------
bool diskCanMove() {
  if(augerMode!=AUGER_STOPPED) { Serial.println(F("ERR AUGER MOVING")); return false; }
  if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
    Serial.println(F("ERR ACTUATOR MOVING")); return false;
  }
  if(diskMoveActive) { Serial.println(F("ERR DISK BUSY")); return false; }
  if(!diskPositionKnown) {
    Serial.println(F("ERR DISK POSITION UNKNOWN - SEND SET SLOT n")); return false;
  }
  if(!diskAtStableDetent()) {
    if(!switchRawReleased) diskPositionKnown=false;
    Serial.println(F("ERR DISK NOT AT STABLE DETENT - CHECK D2 AND ALIGNMENT"));
    return false;
  }
  return true;
}
void startDiskMoveClockwise(uint8_t slotsToMove, uint8_t targetSlot) {
  diskPendingTargetSlot=targetSlot;
  digitalWrite(DISK_DIR_PIN,DISK_CLOCKWISE_DIR_LEVEL);
  setDiskDriverEnabled(true);
  delay(DISK_ENABLE_SETTLE_MS);
  delayMicroseconds(DISK_DIRECTION_SETTLE_US);
  // Recheck after enabling in case energizing the motor shifted the disc.
  if(digitalRead(DISK_SWITCH_PIN)!=HIGH) {
    stopDiskImmediate(true);
    Serial.println(F("ERR DISK ALIGNMENT CHANGED WHEN ENABLED - POSITION UNKNOWN")); return;
  }
  diskMoveStartMs=millis();
  noInterrupts();
  disconnectDiskStepOutput();
  diskPhase=DISK_EXIT;
  diskStepsSinceDetent=diskStableSamples=diskOffsetRemaining=0;
  diskSlotsRemaining=slotsToMove;
  diskResult=DISK_RESULT_NONE;
  diskMoveFinished=false;
  diskMoveActive=true;
  TCCR2A=_BV(WGM21);  // CTC; OC2A disconnected, D11 is toggled by ISR.
  OCR2A=DISK_TIMER_OCR;
  TCNT2=0;
  TIFR2=_BV(OCF2A);
  TIMSK2=_BV(OCIE2A);
  TCCR2B=_BV(CS22);  // Prescaler 64.
  interrupts();
  Serial.print(F("OK DISK MOVING CW SLOTS="));
  Serial.print(slotsToMove);
  Serial.print(F(" TARGET="));
  Serial.println(targetSlot);
}
void goToDiskSlot(uint8_t requestedSlot) {
  if(!diskCanMove()) return;
  uint8_t distance=(requestedSlot+DISK_SLOT_COUNT-diskCurrentSlot)%DISK_SLOT_COUNT;
  if(distance==0) {
    setDiskDriverEnabled(true);
    Serial.print(F("DONE DISK SLOT ")); Serial.println(diskCurrentSlot);
    return;
  }
  startDiskMoveClockwise(distance,requestedSlot);
}
void moveDiskOneSlotClockwise() {
  if(!diskPositionKnown) {
    Serial.println(F("ERR DISK POSITION UNKNOWN - SEND SET SLOT n"));
    return;
  }
  uint8_t target=(diskCurrentSlot%DISK_SLOT_COUNT)+1;
  goToDiskSlot(target);
}
void updateDiskCompletion() {
  if(!diskMoveFinished) return;
  noInterrupts();
  DiskResult result=diskResult;
  diskMoveFinished=false;
  diskMoveActive=false;
  interrupts();
  if(result!=DISK_RESULT_DONE) {
    stopDiskImmediate(true);
    Serial.print(F("ERR DISK "));
    if(result==DISK_RESULT_NO_EXIT) Serial.print(F("SWITCH DID NOT PRESS"));
    else if(result==DISK_RESULT_NO_DETENT) Serial.print(F("DETENT NOT FOUND"));
    else if(result==DISK_RESULT_EARLY_DETENT) Serial.print(F("DETENT TOO EARLY"));
    else Serial.print(F("OFFSET OUTSIDE DETENT"));
    Serial.println(F(" - POSITION UNKNOWN"));
    return;
  }
  diskCurrentSlot=diskPendingTargetSlot;
  diskPendingTargetSlot=0;
  // ISR confirmed release; wait for idle debounce before another move.
  switchRawReleased=digitalRead(DISK_SWITCH_PIN)==HIGH;
  switchChangedMs=millis();
  Serial.print(F("DONE DISK SLOT ")); Serial.println(diskCurrentSlot);
}
void printDiskStatus() {
  const bool atSlot=diskAtStableDetent();
  const bool switchOpen=digitalRead(DISK_SWITCH_PIN)==HIGH;

  Serial.print(F("DISK STATUS MOVING=")); Serial.print(diskMoveActive ? "YES" : "NO");
  Serial.print(F(" ENABLED=")); Serial.print(diskDriverEnabled ? "YES" : "NO");
  Serial.print(F(" SLOT="));
  if(diskPositionKnown) Serial.print(diskCurrentSlot); else Serial.print(F("UNKNOWN"));
  Serial.print(F(" AT_SLOT=")); Serial.print(atSlot ? "YES" : "NO");
  Serial.print(F(" SWITCH=")); Serial.print(switchOpen ? "OPEN" : "PRESSED");
  Serial.print(F(" DIRECTION=CW"));
  Serial.print(F(" STEPS_PER_SLOT=")); Serial.print(DISK_STEPS_PER_SLOT);
  Serial.print(F(" STEP_HZ=")); Serial.println(DISK_ACTUAL_HZ);
}
void printStatus() {
  Serial.print(F("STATUS MODE="));
  Serial.print(augerMode==AUGER_CONTINUOUS ? "CONTINUOUS" : augerMode==AUGER_PULSE ? "PULSE" : "STOPPED");
  Serial.print(F(" CURRENT_HZ=")); Serial.print(augerMode==AUGER_CONTINUOUS ? currentContinuousHz : activePulseHz);
  Serial.print(F(" TARGET_HZ=")); Serial.print(targetContinuousHz);
  Serial.print(F(" OCR1A=")); Serial.println(OCR1A);
}
void updateWatchdog() {
  if(augerMode!=AUGER_STOPPED && (uint32_t)(millis()-lastSerialContactMs)>SERIAL_WATCHDOG_MS) {
    stopAugerImmediate(false); Serial.println(F("FAULT WATCHDOG"));
  }
  // Finite disk moves have their own limit, so a Pi waiting for DONE does
  // not need to add heartbeats. ISR step bounds also stop a missing switch.
  if(diskMoveActive && !diskMoveFinished &&
     (uint32_t)(millis()-diskMoveStartMs)>DISK_MOVE_TIMEOUT_MS) {
    stopDiskImmediate(true);
    Serial.println(F("ERR DISK TIMEOUT - POSITION UNKNOWN"));
  }
}


// ---------------- Linear actuator ----------------
const __FlashStringHelper* actuatorDirectionName(ActuatorMotionDirection direction) {
  return direction==ACTUATOR_MOTION_DOWN ? F("DOWN") : F("UP");
}
const __FlashStringHelper* actuatorPositionName() {
  if(actuatorPosition==ACTUATOR_POSITION_UP) return F("UP");
  if(actuatorPosition==ACTUATOR_POSITION_DOWN) return F("DOWN");
  return F("UNKNOWN");
}
void stopActuatorMotion(bool printResponse) {
  digitalWrite(ACTUATOR_STEP_PIN,LOW);
  actuatorStepPinHigh=false;
  if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE)
    actuatorPosition=ACTUATOR_POSITION_UNKNOWN;
  actuatorActiveDirection=ACTUATOR_MOTION_NONE;
  actuatorCompletedSteps=0;
  if(printResponse) Serial.println(F("OK ACTUATOR STOPPED"));
}
bool startActuatorMotion(ActuatorMotionDirection direction) {
  if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
    Serial.println(F("ERR ACTUATOR BUSY")); return false;
  }
  if(augerMode!=AUGER_STOPPED) {
    Serial.println(F("ERR AUGER MOVING")); return false;
  }
  if(diskMoveActive) {
    Serial.println(F("ERR DISK MOVING")); return false;
  }
  if((direction==ACTUATOR_MOTION_DOWN && actuatorPosition==ACTUATOR_POSITION_DOWN) ||
     (direction==ACTUATOR_MOTION_UP && actuatorPosition==ACTUATOR_POSITION_UP)) {
    Serial.print(F("ERR ACTUATOR ALREADY "));
    Serial.println(actuatorDirectionName(direction));
    return false;
  }

  digitalWrite(ACTUATOR_DIR_PIN,
      direction==ACTUATOR_MOTION_DOWN ? ACTUATOR_DOWN_DIRECTION_LEVEL
                                      : ACTUATOR_UP_DIRECTION_LEVEL);
  delayMicroseconds(ACTUATOR_DIRECTION_SETTLE_US);
  digitalWrite(ACTUATOR_STEP_PIN,LOW);
  actuatorStepPinHigh=false;
  actuatorCompletedSteps=0;
  actuatorActiveDirection=direction;
  actuatorLastStepTransitionUs=micros();

  Serial.print(F("OK ACTUATOR "));
  Serial.println(actuatorDirectionName(direction));
  return true;
}
uint32_t actuatorCurrentHalfPeriodUs() {
  if(actuatorActiveDirection==ACTUATOR_MOTION_UP)
    return ACTUATOR_UP_FAST_HALF_PERIOD_US;
  if(actuatorActiveDirection==ACTUATOR_MOTION_DOWN)
    return actuatorCompletedSteps<ACTUATOR_DOWN_FAST_STEPS
        ? ACTUATOR_DOWN_FAST_HALF_PERIOD_US
        : ACTUATOR_DOWN_SLOW_HALF_PERIOD_US;
  return ACTUATOR_UP_FAST_HALF_PERIOD_US;
}
void updateActuatorMotion() {
  if(actuatorActiveDirection==ACTUATOR_MOTION_NONE) return;

  uint32_t now=micros();
  uint32_t halfPeriod=actuatorCurrentHalfPeriodUs();
  if((uint32_t)(now-actuatorLastStepTransitionUs)<halfPeriod) return;
  actuatorLastStepTransitionUs=now;

  if(!actuatorStepPinHigh) {
    digitalWrite(ACTUATOR_STEP_PIN,HIGH);
    actuatorStepPinHigh=true;
    return;
  }

  digitalWrite(ACTUATOR_STEP_PIN,LOW);
  actuatorStepPinHigh=false;
  ++actuatorCompletedSteps;
  if(actuatorCompletedSteps<ACTUATOR_TRAVEL_STEPS) return;

  ActuatorMotionDirection finishedDirection=actuatorActiveDirection;
  actuatorActiveDirection=ACTUATOR_MOTION_NONE;
  actuatorPosition=finishedDirection==ACTUATOR_MOTION_DOWN
      ? ACTUATOR_POSITION_DOWN : ACTUATOR_POSITION_UP;

  Serial.print(F("DONE ACTUATOR "));
  Serial.print(actuatorDirectionName(finishedDirection));
  Serial.print(F(" "));
  Serial.println(ACTUATOR_TRAVEL_STEPS);
}
void printActuatorStatus() {
  Serial.print(F("ACTUATOR STATUS MOVING="));
  Serial.print(actuatorActiveDirection==ACTUATOR_MOTION_NONE ? 0 : 1);
  Serial.print(F(" DIRECTION="));
  if(actuatorActiveDirection==ACTUATOR_MOTION_NONE) Serial.print(F("NONE"));
  else Serial.print(actuatorDirectionName(actuatorActiveDirection));
  Serial.print(F(" POSITION="));
  Serial.print(actuatorPositionName());
  Serial.print(F(" COMPLETED_STEPS="));
  Serial.print(actuatorCompletedSteps);
  Serial.print(F(" TRAVEL_STEPS="));
  Serial.print(ACTUATOR_TRAVEL_STEPS);
  Serial.print(F(" SPEED_PHASE="));
  if(actuatorActiveDirection==ACTUATOR_MOTION_DOWN)
    Serial.println(actuatorCompletedSteps<ACTUATOR_DOWN_FAST_STEPS ? F("FAST") : F("SLOW"));
  else if(actuatorActiveDirection==ACTUATOR_MOTION_UP) Serial.println(F("FAST"));
  else Serial.println(F("NONE"));
}

// ---------------- Serial protocol ----------------
bool commandEquals(const char *s) { return strcmp(commandBuffer,s)==0; }
bool parseSlotArgument(const char *prefix,uint8_t &slot) {
  size_t len=strlen(prefix);
  if(strncmp(commandBuffer,prefix,len)!=0) return false;
  const char *text=commandBuffer+len;
  char *end=NULL;
  long n=strtol(text,&end,10);
  slot=(end!=text && *end=='\0' && n>=1 && n<=DISK_SLOT_COUNT) ? (uint8_t)n : 0;
  return true;
}
bool parsePowderPhaseArgument(const char *prefix,uint8_t &profileId,const char *&phase) {
  size_t len=strlen(prefix);
  if(strncmp(commandBuffer,prefix,len)!=0) return false;

  const char *text=commandBuffer+len;
  // Non-numeric forms are old FREE/NONFREE aliases handled farther below.
  if(*text<'0' || *text>'9') return false;
  char *end=NULL;
  long n=strtol(text,&end,10);
  if(end==text || end==NULL || *end!=' ') {
    profileId=0; phase=NULL; return true;
  }
  while(end!=NULL && *end==' ') ++end;
  if(*end=='\0' || n<1 || n>POWDER_PROFILE_COUNT) {
    profileId=0; phase=NULL; return true;
  }
  profileId=(uint8_t)n;
  phase=end;
  return true;
}
void processCommand() {
  lastSerialContactMs=millis();
  if(commandEquals("PING")) { Serial.println(F("OK PING")); return; }
  if(commandEquals("HEARTBEAT")) { Serial.println(F("OK HEARTBEAT")); return; }
  if(commandEquals("STATUS")) { printStatus(); return; }
  if(commandEquals("DISK STATUS")) { printDiskStatus(); return; }
  if(commandEquals("ACTUATOR STATUS")) { printActuatorStatus(); return; }
  if(commandEquals("ACTUATOR PING")) { Serial.println(F("OK ACTUATOR PING")); return; }
  if(commandEquals("ACTUATOR HEARTBEAT")) { Serial.println(F("OK ACTUATOR HEARTBEAT")); return; }

  if(commandEquals("ACTUATOR STOP")) { stopActuatorMotion(true); return; }
  if(commandEquals("SET ACTUATOR UP")) {
    if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
      Serial.println(F("ERR ACTUATOR BUSY")); return;
    }
    actuatorPosition=ACTUATOR_POSITION_UP;
    actuatorCompletedSteps=0;
    Serial.println(F("OK ACTUATOR POSITION SET UP")); return;
  }
  if(commandEquals("SET ACTUATOR DOWN")) {
    if(actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
      Serial.println(F("ERR ACTUATOR BUSY")); return;
    }
    actuatorPosition=ACTUATOR_POSITION_DOWN;
    actuatorCompletedSteps=0;
    Serial.println(F("OK ACTUATOR POSITION SET DOWN")); return;
  }
  if(commandEquals("ACTUATOR DOWN") || commandEquals("DOWN")) {
    startActuatorMotion(ACTUATOR_MOTION_DOWN); return;
  }
  if(commandEquals("ACTUATOR UP") || commandEquals("UP")) {
    startActuatorMotion(ACTUATOR_MOTION_UP); return;
  }

  if(commandEquals("STOP") || commandEquals("STOP ALL")) {
    stopAugerImmediate(false); stopDiskImmediate(true); stopActuatorMotion(false);
    Serial.println(F("OK STOP ALL")); return;
  }
  if(commandEquals("AUGER STOP")) { stopAugerImmediate(false); Serial.println(F("OK AUGER STOP")); return; }
  if(commandEquals("DISK STOP") || commandEquals("DISK DISABLE")) {
    bool disable=commandEquals("DISK DISABLE");
    stopDiskImmediate(true);
    Serial.println(disable ? F("OK DISK DISABLED POSITION UNKNOWN") : F("OK DISK STOPPED POSITION UNKNOWN")); return;
  }
  uint8_t slot=0;
  if(parseSlotArgument("SET SLOT ",slot)) {
    if(!slot) { Serial.println(F("ERR SLOT MUST BE 1..8")); return; }
    if(augerMode!=AUGER_STOPPED || diskMoveActive ||
       actuatorActiveDirection!=ACTUATOR_MOTION_NONE) {
      Serial.println(F("ERR MOTION ACTIVE")); return;
    }
    if(!diskAtStableDetent()) { Serial.println(F("ERR SWITCH MUST BE RELEASED IN DETENT")); return; }
    setDiskDriverEnabled(true);
    delay(DISK_ENABLE_SETTLE_MS);
    if(digitalRead(DISK_SWITCH_PIN)!=HIGH) {
      stopDiskImmediate(true); Serial.println(F("ERR ALIGNMENT CHANGED WHEN ENABLED")); return;
    }
    diskCurrentSlot=slot; diskPositionKnown=true;
    Serial.print(F("OK DISK SLOT SET ")); Serial.println(slot); return;
  }
  if(parseSlotArgument("DISK GOTO ",slot) || parseSlotArgument("DISK SLOT ",slot)) {
    if(!slot) Serial.println(F("ERR SLOT MUST BE 1..8")); else goToDiskSlot(slot);
    return;
  }
  if(commandEquals("DISK NEXT")) { moveDiskOneSlotClockwise(); return; }
  if(commandEquals("DISK PREV")) { Serial.println(F("ERR DISK CLOCKWISE ONLY")); return; }

  // Current Pi protocol: the profile ID selects one exact powder row above.
  uint8_t powderProfileId=0;
  const char *augerPhase=NULL;
  if(parsePowderPhaseArgument("AUGER CONT ",powderProfileId,augerPhase)) {
    if(!powderProfileId)
      Serial.println(F("ERR USE AUGER CONT <PROFILE 1..8> <MAX|TURBO|NORMAL>"));
    else
      startProfileContinuous(powderProfileId,augerPhase);
    return;
  }
  if(parsePowderPhaseArgument("AUGER PULSE ",powderProfileId,augerPhase)) {
    if(!powderProfileId)
      Serial.println(F("ERR USE AUGER PULSE <PROFILE 1..8> <FINE|FINAL>"));
    else
      startProfilePulse(powderProfileId,augerPhase);
    return;
  }

  // Backward-compatible Serial Monitor aliases. Current Pi code does not use
  // these; FREE aliases use profile 1 and NONFREE aliases use profile 5.
  if(commandEquals("MAX") || commandEquals("NONFREE MAX")) {
    if(startProfileContinuous(POWDER_CORNSTARCH,"MAX")) Serial.println(F("OK NONFREE MAX"));
    return;
  }
  if(commandEquals("FREE MAX")) {
    if(startProfileContinuous(POWDER_GRANULATED_SUGAR,"MAX")) Serial.println(F("OK FREE MAX"));
    return;
  }
  if(commandEquals("TURBO")) {
    if(startProfileContinuous(POWDER_CORNSTARCH,"TURBO")) Serial.println(F("OK TURBO"));
    return;
  }
  if(commandEquals("NORMAL")) {
    if(startProfileContinuous(POWDER_CORNSTARCH,"NORMAL")) Serial.println(F("OK NORMAL"));
    return;
  }
  if(commandEquals("FINE")) { startProfilePulse(POWDER_CORNSTARCH,"FINE","FINE"); return; }
  if(commandEquals("FINAL")) { startProfilePulse(POWDER_CORNSTARCH,"FINAL","FINAL"); return; }

  if(commandEquals("AUGER CONT FREE MAX")) { startProfileContinuous(POWDER_GRANULATED_SUGAR,"MAX"); return; }
  if(commandEquals("AUGER CONT FREE TURBO")) { startProfileContinuous(POWDER_GRANULATED_SUGAR,"TURBO"); return; }
  if(commandEquals("AUGER CONT FREE NORMAL")) { startProfileContinuous(POWDER_GRANULATED_SUGAR,"NORMAL"); return; }
  if(commandEquals("AUGER CONT NONFREE MAX")) { startProfileContinuous(POWDER_CORNSTARCH,"MAX"); return; }
  if(commandEquals("AUGER CONT NONFREE TURBO")) { startProfileContinuous(POWDER_CORNSTARCH,"TURBO"); return; }
  if(commandEquals("AUGER CONT NONFREE NORMAL")) { startProfileContinuous(POWDER_CORNSTARCH,"NORMAL"); return; }
  if(commandEquals("AUGER PULSE FREE APPROACH")) { startPulse(80UL,3200UL,NULL); return; }
  if(commandEquals("AUGER PULSE FREE FINE")) { startProfilePulse(POWDER_GRANULATED_SUGAR,"FINE"); return; }
  if(commandEquals("AUGER PULSE FREE FINAL")) { startProfilePulse(POWDER_GRANULATED_SUGAR,"FINAL"); return; }
  if(commandEquals("AUGER PULSE NONFREE APPROACH")) { startProfilePulse(POWDER_CORNSTARCH,"FINE"); return; }
  if(commandEquals("AUGER PULSE NONFREE FINE") || commandEquals("AUGER PULSE NONFREE FINAL")) {
    startProfilePulse(POWDER_CORNSTARCH,"FINAL"); return;
  }
  Serial.print(F("ERR UNKNOWN COMMAND: ")); Serial.println(commandBuffer);
}
void readSerialCommands() {
  // Bound work per loop so a serial stream cannot starve motion/watchdog handling.
  uint8_t budget=32;
  while(budget-- && Serial.available()>0) {
    char c=(char)Serial.read();
    if(c=='\r') continue;
    if(c=='\n') {
      if(!commandOverflow && commandLength) {
        commandBuffer[commandLength]='\0'; processCommand();
      }
      commandLength=0; commandOverflow=false; commandBuffer[0]='\0';
    } else if(!commandOverflow) {
      if(commandLength<COMMAND_BUFFER_SIZE-1) commandBuffer[commandLength++]=c;
      else {
        commandOverflow=true; commandLength=0;
        Serial.println(F("ERR COMMAND TOO LONG"));
        // Discard the WHOLE remainder; never execute an overflow suffix.
      }
    }
  }
}

void setup() {
  // Initialize output latches before enabling outputs.
  digitalWrite(AUGER_ENABLE_PIN,DRIVER_DISABLE_LEVEL);
  digitalWrite(DISK_ENABLE_PIN,DRIVER_DISABLE_LEVEL);
  pinMode(AUGER_STEP_PIN,OUTPUT); pinMode(AUGER_DIR_PIN,OUTPUT);
  pinMode(AUGER_ENABLE_PIN,OUTPUT);
  pinMode(DISK_STEP_PIN,OUTPUT); pinMode(DISK_DIR_PIN,OUTPUT);
  pinMode(DISK_ENABLE_PIN,OUTPUT);
  pinMode(DISK_SWITCH_PIN,INPUT_PULLUP);
  pinMode(ACTUATOR_STEP_PIN,OUTPUT); pinMode(ACTUATOR_DIR_PIN,OUTPUT);
  digitalWrite(AUGER_STEP_PIN,LOW); digitalWrite(AUGER_DIR_PIN,DISPENSE_DIR_LEVEL);
  digitalWrite(DISK_STEP_PIN,LOW); digitalWrite(DISK_DIR_PIN,DISK_CLOCKWISE_DIR_LEVEL);
  digitalWrite(ACTUATOR_STEP_PIN,LOW);
  digitalWrite(ACTUATOR_DIR_PIN,ACTUATOR_DOWN_DIRECTION_LEVEL);
  noInterrupts();
  disconnectStepOutput(); disconnectDiskStepOutput();
  TCCR2A=_BV(WGM21);
  interrupts();
  setDiskDriverEnabled(true);  // Hold after USB reset; position still UNKNOWN.
  switchRawReleased=digitalRead(DISK_SWITCH_PIN)==HIGH;
  switchChangedMs=millis();
  lastSerialContactMs=lastRampUpdateMs=millis();
  commandBuffer[0]='\0';
  Serial.begin(115200);
  Serial.println(F("READY AUGER + SENSOR-INDEXED CW DISK + ACTUATOR"));
  Serial.println(F("DRIVER ALARM INPUTS = DISABLED"));
  Serial.println(F("D2 DETENT INDEXING - SET SLOT n REQUIRED"));
}
void loop() {
  updateSwitch();
  updateWatchdog();
  updatePulseCompletion(); updateDiskCompletion(); updateActuatorMotion();
  readSerialCommands();
  updateContinuousRamp();
}
