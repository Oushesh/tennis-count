'''
OCR: based on pytesseract Google V4 engine
'''

#Ref: https://github.com/oezguensi/wild-OCR/blob/master/pipeline.ipynb
#https://github.com/diewland/text-detection-opencv-east, EAST text detector

#TODO: Refactor EAST code, we tested above.
#We perform OCR testing here then:
#Write OCR pipeline from the detector here:

#Load the image here.
#Detect then pass for OCR detection

import numpy as np
import cv2
import pytesseract
import re
import sys

from PIL import Image
from collections import defaultdict

###This is an adaptation function

'''
Referring to EAST github detector:
The EAST detector would output the detections:

'''
def detections2crops(img,detect_list_path):
    #Read file then write the croppeed
    #detected objects onto disk
    f = open(detect_list_path,"r")
    count=0
    for detection in f:
        print (detection)
        #here we have the 4 corner-coordinates x1,y1,x2,y2,x3,y3,x4,y4
        cv2.imwrite("detection" + str(count)+".jpg",img[min_y-20:max_y+20,min_x-20:max_y+20])
        cv2.
        count +=1

    return None

detect_list_path = "../EAST/model/eval/frame31.txt"
detections2crops(img,detect_list_path)

def img2detections(img,detections):
    idx = 0
    for detection in detections:
        #We get the detected coorindates here:

        idx+=1
    return

def get_ocr_data(img, psm=6, oem=1, whitelist=None):
    '''
    Reads the text.
    :param img: An image containing text.
    :param psm: The "page segmentation method". If set to 6 we assume a single uniform block of text.
        More information at https://github.com/tesseract-ocr/tesseract/wiki/ImproveQuality
    :param oem: The engine to use. 1 sets the engine to use the LSTM.
    :param whitelist: Characters to allow in the result.
    :return: Data containing information about the text, confidence and more.
    '''
    ocr_data = pytesseract.image_to_data(Image.fromarray(img),output_type='dict',config='--psm {} --oem {} -c load_system_dawg=0 load_freq_dawg=0'.format(psm, oem))
    # as whitelist doesn't work for LSTM engine
    ocr_data['text'] = [re.sub(r'[^{}]+'.format(whitelist), '', text) if whitelist is not None else text                        for text in ocr_data['text']]
    return ocr_data

#Complete the ocr implementation here:
#Refactor the code, then perform improvement with different classification algorithms

if __name__ == "__main__":
    #groundtruth = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    img = "cropped20.jpg"
    img = "frame31.jpg"
    image = cv2.imread(img)
    #print (image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #call pytesseract engine
    text  = pytesseract.image_to_string(gray,lang='eng')
    print ("The recognised text is:",text)

#How to properly install tesseract here:
#https://medium.com/@ahmedbr/how-to-implement-pytesseract-properly-d6e2c2bc6dda

#needed is a function from image to decoupled crops for each detection
