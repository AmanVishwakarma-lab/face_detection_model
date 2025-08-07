from flask import Flask, request, jsonify
import os
from recognize_faces import recognize_faces_in_image

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/recognize", methods=["POST"])
def recognize():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image_file = request.files["image"]
    file_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
    image_file.save(file_path)

    names = recognize_faces_in_image(file_path)

    os.remove(file_path)  # delete after processing
    return jsonify({"recognized_faces": names})

if __name__ == "__main__":
    app.run(debug=True)