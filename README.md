# FaceSnap
A simple real time face recognition project using OpenCV in Python
# FaceSnap  
**Real-Time Face Recognition System using Python & OpenCV**

FaceSnap is a beginner-friendly yet powerful project that demonstrates **real-time face detection and recognition** using OpenCV. It allows capturing faces, training a recognition model, and running live recognition with history logging.

---

## Features
- **Capture Faces** – Collect face images for new users.  
- **Train Model** – Train an LBPH (Local Binary Patterns Histogram) model.  
- **Real-Time Recognition** – Recognize faces live using your webcam.  
- **Search History** – View recognition logs and events.  
- **New Person Alert** – Display alerts when an unknown person is detected.  
- **Interactive Menu** – One main script (`FaceSnap.py`) to control everything.

---

## Tech Stack
- **Python 3**  
- **OpenCV** (cv2)  
- **NumPy**  

---

## Project Structure
FaceSnap/
│── FaceSnap.py # Main menu (launcher)
│── capture_faces.py # Capture images
│── train_model.py # Train recognition model
│── recognize_realtime.py # Real-time recognition
│── search_history.py # View recognition history
│── faces/ # Captured faces (dataset)
│── model/ # Trained model files
│── history/ # Logs of recognized/unknown persons
│── requirements.txt # Dependencies
│── README.md # Documentation
