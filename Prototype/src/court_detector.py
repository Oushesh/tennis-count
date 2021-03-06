import numpy as np
import cv2

# construct the argument parse and parse the arguments
# load the image
import sys
sys.path.insert(1,"opencv_wrapper")
import opencv_wrapper as cvw

'''
image = cv2.imread("input/tennis.jpg")
print (image)
'''

def detector(image):
    # define the list of boundaries
    boundaries = [([180, 180, 100], [255, 255, 255])]
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)

    # Start my code
    gray = cvw.bgr2gray(output)
    corners = cv2.cornerHarris(gray, 9, 3, 0.01)
    corners = cvw.normalize(corners).astype(np.uint8)

    thresh = cvw.threshold_otsu(corners)
    dilated = cvw.dilate(thresh, 3)
    contours = cvw.find_external_contours(dilated)

    #TODO: Can be combined together in 1 loop
    for contour in contours:
        cvw.circle(image, contour.center, 3, cvw.Color.RED, -1)
        #Draw lines using openCV
    #Build a list of contour.center

    '''
    pts = [(int(contour.center.x),int(contour.center.y)) for contour in contours]
    #print (pts)
    #TODO: selection of points needed.

    for i in range(len(pts)-1):
        cv2.line(image,pts[i],pts[i+1],(255,0,0),2)
        cv2.imshow("Image",image)
    '''
    return image

    #Draw the lines here given the points in OpenCV2.
#print (cv2.imread("../input/tennis.jpg"))
#detector(cv2.imread("../input/tennis.jpg"))

#TODO: import tennis video & run the code with multiprocessing to get
#tennis count for the output.
