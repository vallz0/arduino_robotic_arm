from typing import List, Optional
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmark
from mediapipe.python.solutions.hands import HandLandmark


class GestureRecognizer:
    @staticmethod
    def recognize_gesture(landmarks: List[NormalizedLandmark]) -> str:
        if not landmarks:
            return "Gesto não identificado"

        dedos_abertos = []
        dedos = [
            landmarks[HandLandmark.THUMB_TIP],
            landmarks[HandLandmark.INDEX_FINGER_TIP],
            landmarks[HandLandmark.MIDDLE_FINGER_TIP],
            landmarks[HandLandmark.RING_FINGER_TIP],
            landmarks[HandLandmark.PINKY_TIP],
        ]
        bases = [
            landmarks[HandLandmark.THUMB_CMC],
            landmarks[HandLandmark.INDEX_FINGER_MCP],
            landmarks[HandLandmark.MIDDLE_FINGER_MCP],
            landmarks[HandLandmark.RING_FINGER_MCP],
            landmarks[HandLandmark.PINKY_MCP],
        ]

        for dedo, base in zip(dedos, bases):
            dedos_abertos.append(dedo.y < base.y)

        if dedos_abertos == [False, True, True, False, False]:
            return "Sinal de V"
        elif dedos_abertos == [True, True, True, True, True]:
            return "Mão aberta"
        elif dedos_abertos == [True, False, False, False, False]:
            return "Mão fechada"

        return "Gesto não identificado"
