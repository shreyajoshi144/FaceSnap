import cv2
import os
import numpy as np
from datetime import datetime

# Paths
faces_dir = "faces"
model_path = "model/facerecognizer.yml"
history_file = "history/recognitions.csv"

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
if not os.path.exists(model_path):
    print("Model not found. Please run training first.")
    exit()
recognizer.read(model_path)

# Load label names
labels = {}
with open("model/labels.txt", "r") as f:
    for line in f:
        id_, name = line.strip().split(",")
        labels[int(id_)] = name

# Ensure history directory exists
os.makedirs("history", exist_ok=True)

# Initialize camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

print("Starting real-time recognition. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_, confidence = recognizer.predict(roi_gray)

        if confidence < 80:  # Threshold for known face
            name = labels.get(id_, "Unknown")
            cv2.putText(frame, f"{name} ({round(confidence,2)})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # Greet known person
            print(f"Hi, {name}!")

            # Log recognition
            with open(history_file, "a") as f:
                f.write(f"{datetime.now()}, {name}, {round(confidence,2)}\n")

        else:
            # Unknown person alert
            cv2.putText(frame, "Unknown", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            print("⚠ ALERT: Unknown person detected!")

            # Log unknown
            with open(history_file, "a") as f:
                f.write(f"{datetime.now()}, Unknown, {round(confidence,2)}\n")

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("Face Recognition - FaceNav", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
