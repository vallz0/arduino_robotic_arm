#include "ServoController.h"
#include <Servo.h>

ServoController::ServoController(int pin1, int pin2) 
    : servoPin1(pin1), servoPin2(pin2) {}

void ServoController::setup() {
    meuServo.attach(servoPin1);
    meuServo.write(45);
    servo2.attach(servoPin2);
    servo2.write(90);
}

void ServoController::processCommand(char command) {
    if (command == 'A') {
        meuServo.write(45);
    } else if (command == 'C') {
        meuServo.write(120);
    } else if (command == 'B') {
        servo2.write(0);
    }
}
