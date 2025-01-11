import mediapipe as mp
import cv2
from typing import Optional


class HandDetector:
    def __init__(self, min_detection_confidence: float = 0.7, min_tracking_confidence: float = 0.5) -> None:
        self.hands = mp.solutions.hands.Hands(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.hand_connections = mp.solutions.hands.HAND_CONNECTIONS

    def process_frame(self, frame_rgb: any) -> Optional[any]:
        return self.hands.process(frame_rgb)

    def draw_landmarks(self, frame: any, landmarks: any) -> None:
        self.mp_drawing.draw_landmarks(frame, landmarks, self.hand_connections)

    def release(self) -> None:
        self.hands.close()
