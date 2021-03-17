'''
Given an input image,
return crop
'''

import cv2
import numpy as np

#These coordinates are delivered by the Optical Flow Tracker
min_x = 130
min_y = 600
max_x = 350
max_y = 660

frame = cv2.imread("frame.jpg")

cropped = frame[min_y:max_y,min_x:max_x]
#while True:
#    cv2.imshow("cropped",cropped)
cv2.imwrite("cropped.jpg",cropped)
