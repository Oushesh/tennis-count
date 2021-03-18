### Papers and Approach:
    * https://arxiv.org/pdf/1801.01430.pdf
    *
    * Temporarily segmenting out the rallies. (DONE)
    * Scorecard & Score Extraction (OCR Problem)
    * OCR used: Google Tesseract (pytesseract)
    *

### Installation Guideline
    * tesseract installation properly:
      * https://medium.com/@ahmedbr/how-to-implement-pytesseract-properly-d6e2c2bc6dda
### Current Pipeline:
    1) Deep Learning Based
        * Pass in TextFuseNet:
    2) OpenCV OCR + Tesseract Engine: https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/

    * Pypi: https://github.com/madmaze/pytesseract
    * https://pypi.org/project/pytextractor/33

    * Wild-OCR: https://github.com/oezguensi/wild-OCR
    * Rally Segmentation: Court detection (DONE already)
    * Tennis Video --> Court (Yes or No)
    * Scoreboard Extraction: Optical Flow Constant Objects
    * TODO: Read: https://cdn.iiit.ac.in/cdn/cvit.iiit.ac.in/images/Thesis/MS/Anurag_Ghosh/Anurag_MS_Thesis.pdf
    * Optical Flow: https://developer.nvidia.com/blog/opencv-optical-flow-algorithms-with-nvidia-turing-gpus/
    * Tested Lucas Kanade Flow method.
    * Now testing the other pyramid approaches.
    *
    * Mention optimisation with Nvidia Cuda implementation: https://developer.nvidia.com/blog/opencv-optical-flow-algorithms-with-nvidia-turing-gpus/


### Optimisation and Inference:
    * How to make the current stuffs better?
      * Optical Flow Part:
        Referred from Nvidia Claim: https://developer.nvidia.com/opticalflow-sdk
          * Up to 150 fps at 4K resolution.
          * at 1/4 pixel resolution. (150*4)x Improvement Factor.

    * Improvement on the Digit & Character Recognition Part --> separate the run for digit and character part.
      We can use data mining to detect  the true names from a dictionary
    * Even if we don't have perfect scoreboard detection, the list of
      players in Tennis is finite. So build a dictionary and search if the
      detected player game is inside the dictionary. (Sanity Check)
