import cv2
import os
import face_recognition

# Folder to save known face images
KNOWN_FACES_DIR = "known_faces"
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

# Ask user for their name
# name = input("Enter your name: ").strip()
# if not name:
#     print("[ERROR] Name cannot be empty.")
#     exit()
name="shub"

print("[INFO] Position your face. Press ENTER to capture, ESC to cancel...")

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("[ERROR] Cannot access webcam.")
    exit()

while True:
    ret, frame = cap.read()
    # if not ret:
    #     print("[ERROR] Failed to read frame from webcam.")
    #     break

    # Show webcam feed
    cv2.imshow("Capture Face - Press ENTER to Capture", frame)
   

    if cv2.waitKey(1) == 13:  # ENTER key
        # Convert frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face in RGB image
        face_locations = face_recognition.face_locations(rgb_frame)

        if face_locations:
            # Save the original BGR frame with face
            filepath = os.path.join(KNOWN_FACES_DIR, f"{name}.jpg")
            cv2.imwrite(filepath, frame)
            print(f"[SAVED] Face image saved as: {filepath}")
        else:
            print("[WARNING] No face detected. Try again.")
        break

    elif cv2.waitKey(1) == 27:  # ESC key
        print("[CANCELLED] Operation cancelled.")
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
