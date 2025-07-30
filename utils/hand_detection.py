def is_hand_open(landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]

    open_fingers = sum(1 for tip, pip in zip(finger_tips, finger_pips) if landmarks[tip].y < landmarks[pip].y)
    return open_fingers >= 4


def is_hand_closed(landmarks):
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]

    closed_fingers = sum(1 for tip, pip in zip(finger_tips, finger_pips) if landmarks[tip].y > landmarks[pip].y)
    return closed_fingers >= 4
