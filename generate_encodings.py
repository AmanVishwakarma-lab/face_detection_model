import face_recognition
import os
import pickle

KNOWN_FACES_DIR = "known_faces"
ENCODINGS_PATH = "encodings.pkl"

known_encodings = []
known_names = []

print("[INFO] Loading and encoding faces...")

for filename in os.listdir(KNOWN_FACES_DIR):
    path = os.path.join(KNOWN_FACES_DIR, filename)
    name, ext = os.path.splitext(filename)

    image = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        known_encodings.append(encodings[0])
        known_names.append(name)
        print(f"[DEBUG] Processed {filename} as {name}")
    else:
        print(f"[WARNING] No face found in {filename}")

with open(ENCODINGS_PATH, "wb") as f:
    pickle.dump({"encodings": known_encodings, "names": known_names}, f)

print("[DONE] Encodings saved to encodings.pkl")
