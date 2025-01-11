import cv2


class Camera:
    def __init__(self, camera_index: int = 0) -> None:
        self.cap = cv2.VideoCapture(camera_index)

    def read_frame(self) -> tuple[bool, any]:
        return self.cap.read()

    def release(self) -> None:
        self.cap.release()

    def display_frame(self, window_name: str, frame: any) -> None:
        cv2.imshow(window_name, frame)
