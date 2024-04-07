import cv2
import easyocr
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Initialize EasyOCR Reader
reader = easyocr.Reader(['en'], gpu=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Convert uploaded file to image
            img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
            # Detect text on the image
            text_ = reader.readtext(img)
            # Process text detection results and return the appropriate response
            return render_template('result.html', text=text_)
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)
