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
        values = detection.split(',')
        #print (values)
        #here we have the 4 corner-coordinates x1,y1,x2,y2,x3,y3,x4,y4
        min_x = min([int(a) for a in [values[0],values[2],values[4],values[6]]])
        #print (min_x)
        min_y = min([int(a) for a in [values[1],values[3],values[5],values[7]]])
        #print (min_y)
        max_x = max([int(a) for a in [values[0],values[2],values[4],values[6]]])
        #print (max_x)
        max_y = max([int(a) for a in [values[1],values[3],values[5],values[7]]])
        #print (max_y)
        #Perform test-check that detector
        print ("image_shape",img.shape)
        print (min_x,min_y,max_x,max_y)
        assert(min_y>0 and min_y <img.shape[0])
        assert(max_y>0 and max_y <img.shape[0])
        assert(min_x>0 and min_x <img.shape[1])
        assert(max_x>0 and max_x <img.shape[1])

        cv2.imwrite("detection" + str(count)+".jpg",img[min_y:max_y,min_x:max_x])
        count +=1
    return None

detect_list_path = "../EAST/model/eval/frame31.txt"
img = cv2.imread("../EAST/examples/frame31.jpg")
print (img)
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

#Use a pretty simple regex function to
#extract all numbers from input string
#def digit():
#Fine tuning OCR tesseract

if __name__ == "__main__":
    groundtruth = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    img = "cropped20.jpg"
    img = "char_digit.jpg"
    image = cv2.imread(img)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #otsu_img, thresh = cv2.threshold(image, 100, 255, cv2.THRESH_OTSU)
    #cv2.imwrite(otsu_img,"otsu_img.jpg")

    #call pytesseract engine
    text  = pytesseract.image_to_string(gray,lang='eng')
    #print (get_ocr_data(gray, psm=6, oem=1,whitelist=groundtruth))
    #psm = page segmentation methods
    ocr_result = pytesseract.image_to_string(image, lang='eng',config='--psm 6 --oem 1 -c tessedit_char_whitelist=0123456789')
    print ('The trial result is:',ocr_result)
    print ("The recognised text is:",text)

#TODO: complete the 1 pipeline and results first: then we work on the improvement

    #Getting Boxes around .txt for adaptive binarisation strategies.
    boxes = pytesseract.image_to_boxes(gray)
    h,w,_ = image.shape
    for b in boxes.splitlines():
        b = b.split(' ')
        boxed = cv2.rectangle(image, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
        #write those images onto the
    cv2.imshow('boxed',boxed)
    cv2.imwrite("boxed_char_digit.jpg",boxed)

    #Pytesseract to subboexes --> then perform ocr on it. again
    #https://nanonets.com/blog/ocr-with-tesseract/
