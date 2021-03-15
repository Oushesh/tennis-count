import cv2
from threading import Thread


class VideoStream:
    def __init__(self,video_path,name="VideoStream"):
        self.stream = cv2.VideoCapture(video_path)
        (self.grabbed,self.frame) = self.stream.read()

        #initialize the thread name
        self.name = name
        #initialize the variable used to indicate if the
        #thread should be stopped.
        self.stopped = False

    def start(self):
        #start the thread to read frames from the video stream
        t = Thread(target=self.update, name=self.name,args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        #keep looping until the thread is stopped
        while True:
            #if the thread indicator vaiable is set, stop the thread
            if self.stopped:
                return
            #otherwise, read the next frame from stream
            (self.grabbed,self.frame) = self.stream.read()


if __name__ == "__main__":
    video_path = "../input/videos/RogerFedererDoha2021.mp4"
    current_stream = VideoStream(video_path)
    current_stream.start()
    current_stream.update()
    
