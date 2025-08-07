import face_recognition
import pickle
import cv2
from datetime import datetime
import os
import pandas as pd

ENCODINGS_PATH = "encodings.pkl"

with open(ENCODINGS_PATH, "rb") as f:
    data = pickle.load(f)

def recognize_faces_in_image(image_path):
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)

    names = []
    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matched_idxs = [i for i, b in enumerate(matches) if b]
            counts = {}
            for i in matched_idxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)

        names.append(name)

    today = datetime.now().strftime("%Y-%m-%d")
    output_dir = "previousData"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{today}.txt")

    # Load existing names if file exists
    existing_names = set()
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            existing_names = set(name.strip() for name in f.readlines())

    # Filter new names
    new_names = [name for name in names if name != "Unknown" and name not in existing_names]

    if new_names:
        with open(output_path, "a") as f:
            for name in new_names:
                f.write(name + "\n")
        print(f"[UPDATED] Added {len(new_names)} new name(s) to: {output_path}")
    else:
        print(f"[NO NEW NAMES] File already has all recognized names for today.")

    return names
