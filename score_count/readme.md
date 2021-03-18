### Papers and Approach:
    * https://arxiv.org/pdf/1801.01430.pdf
    *
    * Temporarily segmenting out the rallies. (DONE)
    * Scorecard & Score Extraction (OCR Problem)
    * OCR used: Google Tesseract (pytesseract)
    *

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
      Referred from Nvidia Claim: https://developer.nvidia.com/opticalflow-sdk
        * Up to 150 fps at 4K resolution.
        * at 1/4 pixel resolution. (150*4)x Imrovement Factor.
