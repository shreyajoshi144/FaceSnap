import cv2
import os

def capture_faces(person_name, dataset_path="dataset"):
    """
    Captures face images of a new person using webcam and stores them.
    """
    person_dir = os.path.join(dataset_path, person_name)
    os.makedirs(person_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    count = 0
    print(f"[INFO] Capturing faces for {person_name}. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            file_path = os.path.join(person_dir, f"{person_name}_{count}.jpg")
            cv2.imwrite(file_path, face_img)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Face Capture", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"[INFO] Saved {count} face images for {person_name}.")

# ✅ Run directly if called
if __name__ == "__main__":
    name = input("Enter the name of the person: ")
    capture_faces(name)
