### Ball Tracking.py --> Classical Computer Vision to track the ball

### Second is one tried on Google Colab -->
    https://colab.research.google.com/drive/1B7kBie3OCkaUO4RjA6yTztP1L2E5C_Ew#scrollTo=JPW_kiJsTIGl

    # Command line code:
      # !git clone https://nol.cs.nctu.edu.tw:234/open-source/TrackNet.git
      # !dir
      # !pip install  -r TrackNet/requirements.txt
      # Change folder directory to 3 and 3F (renaming)
      # !python TrackNet/3/3F/predict_video.py --save_weights_path=TrackNet/3/3F/weights/model.3 --input_video_path=TrackNet/test.mp4 --output_video_path=TrackNet/test_detection.mp4 --n_classes=256

      # Download the file back to test_detection
      # Download the original input file as well.
      # Need to use tensorflow GPU: otherwise bug with tensorflow.keras backend.
      # No current fix

### Third is test the code onto:
    # https://github.com/Chang-Chia-Chi/TrackNet-Badminton-Tracking-tensorflow2
    # Test: python predict.py

### Fourth is to test this one and rewrite it here:
    # Tennis Ball Tracking: https://researchweb.iiit.ac.in/~vishal.tiwari/ball_tracking_BTV.html
      # F Yan Data Association Algorithm --> Ball Candidate extraction & tracklet generation
      #
      # Maybe I can use this algorithm to track my hands for the hand interface for my prototype.
      # The hand tracker here.

### Target Today: TODO: https://github.com/Chang-Chia-Chi/TrackNet-Badminton-Tracking-tensorflow2
    Test this and run on Google Research Collab. (TODO:tonight)
    Then test the other stuffs. Then perform multi-object tracking.
###
