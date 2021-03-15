'''
Module:
1)load in video & detect tennis-court in frames.
2) remove frames which do not contain court.
'''
import cv2 as cv
import time
import subprocess as sp
import multiprocessing as mp
from os import remove
import court_detector
from court_detector import detector

def combine_output_files(num_processes):
    # Create a list of output files and store the file names in a txt file
    list_of_output_files = ["output_{}.mp4".format(i) for i in range(num_processes)]
    with open("list_of_output_files.txt", "w") as f:
        for t in list_of_output_files:
            f.write("file {} \n".format(t))

    # use ffmpeg to combine the video output files
    ffmpeg_cmd = "ffmpeg -y -loglevel error -f concat -safe 0 -i list_of_output_files.txt -vcodec copy " + output_file_name
    sp.Popen(ffmpeg_cmd, shell=True).wait()

    '''
    # Remove the temperory output files
    for f in list_of_output_files:
        remove(f)
    remove("list_of_output_files.txt")
    '''
def process_video_multiprocessing(group_number):
    # Read video file
    cap = cv.VideoCapture(video_path)
    # get height, width and frame count of the video
    width, height = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    frame_count  = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

    num_processes = mp.cpu_count()
    #print("Number of CPU: " + str(num_processes))
    frame_jump_unit = frame_count // num_processes
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_jump_unit*group_number)

    fps = int(cap.get(cv.CAP_PROP_FPS))
    proc_frames = 0

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv.VideoWriter()
    output_file_name = "output_multi.mp4"
    print ("output_file_name")
    out.open("output_{}.mp4".format(group_number), fourcc, fps, (width, height), True)
    try:
        while proc_frames < frame_jump_unit:
            ret, frame = cap.read()
            if not ret:
                break

            im = frame
            #Perorm Tennis court detection on each frame
            #TODO: call the court detector here.
            out = detector(im)
            print ("calling detector")
            print ("out",out)
            cv2.imwrite("outptut.jpg",out)
            proc_frames += 1
    except:
        # Release resources
        cap.release()
        out.release()

    # Release resources
    cap.release()
    out.release()

def multi_process():
    print("Video processing using {} processes...".format(num_processes))
    start_time = time.time()

    # Parallelise the execution of a function across multiple input values
    p = mp.Pool(num_processes)
    p.map(process_video_multiprocessing, range(num_processes))

    #combine_output_files(num_processes)
    end_time = time.time()
    total_processing_time = end_time - start_time
    print("Time taken: {}".format(total_processing_time))

if __name__ == "__main__":
    video_path = "..input/RogerFedererDoha2021.mp4"

    output_file_name = "output"+video_path.split('/')[-1]
    num_processes = mp.cpu_count()
    print("Number of CPU: " + str(num_processes))
    multi_process()

#Reference: https://www.xailient.com/post/multiprocessing-video-in-python
