import cv2
import os
import numpy as np
import pickle

def train_model(dataset_path="dataset", model_path="model/face_recognizer.pkl", labels_path="model/labels.pkl"):
    """
    Trains an LBPH face recognizer model from dataset and saves the model and label encodings.
    """
    faces = []
    labels = []
    label_ids = {}
    current_id = 0

    # Ensure "model" folder exists safely
    if os.path.exists("model") and not os.path.isdir("model"):
        os.remove("model")  # Remove file if exists with same name
    os.makedirs("model", exist_ok=True)

    # Loop through each person's folder in the dataset
    for person_name in os.listdir(dataset_path):
        person_dir = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_dir):
            continue  # Skip if not a folder

        for img_name in os.listdir(person_dir):
            img_path = os.path.join(person_dir, img_name)
            try:
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    print(f"Warning: Could not read image {img_path}")
                    continue
                faces.append(img)

                # Assign numeric labels
                if person_name not in label_ids:
                    label_ids[person_name] = current_id
                    current_id += 1
                labels.append(label_ids[person_name])
            except Exception as e:
                print(f"Error processing image {img_path}: {e}")

    # Convert labels to numpy array
    labels = np.array(labels)

    # Train LBPH face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, labels)

    # Save the trained model
    recognizer.save(model_path)
    print(f"Model saved at {model_path}")

    # Save the labels mapping
    with open(labels_path, "wb") as f:
        pickle.dump(label_ids, f)
    print(f"Labels saved at {labels_path}")


if __name__ == "__main__":
    train_model()
