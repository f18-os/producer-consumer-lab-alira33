#!/usr/bin/env python3

import cv2
import time
from threading import Condition

# globals
outputDir    = 'frames'
frameDelay   = 42       # the answer to everything
condition = Condition()

def display(self, frame, count):
    
    # Condition aquired
    condition.acquire()
    startTime = time.time()

    # # Generate the filename for the first frame 
    frameFileName = "{}/grayscale_{:04d}.jpg".format(outputDir, count)

    # # load the frame
    frame = cv2.imread(frameFileName)
    
    print("Displaying frame {}".format(count))
    # Display the frame in a window called "Video"
    cv2.imshow("Video", frame)

    # compute the amount of time that has elapsed
    # while the frame was processed
    elapsedTime = int((time.time() - startTime) * 1000)
    print("Time to process frame {} ms".format(elapsedTime))
        
        # determine the amount of time to wait, also
        # make sure we don't go into negative time
    timeToWait = max(1, frameDelay - elapsedTime)

        # Wait for 42 ms and check if the user wants to quit
    cv2.waitKey(timeToWait)   

        # # get the start time for processing the next frame
    startTime = time.time()
        
        # # get the next frame filename
    frameFileName = "{}/grayscale_{:04d}.jpg".format(outputDir, count)

        # # Read the next frame file
    frame = cv2.imread(frameFileName)

