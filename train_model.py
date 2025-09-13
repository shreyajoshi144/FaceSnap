import cv2
import os
import numpy as np
import pickle

def train_model(dataset_path="dataset", model_path="face_model.yml", labels_path="labels.pkl"):
    """
    Trains a face recognizer using images in the dataset.
    """
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    faces, labels = [], []
    label_ids = {}
    current_id = 0

    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith("jpg") or file.endswith("png"):
                path = os.path.join(root, file)
                person_name = os.path.basename(root)

                if person_name not in label_ids:
                    label_ids[person_name] = current_id
                    current_id += 1

                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                detected_faces = face_cascade.detectMultiScale(img, 1.2, 5)

                for (x, y, w, h) in detected_faces:
                    faces.append(img[y:y+h, x:x+w])
                    labels.append(label_ids[person_name])

    face_recognizer.train(faces, np.array(labels))
    face_recognizer.save(model_path)

    with open(labels_path, "wb") as f:
        pickle.dump(label_ids, f)

    print("[INFO] Training complete. Model saved.")
