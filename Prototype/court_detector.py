import numpy as np
import argparse
import cv2
import scipy.ndimage as ndi

#Clone the git of poly_point_isect and put it here:
#https://github.com/ideasman42/isect_segments-bentley_ottmann
import sys

sys.path.insert(1,"isect_segments-bentley_ottmann")
import  poly_point_isect as bot

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image",default="tennis.jpg")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
boundaries = [([180, 180, 100], [255, 255, 255])]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    #cv2.imshow("images", np.hstack([image, output]))
    #cv2.waitKey(0)

gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)

kernel_size = 5
blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)

low_threshold = 10
high_threshold = 200
edges = cv2.Canny(gray, low_threshold, high_threshold)
dilated = cv2.dilate(edges, np.ones((2,2), dtype=np.uint8))

#cv2.imshow('dilated.png', dilated)
#cv2.waitKey(0)

rho = 1  # distance resolution in pixels of the Hough grid
theta = np.pi / 180  # angular resolution in radians of the Hough grid
threshold = 10 # minimum number of votes (intersections in Hough grid cell)
min_line_length = 40  # minimum number of pixels making up a line
max_line_gap = 5  # maximum gap in pixels between connectable line segments
line_image = np.copy(output) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
# Output "lines" is an array containing endpoints of detected line segments

lines = cv2.HoughLinesP(dilated, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

points = []
for line in lines:
    for x1, y1, x2, y2 in line:
        points.append(((x1 + 0.0, y1 + 0.0), (x2 + 0.0, y2 + 0.0)))
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

cv2.imshow('houghlines.png', line_image)
#cv2.waitKey(0)
cv2.imwrite('houghlines.jpg',line_image)


lines_edges = cv2.addWeighted(output, 0.8, line_image, 1, 0)
print(lines_edges.shape)

intersections = bot.isect_segments(points)
print(intersections)

for idx, inter in enumerate(intersections):
    a, b = inter
    match = 0
    for other_inter in intersections[idx:]:
        c, d = other_inter
        if abs(c-a) < 8 and abs(d-b) < 8:
            match = 1
            if other_inter in intersections:
                intersections.remove(other_inter)
                intersections[idx] = ((c+a)/2, (d+b)/2)

    if match == 0:
        intersections.remove(inter)

for inter in intersections:
    a, b = inter
    for i in range(6):
        for j in range(6):
            lines_edges[int(b) + i, int(a) + j] = [0, 0, 255]

# Show the result
cv2.imshow('line_intersections3.png', lines_edges)
cv2.imwrite('line_intersections3.png', lines_edges)
#cv2.waitKey(0)
