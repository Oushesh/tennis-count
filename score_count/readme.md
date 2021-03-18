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
## Current Pipeline:
   * Deep Learning Based
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

## Optimisation and Inference:
  * How to make the current stuffs better?
      * Optical Flow Part:
        Referred from Nvidia Claim: https://developer.nvidia.com/opticalflow-sdk
          * Up to 150 fps at 4K resolution.
          * at 1/4 pixel resolution. (150*4)x Improvement Factor.

      * Implementation of Lukas Kanade (The idea behind it.)
        * Video Screenshot:
          ![](Documentation/lucas_kanade.jpg)
      * Motion Flow estimation

    * Digit & Character Recognition Part
      * CURRENT:
        * The player name is finite. So it is possible to build a dictionary
          to further refine results. This allows to eliminate errors from the
          Tesseract V4. LSTM based Google OCR Engine.
      * IMPROVEMENT:
        * Given that the Tesseract Engine is LSTM based and has been trained onto
          thousands of texts with different handwriting, fonts, lighting conditions(contrast) and so on. It captures a lot of variance which are
          not needed here: for instance: handwriting, contrast and lighting.
          Instead one can custom train the Tesseract engine for this particular use-case
        * Other options:
          * Google Cloud Vision API
          * Microsoft Computer Vision API
          * miscellaneous cloud providers.
      * Separate the run for digit and character part.
      We can use data mining to detect  the true names from a dictionary
    * Even if we don't have perfect scoreboard detection, the list of
      players in Tennis is finite. So build a dictionary and search if the
      detected player game is inside the dictionary. (Sanity Check)

## My Development Philosophy:
   * Fast Code write-up always done on: https://replit.com/~?onboarding=1
   * Ubuntu 18.04, Atom, Sublime Text,
   * Github, possibly for production Docker, Github integrated workflows CI/CD
   * Hoping github releases Codespace soon.
## TODOs
   * Add the pictures of the test and run command next to each bulltet point.
