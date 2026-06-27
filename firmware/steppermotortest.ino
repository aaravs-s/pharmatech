#include <AccelStepper.h>

// defines pins numbers
const int stepPin = 3;
const int directionPin = 2;


// Define a stepper and the pins it will use
// 1 or AccelStepper::DRIVER means a stepper driver (with Step and Direction pins)
AccelStepper stepper(AccelStepper::DRIVER, stepPin, directionPin);

void setup()
{
  Serial.begin(9600);

 
  //stepper.setPinsInverted(false, false, true);
  stepper.enableOutputs();
  stepper.setMaxSpeed(1000);
  stepper.setSpeed(600);
}

void loop()
{
  stepper.runSpeed();
}
