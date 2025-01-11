import cv2
from camera import Camera
from hand_detector import HandDetector
from gesture_recognizer import GestureRecognizer
from serial_handler import SerialHandler


def main():
    camera = Camera(camera_index=1)
    hand_detector = HandDetector()
    serial_handler = SerialHandler(port="COM6")

    try:
        while True:
            ret, frame = camera.read_frame()
            if not ret:
                print("Falha ao acessar a câmera.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hand_detector.process_frame(frame_rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    hand_detector.draw_landmarks(frame, hand_landmarks)

                gesture = GestureRecognizer.recognize_gesture(result.multi_hand_landmarks[0].landmark)
                cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

                if gesture == "Mão aberta":
                    serial_handler.send_data(b'A')
                elif gesture == "Mão fechada":
                    serial_handler.send_data(b'C')
                elif gesture == "Sinal de V":
                    serial_handler.send_data(b'B')

            camera.display_frame("Reconhecimento de Gestos", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        hand_detector.release()
        serial_handler.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
