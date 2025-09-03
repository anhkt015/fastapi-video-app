from PIL import Image
import pytesseract
import cv2
import numpy as np

def ocr_image(path):
    img = Image.open(path)
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    return  pytesseract.image_to_string(img, lang='vie') 


