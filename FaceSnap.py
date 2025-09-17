import subprocess
import sys


def run_script(script_name):
    try:
        print(f"[INFO] Running {script_name}...")
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error running {script_name}: {e}")
    except FileNotFoundError:
        print(f"❌ Could not find {script_name}. Please check the file name.")


def main():
    while True:
        print("\n===== FaceSnap Menu =====")
        print("1. Capture Faces")
        print("2. Train Model")
        print("3. Recognize Faces (Realtime)")
        print("4. Search History")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            run_script("capture_faces.py")
        elif choice == "2":
            run_script("train_model.py")
        elif choice == "3":
            run_script("recognize_realtime.py")
        elif choice == "4":
            run_script("search_history.py")
        elif choice == "5":
            print("[INFO] Exiting FaceSnap. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
