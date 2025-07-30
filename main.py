import cv2
import mediapipe as mp
import pyautogui
import time
import asyncio
import platform
import logging

from utils.hand_detection import is_hand_open, is_hand_closed
from utils.window_focus import focus_browser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85
)
mp_drawing = mp.solutions.drawing_utils

SCROLL_AMOUNT = 500
COOLDOWN = 0.8
last_action = 0


async def main():
    global last_action

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        logging.error("Could not open webcam.")
        print("Error: Could not open webcam.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    logging.info("Webcam initialized.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            logging.error("Could not read frame.")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                current_time = time.time()
                if current_time - last_action < COOLDOWN:
                    continue

                if not focus_browser():
                    cv2.putText(frame, "Browser not found", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    continue

                if is_hand_open(hand_landmarks.landmark):
                    pyautogui.scroll(SCROLL_AMOUNT)
                    last_action = current_time
                    cv2.putText(frame, "Previous Video", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                elif is_hand_closed(hand_landmarks.landmark):
                    pyautogui.scroll(-SCROLL_AMOUNT)
                    last_action = current_time
                    cv2.putText(frame, "Next Video", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "No hand detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('Gesture Control', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            logging.info("Quitting app.")
            break

        await asyncio.sleep(1.0 / 60)

    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    logging.info("Resources released.")


if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())
