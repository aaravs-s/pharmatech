#include <Arduino.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

/*
  Eight-position powder disk indexer test

  Target board:
    Arduino Uno R3 / Nano with ATmega328P (16 MHz AVR)

  Purpose:
    Move a directly driven eight-slot disk exactly 1/8 revolution whenever a
    newline-terminated serial command is received.

  Serial settings:
    115200 baud, Newline or Both NL & CR line ending

  Commands:
    PING          -> reply without moving
    STATUS        -> print motion, enable, slot, and calibration status
    DISK NEXT     -> move one slot in the forward direction
    DISK PREV     -> move one slot in the reverse direction
    DISK GOTO 5   -> move to slot 5 using the shortest path
    SET SLOT 1    -> declare the currently aligned physical slot (1 through 8)
    ENABLE        -> energize/hold the motor without moving
    DISABLE       -> de-energize the motor without moving
    STOP          -> stop immediately; logical position becomes unknown
    STOP ALL      -> same as STOP
    HELP          -> print the command list

  UIM344-series pulse/direction signal wiring used by the existing project:
    Brown  COM       -> Arduino GND
    Gray   DIR       -> Arduino D12
    Yellow PLS/STEP  -> Arduino D11
    Blue   ENA/SD    -> Arduino D4

  The motor power supply is separate from the Arduino. Never connect motor
  supply voltage to an Arduino pin.

  Important calibration assumptions:
    - The motor is 1.8 degrees / 200 full steps per revolution.
    - The integrated driver is configured for 1/32 microstepping.
    - The motor drives the disk 1:1, with no gearing or belt reduction.

  With those assumptions:
    200 * 32 / 8 = 800 STEP pulses for one slot.

  If the configured microstep value or drive ratio differs, update the
  constants below before relying on the slot position.
*/

// ============================================================
// PIN AND DRIVER LOGIC CONFIGURATION
// ============================================================

// D8, D9, and D10 remain available to the existing auger motor.
const uint8_t DISK_STEP_PIN = 11;   // OC2A on ATmega328P
const uint8_t DISK_DIR_PIN = 12;
const uint8_t DISK_ENABLE_PIN = 4;
const uint8_t DISK_ALARM_PIN = 6;   // Optional; leave disconnected if unused

// These levels match the currently supplied working auger firmware.
// If the disk motor uses the opposite configured input logic, verify it with
// the disk mechanically disconnected before changing these two constants.
const uint8_t DRIVER_ENABLE_LEVEL = HIGH;
const uint8_t DRIVER_DISABLE_LEVEL = LOW;

// Swap HIGH and LOW here if DISK NEXT turns the wrong way.
const uint8_t FORWARD_DIR_LEVEL = HIGH;
const uint8_t REVERSE_DIR_LEVEL = LOW;

// Holding after a completed move prevents a loaded disk from drifting away
// from the selected slot. STOP and DISABLE always release the motor.
const bool HOLD_AFTER_MOVE = true;

// ============================================================
// DISK CALIBRATION
// ============================================================

const uint32_t MOTOR_FULL_STEPS_PER_REVOLUTION = 200UL;
const uint32_t DRIVER_MICROSTEPS = 32UL;
const uint32_t DISK_SLOT_COUNT = 8UL;

// Direct drive is 1 motor revolution per 1 disk revolution.
// Example: a 2:1 reduction requiring two motor revolutions for one disk
// revolution would use numerator 2 and denominator 1.
const uint32_t MOTOR_REVS_PER_DISK_REV_NUMERATOR = 1UL;
const uint32_t MOTOR_REVS_PER_DISK_REV_DENOMINATOR = 1UL;

const uint32_t STEP_CALCULATION_NUMERATOR =
    MOTOR_FULL_STEPS_PER_REVOLUTION * DRIVER_MICROSTEPS *
    MOTOR_REVS_PER_DISK_REV_NUMERATOR;
const uint32_t STEP_CALCULATION_DENOMINATOR =
    DISK_SLOT_COUNT * MOTOR_REVS_PER_DISK_REV_DENOMINATOR;
const uint32_t STEPS_PER_SLOT =
    STEP_CALCULATION_NUMERATOR / STEP_CALCULATION_DENOMINATOR;

// UIROBOT recommends starting motor tests at a conservative pulse rate.
// At 800 steps per slot, 1000 Hz takes about 0.8 seconds per index.
const uint32_t INDEX_STEP_FREQUENCY_HZ = 1000UL;
const uint16_t ENABLE_SETTLE_MS = 20;
const uint16_t DIRECTION_SETTLE_US = 20;

// ============================================================
// MOTION STATE
// ============================================================

volatile bool moveActive = false;
volatile bool moveFinished = false;
volatile uint32_t compareMatchesRemaining = 0;

