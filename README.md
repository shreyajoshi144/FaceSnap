# FaceSnap  
**Real-Time Face Recognition System using Python & OpenCV**

FaceSnap is a Python-based face recognition system that can identify people from images or a webcam feed. It uses OpenCV’s LBPH (Local Binary Patterns Histograms) face recognizer to train on a dataset of faces and predict identities in real time.
This project demonstrates image processing, machine learning, and file handling using Python.
--
Features

- Train a face recognition model from a dataset of labeled images.
- Save the trained model and label mapping for later use.
- Recognize faces from images or live webcam feed.
- Handles multiple persons and labels automatically.

Technologies Used

- Python 3
- OpenCV (cv2)
- NumPy
- LBPH Face Recognizer
--

## Project Structure
- FaceSnap.py → Main menu (launcher for all modules)
- capture_faces.py → Capture images for a new person
- train_model.py → Train the recognition model
- recognize_realtime.py → Real-time face recognition
- search_history.py → View recognition logs/history
- faces/ → Stores captured face images
- model/ → Saves the trained model
- history/ → Stores recognition/alert logs
- requirements.txt → Project dependencies
- README.md → Project documentation
