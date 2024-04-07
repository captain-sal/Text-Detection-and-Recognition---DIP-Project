# Text-Detection-and-Recognition : Digital Image Processing Project
# Text Recognition with Flask and EasyOCR

This Flask application detects text in uploaded images using the EasyOCR library and displays the results on a web interface.

## Installation

1. Clone the repository:
https://github.com/captain-sal/Text-Detection-and-Recognition---DIP-Project


2. Navigate to the project directory:
cd text-recognition-flask


3. Install the required Python packages:
pip install easyocr Flask opencv-python-headless numpy


4. Run the Flask application:
python app.py


## Usage

1. Open a web browser and go to `http://localhost:5000`.
2. Click on the "Choose File" button to select an image file containing text.
3. Click the "Upload" button to upload the image.
4. The application will process the image, detect text using EasyOCR, and display the results on the web page.


## Dependencies

- Flask: A micro web framework for Python.
- EasyOCR: An optical character recognition (OCR) library that uses deep learning to recognize text in images.
- OpenCV: An open-source computer vision and machine learning software library.
- NumPy: A library for numerical computing in Python.