int8_t pendingSlotDirection = 0;
uint8_t pendingSlotsToMove = 0;
uint8_t pendingTargetSlot = 0;
uint8_t currentSlot = 1;
bool positionKnown = false;
bool driverEnabled = false;

// ============================================================
// SERIAL INPUT
// ============================================================

const uint8_t COMMAND_BUFFER_SIZE = 48;
char commandBuffer[COMMAND_BUFFER_SIZE];
uint8_t commandLength = 0;

// ============================================================
// TIMER2 HELPERS
// ============================================================

uint8_t frequencyToOcr(uint32_t frequencyHz) {
  const uint32_t timerPrescaler = 64UL;

  // With a 16 MHz clock, prescaler 64, and an 8-bit compare register,
  // the lowest representable STEP rate is approximately 488 Hz.
  if (frequencyHz < 489UL) {
    frequencyHz = 489UL;
  }

  // Timer2 CTC, prescaler 64, OC2A toggles at each compare match.
  // Rising-edge STEP frequency = F_CPU / (2 * 64 * (OCR2A + 1)).
  uint32_t ocr =
      (F_CPU / (2UL * timerPrescaler * frequencyHz)) - 1UL;

  if (ocr > 255UL) {
    ocr = 255UL;
  }
  if (ocr < 1UL) {
    ocr = 1UL;
  }

  return (uint8_t)ocr;
}

void disconnectStepOutput() {
  TCCR2A &= ~_BV(COM2A0);
  TIMSK2 &= ~_BV(OCIE2A);
  digitalWrite(DISK_STEP_PIN, LOW);
}

void setDriverEnabled(bool enabled) {
  digitalWrite(
      DISK_ENABLE_PIN,
      enabled ? DRIVER_ENABLE_LEVEL : DRIVER_DISABLE_LEVEL
  );
  driverEnabled = enabled;
}

void stopMotion(bool announce) {
  bool wasMoving;
  bool wasEnabled = driverEnabled;

  noInterrupts();
  wasMoving = moveActive;
  disconnectStepOutput();
  compareMatchesRemaining = 0;
  moveActive = false;
  moveFinished = false;
  interrupts();

  pendingSlotDirection = 0;
  pendingSlotsToMove = 0;
  pendingTargetSlot = 0;
  setDriverEnabled(false);

  // Once holding torque is released, software alone cannot guarantee that a
  // loaded disk has remained aligned, even if no STEP pulse was commanded.
  if (wasMoving || wasEnabled) {
    positionKnown = false;
  }

  if (announce) {
    Serial.println(wasMoving ? "OK STOPPED POSITION UNKNOWN" : "OK STOPPED");
  }
}

bool calibrationIsIntegral() {
  return STEP_CALCULATION_DENOMINATOR != 0 &&
         (STEP_CALCULATION_NUMERATOR % STEP_CALCULATION_DENOMINATOR) == 0;
}

void startSlotMove(
    int8_t slotDirection,
    uint8_t slotsToMove,
    uint8_t targetSlot
) {
  if (moveActive) {
    Serial.println("ERR BUSY");
    return;
  }

  if (!calibrationIsIntegral() || STEPS_PER_SLOT == 0 || slotsToMove == 0) {
    Serial.println("ERR INVALID STEP CALIBRATION");
    return;
  }

  uint32_t totalSteps = STEPS_PER_SLOT * (uint32_t)slotsToMove;

  pendingSlotDirection = slotDirection;
  pendingSlotsToMove = slotsToMove;
  pendingTargetSlot = targetSlot;

  digitalWrite(
      DISK_DIR_PIN,
      slotDirection > 0 ? FORWARD_DIR_LEVEL : REVERSE_DIR_LEVEL
  );
  setDriverEnabled(true);

  delay(ENABLE_SETTLE_MS);
  delayMicroseconds(DIRECTION_SETTLE_US);

  noInterrupts();
  disconnectStepOutput();
  digitalWrite(DISK_STEP_PIN, LOW);
  OCR2A = frequencyToOcr(INDEX_STEP_FREQUENCY_HZ);
  TCNT2 = 0;
  TIFR2 = _BV(OCF2A);

  // OC2A starts LOW and toggles twice for each complete STEP pulse.
  compareMatchesRemaining = totalSteps * 2UL;
  moveFinished = false;
  moveActive = true;

  TCCR2A |= _BV(COM2A0);
  TIMSK2 |= _BV(OCIE2A);
  interrupts();

  Serial.print("OK MOVING ");
  Serial.print(slotDirection > 0 ? "NEXT" : "PREV");
  Serial.print(" SLOTS=");
  Serial.print(slotsToMove);
  Serial.print(" STEPS=");
  Serial.println(totalSteps);
}

