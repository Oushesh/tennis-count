'''
Dense_Optical_Flow:
TOBE fully implemented.
Dense Lucas Kanade gives better features and more accurate segmentation
mask
'''
import cv2
import numpy as np

def dense_optical_flow(method, video_path, params=[], to_gray=False):
        Feature_vector = None
        return Feature_vector

if __name__ == "__main__":
    video_path = "video/RogerFedererDoha2021.mp4"
    method = cv2.optflow.calcOpticalFlowSparseToDense
    save=True
    dense_optical_flow(method,video_path,save,to_gray=True)

#python dense_lucas_kanade.py
#https://stackoverflow.com/questions/44633378/attributeerror-module-cv2-cv2-has-no-attribute-createlbphfacerecognizer
