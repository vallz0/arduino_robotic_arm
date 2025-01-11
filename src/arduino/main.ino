#include <ServoController.h>

ServoController servoController(9, 10);

void setup() {
    Serial.begin(9600);
    servoController.setup();
}

void loop() {
    if (Serial.available() > 0) {
        char comando = Serial.read();
        servoController.processCommand(comando);
    }
}