void startOneSlotMove(int8_t slotDirection) {
  uint8_t targetSlot = 0;

  if (positionKnown) {
    if (slotDirection > 0) {
      targetSlot = currentSlot == DISK_SLOT_COUNT ? 1 : currentSlot + 1;
    } else {
      targetSlot = currentSlot == 1 ? DISK_SLOT_COUNT : currentSlot - 1;
    }
  }

  startSlotMove(slotDirection, 1, targetSlot);
}

ISR(TIMER2_COMPA_vect) {
  if (!moveActive || compareMatchesRemaining == 0) {
    return;
  }

  compareMatchesRemaining--;

  if (compareMatchesRemaining == 0) {
    TCCR2A &= ~_BV(COM2A0);
    TIMSK2 &= ~_BV(OCIE2A);
    moveActive = false;
    moveFinished = true;
  }
}

void updateMoveCompletion() {
  if (!moveFinished) {
    return;
  }

  noInterrupts();
  moveFinished = false;
  interrupts();

  digitalWrite(DISK_STEP_PIN, LOW);

  if (positionKnown && pendingTargetSlot >= 1 &&
      pendingTargetSlot <= DISK_SLOT_COUNT) {
    currentSlot = pendingTargetSlot;
  }

  pendingSlotDirection = 0;
  pendingSlotsToMove = 0;
  pendingTargetSlot = 0;

  if (!HOLD_AFTER_MOVE) {
    setDriverEnabled(false);
  }

  if (positionKnown) {
    Serial.print("DONE SLOT ");
    Serial.println(currentSlot);
  } else {
    Serial.println("DONE SLOT UNKNOWN - USE SET SLOT n WHEN ALIGNED");
  }
}

// ============================================================
// STATUS AND COMMANDS
// ============================================================

void printHelp() {
  Serial.println("COMMANDS: PING | STATUS | DISK NEXT | DISK PREV | DISK GOTO 1..8");
  Serial.println("          SET SLOT 1..8 | ENABLE | DISABLE | STOP | STOP ALL | HELP");
}

void printStatus() {
  Serial.print("STATUS MOVING=");
  Serial.print(moveActive ? "YES" : "NO");
  Serial.print(" ENABLED=");
  Serial.print(driverEnabled ? "YES" : "NO");
  Serial.print(" SLOT=");

  if (positionKnown) {
    Serial.print(currentSlot);
  } else {
    Serial.print("UNKNOWN");
  }

  Serial.print(" STEPS_PER_SLOT=");
  Serial.print(STEPS_PER_SLOT);
  Serial.print(" STEP_HZ=");
  Serial.println(INDEX_STEP_FREQUENCY_HZ);
}

void normalizeCommand(char* text) {
  char* start = text;
  while (*start != '\0' && isspace((unsigned char)*start)) {
    start++;
  }

  if (start != text) {
    memmove(text, start, strlen(start) + 1);
  }

  size_t length = strlen(text);
  while (length > 0 && isspace((unsigned char)text[length - 1])) {
    text[--length] = '\0';
  }

  for (size_t index = 0; text[index] != '\0'; index++) {
    text[index] = (char)toupper((unsigned char)text[index]);
  }
}

bool parseSlotArgument(const char* prefix, uint8_t& requestedSlot) {
  const size_t prefixLength = strlen(prefix);

  if (strncmp(commandBuffer, prefix, prefixLength) != 0) {
    return false;
  }

  const char* numberText = commandBuffer + prefixLength;
  char* end = NULL;
  long parsed = strtol(numberText, &end, 10);

  if (end == numberText || *end != '\0' || parsed < 1 ||
      parsed > (long)DISK_SLOT_COUNT) {
    requestedSlot = 0;
    return true;
  }

  requestedSlot = (uint8_t)parsed;
  return true;
}

void goToSlot(uint8_t requestedSlot) {
  if (!positionKnown) {
    Serial.println("ERR POSITION UNKNOWN - ALIGN DISK AND SEND SET SLOT n");
    return;
  }

  uint8_t forwardDistance =
      (requestedSlot + DISK_SLOT_COUNT - currentSlot) % DISK_SLOT_COUNT;
  uint8_t reverseDistance =
      (currentSlot + DISK_SLOT_COUNT - requestedSlot) % DISK_SLOT_COUNT;

  if (forwardDistance == 0) {
    setDriverEnabled(true);
    Serial.print("DONE SLOT ");
    Serial.print(currentSlot);
    Serial.println(" ALREADY THERE");
    return;
  }

  // If both paths are four slots long, choose the forward direction.
  if (forwardDistance <= reverseDistance) {
    startSlotMove(1, forwardDistance, requestedSlot);
  } else {
    startSlotMove(-1, reverseDistance, requestedSlot);
  }
}

