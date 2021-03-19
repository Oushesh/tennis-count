'''
Optical Flow is meant to find the
stationary regions
https://learnopencv.com/optical-flow-in-opencv/
https://developer.nvidia.com/blog/opencv-optical-flow-algorithms-with-nvidia-turing-gpus/

'''
import cv2
import numpy as np

#Python Lucas Kanade
def lucas_kanade_method(video_path):
    # Read the video
    cap = cv2.VideoCapture(video_path)

    # Parameters for ShiTomasi corner detection
    feature_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=15)

    # Parameters for Lucas Kanade optical flow
    lk_params = dict(winSize=(50, 50),maxLevel=2,criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
    )

    # Create random colors
    color = np.random.randint(0, 255, (100, 3))

    # Take first frame and find corners in it
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    # Create a mask image for drawing purposes
    mask = np.zeros_like(old_frame)

    count = 0
    while True:
        # Read new frame
        ret, frame = cap.read()

        if not ret:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate Optical Flow
        '''
        p1: nextPts
        status: 0: if no flow.
                1: if there is flow.
        err: error
        '''
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        max_x = int(max([point[0][0] for point in p1]))
        max_y = int(max([point[0][1] for point in p1]))
        min_x = int(min([point[0][0] for point in p1]))
        min_y = int(min([point[0][1] for point in p1]))
        #print (min_x,min_y,max_x,max_y)

        #Crop the region of interest here:
        #TODO: use the scientific theorem provided by the paper:
        #https://arxiv.org/pdf/1801.01430.pdf
        #Decide on how to put the threshold
        #
        #cv2.imwrite("cropped" + str(count) + ".jpg",frame[min_y-20:max_y+20,min_x-20:max_y+20])
        count+=1

        # Select good points
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        # Draw the tracks
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

        # Display the demo
        img = cv2.add(frame, mask)
        cv2.imshow("frame", img)
        #cv2.imwrite("frame"+ str(count)+".jpg",frame)
        k = cv2.waitKey(25) & 0xFF
        if k == 27:
            break

        # Update the previous frame and previous points
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

#Extension of Lukas Kanade Method:
#1. Playing with the block size of: 50,50 approximately the width height
#2. We can also add the credential from the Indian student paper --> modify it from here
#3. See how to get the coordinates where Lucas Kanade has motion: -->
#4. reduce the ROI for the EAST: detector

if __name__ == "__main__":
    video_path = "video/RogerFedererDoha2021.mp4"
    #video_path = "video/TheBestGameEver_MurrayvFederer_cut001.mp4"
    lucas_kanade_method(video_path)

'''
python lucas_kanade.py
'''
