from flask import Flask, request, render_template, send_from_directory
import os
from huffman import HuffmanCoding

app = Flask(__name__)

# Folder to store uploaded and processed files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_file():
    if "file" not in request.files:
        return "No file uploaded.", 400

    file = request.files["file"]
    if file.filename == "":
        return "No file selected.", 400

    # Save the uploaded file
    input_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(input_path)

    # Compress and decompress using HuffmanCoding
    huffman = HuffmanCoding(input_path)
    compressed_path = huffman.compress()
    decompressed_path = huffman.decompress(compressed_path)

    # Get filenames for display
    compressed_file = os.path.basename(compressed_path)
    decompressed_file = os.path.basename(decompressed_path)

    return render_template(
        "result.html",
        compressed_file=compressed_file,
        decompressed_file=decompressed_file,
    )


@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Ensure the file exists in the UPLOAD_FOLDER
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)
    return "File not found.", 404


if __name__ == "__main__":
   app.run(debug=True)