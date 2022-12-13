from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from PIL import Image
import pytesseract
import requests
import cv2



pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

app.config['SECRET_KEY'] = "Your_secret_string"


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/translated', methods=['GET', 'POST'])
def translated():
    if request.method=="POST":
        path_to_image = 'stop_.jpg'
#Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = path_to_tesseract
#Open image with PIL
        img = Image.open(path_to_image)
#Extract text from image
        text = pytesseract.image_to_string(img)
        print(text)

    return render_template('translated.html',img=img)


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(  # Starts the site
        debug=True
    )
