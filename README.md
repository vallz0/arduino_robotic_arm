# Robotic Arm Control with Gesture Recognition

This project uses gesture recognition technology with the MediaPipe library in Python to control servos connected to an Arduino. Gesture recognition is done through a camera, and commands are sent to the Arduino via serial communication to control the servos.

## Features

- **Camera gesture recognition**: Through a camera and the MediaPipe library, the regular hand gesture system.
- **Servo control via Arduino**: Depending on the recognized gesture, commands are sent to the Arduino to control two connected servos.
- **Communication via Serial**: Communication between Python and Arduino is done via serial port.

## Repository Structure

```plaintext
arduino_robotic_arm/
│
├── src/                       
│   ├── arduino/               
│   │   ├── ServoController.h   
│   │   ├── ServoController.cpp
│   │   └── main.ino          
│   └── python/                
│       ├── camera.py 
│       ├── gesture_recognizer.py 
│       ├── hand_detector.py 
│       ├── serial_handler.py 
│       └── main.py                 
├── docs/                        
│   └── README.md               
│
└── requirements.txt            
```
## Dependencies

To run Python code, you will need to install the following libraries:
1. Python 3.x

2. Python Libraries: You can install the required dependencies using the requirements.txt file. Run the following command:
```bash 
pip install -r requirements.txt
```
#### Dependencies include:
- opencv-python: For video capture and manipulation.
- mediapipe: For gesture recognition.
- pyserial: For serial communication with Arduino.
3. Arduino IDE: You also need the Arduino IDE to load code into your Arduino.