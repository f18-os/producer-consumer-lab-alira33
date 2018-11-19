#!/usr/bin/env python3

import cv2
from threading import Condition

# globals
outputDir = 'frames'
condition = Condition()

def GrayscaleThread(self, frame, count):

        # Condition aquired
        condition.acquire()

        while frame is not None:
            print("Converting frame {}".format(count))

            # convert the image to grayscale
            grayscaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
            # generate output file name
            outFileName = "{}/grayscale_{:04d}.jpg".format(outputDir, count)

            # write output file
            cv2.imwrite(outFileName, grayscaleFrame)

            return frame
      

    
    