void processCommand() {
  normalizeCommand(commandBuffer);

  if (strcmp(commandBuffer, "PING") == 0) {
    Serial.println("OK PING");
    return;
  }

  if (strcmp(commandBuffer, "STATUS") == 0) {
    printStatus();
    return;
  }

  if (strcmp(commandBuffer, "STOP") == 0 ||
      strcmp(commandBuffer, "STOP ALL") == 0) {
    stopMotion(true);
    return;
  }

  if (strcmp(commandBuffer, "HELP") == 0) {
    printHelp();
    return;
  }

  if (moveActive) {
    Serial.println("ERR BUSY - SEND STOP FIRST");
    return;
  }

  if (strcmp(commandBuffer, "DISK NEXT") == 0) {
    startOneSlotMove(1);
    return;
  }

  if (strcmp(commandBuffer, "DISK PREV") == 0) {
    startOneSlotMove(-1);
    return;
  }

  uint8_t requestedSlot = 0;
  if (parseSlotArgument("DISK GOTO ", requestedSlot)) {
    if (requestedSlot == 0) {
      Serial.println("ERR SLOT MUST BE 1..8");
      return;
    }

    goToSlot(requestedSlot);
    return;
  }

  if (strcmp(commandBuffer, "ENABLE") == 0) {
    setDriverEnabled(true);
    Serial.println("OK ENABLED");
    return;
  }

  if (strcmp(commandBuffer, "DISABLE") == 0) {
    positionKnown = false;
    setDriverEnabled(false);
    Serial.println("OK DISABLED POSITION UNKNOWN");
    return;
  }

  requestedSlot = 0;
  if (parseSlotArgument("SET SLOT ", requestedSlot)) {
    if (requestedSlot == 0) {
      Serial.println("ERR SLOT MUST BE 1..8");
      return;
    }

    currentSlot = requestedSlot;
    positionKnown = true;
    Serial.print("OK SLOT SET ");
    Serial.println(currentSlot);
    return;
  }

  Serial.print("ERR UNKNOWN COMMAND: ");
  Serial.println(commandBuffer);
}

void readSerialCommands() {
  while (Serial.available() > 0) {
    char incoming = (char)Serial.read();

    if (incoming == '\r') {
      continue;
    }

    if (incoming == '\n') {
      commandBuffer[commandLength] = '\0';

      if (commandLength > 0) {
        processCommand();
      }

      commandLength = 0;
      commandBuffer[0] = '\0';
      continue;
    }

    if (commandLength < COMMAND_BUFFER_SIZE - 1) {
      commandBuffer[commandLength++] = incoming;
    } else {
      commandLength = 0;
      commandBuffer[0] = '\0';
      Serial.println("ERR COMMAND TOO LONG");
    }
  }
}

void checkDriverAlarm() {
  // With no alarm wire connected, INPUT_PULLUP reads HIGH and will not fault.
  if (digitalRead(DISK_ALARM_PIN) == LOW) {
    bool shouldReport = moveActive || driverEnabled;
    stopMotion(false);

    if (shouldReport) {
      Serial.println("FAULT DRIVER ALARM - POSITION UNKNOWN");
    }
  }
}

// ============================================================
// SETUP / LOOP
// ============================================================

void setup() {
  pinMode(DISK_STEP_PIN, OUTPUT);
  pinMode(DISK_DIR_PIN, OUTPUT);
  pinMode(DISK_ENABLE_PIN, OUTPUT);
  pinMode(DISK_ALARM_PIN, INPUT_PULLUP);

  digitalWrite(DISK_STEP_PIN, LOW);
  digitalWrite(DISK_DIR_PIN, FORWARD_DIR_LEVEL);
  setDriverEnabled(false);

  Serial.begin(115200);

  // Timer2 CTC with prescaler 64. OC2A is disconnected until a move starts.
  TCCR2A = _BV(WGM21);
  TCCR2B = _BV(CS22);
  TIMSK2 = 0;
  OCR2A = frequencyToOcr(INDEX_STEP_FREQUENCY_HZ);
  TCNT2 = 0;

  commandBuffer[0] = '\0';

  Serial.println("READY 8-SLOT DISK TEST");
  Serial.print("STEPS PER SLOT = ");
  Serial.println(STEPS_PER_SLOT);

  if (!calibrationIsIntegral()) {
    Serial.println("FAULT STEP CALCULATION IS NOT AN INTEGER");
  }

  Serial.println("POSITION UNKNOWN - ALIGN DISK, THEN SEND SET SLOT 1");
  printHelp();
}

void loop() {
  readSerialCommands();
  updateMoveCompletion();
  checkDriverAlarm();
}
