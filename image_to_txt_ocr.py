# -*- coding: utf-8 -*-
"""
load image and return text (OCR)
@author: avinash gaikwad
"""
from flask import *  
from PIL import Image
import pytesseract

app = Flask(__name__)  

@app.route('/')  
def upload():  
    return render_template("upload_image_file.html")  

def encoder_image():
    ##############################encoder and decoder image############
    import base64

    with open('slider2.jpg', 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

        print(base64_message)
        
    base64_img_bytes = base64_message.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

@app.route('/success2', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        im = Image.open(f)
        text = pytesseract.image_to_string(im, lang = 'eng')
        #print(text1,f)
        f.save(f.filename)  
        #return render_template("upload_sucess.html", name = f.filename)  
        return render_template("upload_sucess.html", name = text)
    
#api upload image from postman and get response
@app.route('/ap_image', methods = ['POST'])  
def sucess():  
    if request.method == 'POST':  
        f = request.files['file']
        im = Image.open(f)
        text = pytesseract.image_to_string(im, lang = 'eng')
        return text
  
if __name__ == '__main__':  
    app.run(host="0.0.0.0",port=9595)  
