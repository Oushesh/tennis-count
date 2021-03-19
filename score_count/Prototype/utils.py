'''
This script contains miscellaenous helper functions
'''

#The player name is finite. So it is possible to build a dictionary
#Build a web scraper with beautiful soup or so on to get a database
#of the names from official source here: https://www.atptour.com/en/rankings/singles
#groundtruth = {'Federer','Nadal','Basilashvili'}

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
