import sys
import subprocess

def run_script(script_name):
    """
    Runs another Python script using the same interpreter as FaceSnap.py
    """
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except Exception as e:
        print(f"⚠️ Error running {script_name}: {e}")

def main():
    while True:
        print("\n===== FaceSnap Menu =====")
        print("1. Capture Faces")
        print("2. Train Model")
        print("3. Recognize Faces (Run Attendance)")
        print("4. Show Attendance")
        print("5. Alert on New Person")
        print("6. Exit")
        choice = input("Enter your choice (1–6): ")

        if choice == "1":
            run_script("capture_faces.py")
        elif choice == "2":
            run_script("train_model.py")
        elif choice == "3":
            run_script("recognize_faces.py")
        elif choice == "4":
            run_script("attendance.py")
        elif choice == "5":
            run_script("alert_new_person.py")
        elif choice == "6":
            print("✅ Exiting FaceSnap. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

