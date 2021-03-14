## tennis-count
    Counting scores of tennis balls

      1. Counting tennis balls from input: videos of tennis matches.
      2. Output: Each player score
      3. Steps and literature
         https://gml16.github.io/projects/Report_LV8_Project.pdf
      4. Action Recognition: https://medium.com/bakken-b%C3%A6ck/improving-your-tennis-game-with-computer-vision-863969743024
      5. Get tennis court from videos
      6. Track ball from tennis videos
      7. Track hit action --> Track ball trajectory --> Track bounce (position of bounce)
            --> get the position of the ball inside the court.
      8. Track Tennis Ball: https://nol.cs.nctu.edu.tw:234/open-source/TrackNet/
      9. Official TrackNet V2: https://nol.cs.nctu.edu.tw:234/open-source/TrackNetv2
      10. TrackNet: https://nol.cs.nctu.edu.tw/ndo3je6av9/
      11. https://medium.com/bakken-b%C3%A6ck/improving-your-tennis-game-with-computer-vision-863969743024 for Tracking OpenPose
      12. Positions of players around the net: https://github.com/sethah/deeptennis
      13. The stuffs here: https://towardsdatascience.com/ball-detection-with-computer-vision-ai-in-sports-f9ef743e0ef1
      14. This one is really awesome: https://github.com/vishaltiwari/bmvc-tennis-analytics
      15. https://github.com/vishaltiwari/bmvc-tennis-analytics


#### How did I setup the problem?
     * https://medium.com/deep-learning-turkey/google-colab-free-gpu-tutorial-e113627b9f5d
     * Game: 

#### Milestones
     * Track Balls on Tennis Videos --> (x,y, frame) pos of moving ball in each frame.
     * Improved detection using Focal Lens and ResNet extension of TrackNet.
     * Next: build a classical filter to optimise the trajectory prediction.
     * How can I reduce the time complexity of detection?
       * Instead of running inference on each frame: propagate the dec
       ** TODO: Handle the case where we dont see the players: 
       ** DONE: Run the detector for court detection then eliminate the wrong frames.
       ** TODO: Steps to perform bounce. (Test this here: )
       ** DONE: Tennis Court detection: https://github.com/gchlebus/tennis-court-detection
       ** Test algorithm to determine bounce from 2D Coordinates.
       ** 
#### Report:
     * https://leimao.github.io/blog/Focal-Loss-Explained/
     * Think what to write in the report --> Mention advantage Focal Loss,  ResNet and RetinaNet.
     * Mention why Tracking steps more      
