# Gesture Scroll Youtube Shots

This project allows gesture-based control of YouTube Shorts (or any webpage) using hand gestures from a webcam.


# Gesture Scroll YouTube Shorts Demo 

<p align="center">
  <img src="demo_video/hand_gesture_demo.gif" width="600" alt="Hand Gesture Demo" />
</p>

## ✨ Features

- ✋ **Open hand** → scrolls **up** (previous video)
- ✊ **Closed fist** → scrolls **down** (next video)
- Automatically focuses on your browser window (Chrome, Firefox, Edge, etc.)
- ✅ **Stops scrolling** if only a **single finger** (like the index finger) is detected — useful for pausing at a specific YouTube Short
- Real-time hand gesture detection using [MediaPipe](https://google.github.io/mediapipe/)
- Lightweight and fast — works on most webcams



## 📌 Important Notes:
✅ Ensure your webcam is connected and working.

🖥️ The app automatically brings the browser window into focus when a gesture is detected.

🌐 Open YouTube Shorts in your browser and keep the browser visible, after executing the **main.py** file 

📷 The webcam preview window will open, and you can keep it on one half of the screen and your browser on the other half.

## 🛠 Setup
```bash

git clone https://github.com/your-username/gesture_scroll.git
pip install -r requirements.txt
cd gesture_control_youtube_shots
To run the file --> python main.py**
