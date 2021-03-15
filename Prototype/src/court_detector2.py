import numpy as np
import cv2
import scipy.ndimage as ndi

#path = "../input/tennis.jpg"
path = "../input/output9.jpg"
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
smooth = ndi.filters.median_filter(gray, size=2)
edges = smooth > 180
lines = cv2.HoughLines(edges.astype(np.uint8), 0.5, np.pi/180, 120)
#Perform clustering here:

##Do this for all lines.
points = []
for line in lines:
    for rho,theta in line:
        #k means of rho, theta
        #print(rho, theta)



        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        points.append([x1,y1])
        points.append([x2,y2])

        #cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
# Show the result
#print (points)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

from scipy.cluster.vq import vq, kmeans, whiten

whitened = whiten(points)

book = np.array((whitened[0],whitened[2]))

kmeans(whitened,book)
print (len(kmeans))

cv2.imshow("Line Detection", img)
cv2.imwrite("linedetection10.jpg",img)

#Find k means of the point, then eliminate them
#Tom Titcombe.

#We have all lines
#Define model: like upper left, upper right, lower
