#ifndef SERVO_CONTROLLER_H
#define SERVO_CONTROLLER_H

#include <Servo.h>

class ServoController {
public:
    ServoController(int servoPin1, int servoPin2);
    void setup();
    void processCommand(char command);

private:
    Servo meuServo;
    Servo servo2;
    int servoPin1;
    int servoPin2;
};

#endif // SERVO_CONTROLLER_H
