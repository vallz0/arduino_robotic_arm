import serial


class SerialHandler:
    def __init__(self, port: str, baudrate: int = 9600) -> None:
        self.arduino = serial.Serial(port, baudrate)

    def send_data(self, data: bytes) -> None:
        self.arduino.write(data)

    def close(self) -> None:
        self.arduino.close()
