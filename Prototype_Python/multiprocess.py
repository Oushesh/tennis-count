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

def process_video_multiprocessing(group_number):
    # Read video file
    cap = cv.VideoCapture(file_name)
    cap.set(cv.CAP_PROP_POS_FRAMES, frame_jump_unit * group_number)

    # get height, width and frame count of the video
    width, height = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
    no_of_frames = int(cap.get(cv.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv.CAP_PROP_FPS))
    proc_frames = 0

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv.VideoWriter()
    output_file_name = "output_multi.mp4"
    out.open("output_{}.mp4".format(group_number), fourcc, fps, (width, height), True)
    try:
        while proc_frames < frame_jump_unit:
            ret, frame = cap.read()
            if not ret:
                break

            im = frame
            #Perorm Tennis court detection on each frame
            #TODO: 
            _, bboxes = detectum.process_frame(im, THRESHOLD)

            # Loop through list (if empty this will be skipped) and overlay green bboxes
            for i in bboxes:
                cv.rectangle(im, (i[0], i[1]), (i[2], i[3]), (0, 255, 0), 3)

            # write the frame
            out.write(im)

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

    # Paralle the execution of a function across multiple input values
    p = mp.Pool(num_processes)
    p.map(process_video_multiprocessing, range(num_processes))

    combine_output_files(num_processes)
    end_time = time.time()
    total_processing_time = end_time - start_time
    print("Time taken: {}".format(total_processing_time))
    print("FPS : {}".format(frame_count/total_processing_time))

if __name__ == "__main__":
    video_path = "videos/RogerFedererDoha2021.mp4"
    output_file_name = output + "/" + video_path
    width, height, frame = get_video_frame_details(video_path)
    print("Video frame count = {}".format(frame_count))
    print("Width = {}, Height = {}".format(width, height))
    num_processes = mp.cpu_count()
    print("Number of CPU: " + str(num_processes))
    frame_jump_unit =  frame_count// num_processes
    multi_process()
