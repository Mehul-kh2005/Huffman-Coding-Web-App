# Huffman Coding Flask Web Application

This is a simple web application that allows you to upload a file, compress it using the Huffman coding algorithm, and then download both the compressed and decompressed versions of the file. The application is built using **Flask** for the backend and implements **Huffman coding** for file compression.

## Features
- **File Upload**: Upload a text file to be processed.
- **Huffman Compression**: Compress the uploaded file using the Huffman coding algorithm.
- **Decompression (Optional)**: Reconstruct the original file from the compressed data for verification.
- **File Download**: Download the compressed file and, if decompressed, the reconstructed file.

## Requirements
- Python 3.x
- Flask
- Other Python libraries used in the project (like `os`, `heapq`)

## Installation

### Clone the Repository
To get started, clone this repository to your local machine:

```bash
git clone https://github.com/Mehul-kh2005/Huffman-Coding-Web-App
cd huffman-coding-flask
```

### Install Dependencies
You will need to install the required Python packages. You can do this by creating a virtual environment and installing the dependencies.

#### Create a virtual environment:

```bash
python3 -m venv venv
```

#### Activate the virtual environment:

- On Windows:
    ```bash
    venv\Scripts\activate
    ```
- On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

#### Install required libraries:

```bash
pip install flask
``` 

Alternatively, if you have a `requirements.txt` file, you can install the dependencies with:

```bash 
pip install -r requirements.txt
```

## Run the Application
To run the application locally, use the following command:

```bash
python3 app.py
```

This will start a local server, typically at `http://127.0.0.1:5000/`. If port `5000` is unavailable, Flask may use a different port (e.g., `5001`, `5002`, etc.). Check your terminal for the exact URL to access the application.

## How It Works
1. **Upload a File:** Select a file to upload for compression.
2. **Compression:** The uploaded file is compressed using Huffman coding.
3. **Download Files:** Once the file is compressed and decompressed, you can download both the compressed and decompressed versions.

## File Structure

```bash
huffman-coding-flask/
├── app.py            # Main Flask application code
├── huffman.py        # Contains Huffman coding logic
├── uploads/          # Directory where uploaded and processed files are stored
├── templates/
│   ├── index.html    # Home page HTML template
│   └── result.html   # Page to show compressed and decompressed files
├── static/
│   └── style.css     # Styling for the web pages
├── .gitignore        # Git ignore file
└── requirements.txt  # List of dependencies (if applicable)
```

## Author
### Mehul Khandelwal – [GitHub Profile](https://github.com/Mehul-kh2005/)

## License
This project is the intellectual property of **Mehul Khandelwal**.

**Allowed:**
You are permitted to use this project by following the steps mentioned in this README file.

**Restricted:**
You are not allowed to modify, copy, distribute, or use this project in any way beyond what is explicitly mentioned without prior permission from the author.