import cv2
import pickle
import os

def recognize_realtime(model_path="model/face_recognizer.pkl", labels_path="model/labels.pkl"):
    """
    Runs real-time face recognition using trained LBPH model.
    """
    # Check if model exists
    if not os.path.exists(model_path) or not os.path.exists(labels_path):
        print("⚠️ No trained model found. Please run 'Train Model' first (option 2).")
        return

    # Load recognizer + labels
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(model_path)

    with open(labels_path, "rb") as f:
        labels = pickle.load(f)
    labels = {v: k for k, v in labels.items()}  # reverse: id → name

    # Initialize webcam + face detector
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print("[INFO] Recognition started. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)

            if conf < 70:  # lower conf → more confident
                name = labels.get(id_, "Unknown")
                color = (0, 255, 0)  # green for known
            else:
                name = "Unknown"
                color = (0, 0, 255)  # red for unknown

            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Recognition stopped.")

# ✅ Run directly if called
if __name__ == "__main__":
    recognize_realtime()

