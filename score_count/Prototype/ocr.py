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
#Check where does get_
whitelist = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

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
    ocr_data['text'] = [re.sub(r'[^{}]+'.format(whitelist), '', text) if whitelist is not None else text
                        for text in ocr_data['text']]
    return ocr_data
