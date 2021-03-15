import cv2
from court_detector import detector

cap = cv2.VideoCapture("../videos/RogerFedererDoha2021.mp4")
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    #cv2.imwrite("frame%d.jpg" % count, frame)
    out_img = detector(frame)
    cv2.imwrite("output"+str(count)+".jpg",out_img)
    #print ("out_img",out_img)
    #Call the detector here:

    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() # destroy all opened windowss

#Run detector on each frame
#package as function and put onto multiprocessing.
