#!/usr/bin/env python3

import cv2
import os
from threading import Thread, Lock
import time
import random
from threading import Condition
import threading

# globals
outputDir    = 'frames'

#queue = []
lock = Lock()
MAX_NUM = 10 #requirement completed: is being halved to 10
condition = Condition()

class GrayscaleProducerThread(Thread):
    def run(self):
        #global queue
        condition.acquire()
        # initialize frame count
        count = 0

        # get the next frame file name
        inFileName = "{}/frame_{:04d}.jpg".format(outputDir, count)

        # load the next file
        inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

        while inputFrame is not None:
            # if len(queue) == MAX_NUM:
            #         print ("Queue full, producer is waiting")
            #         condition.wait()
            #         queue = []
            #         print ("Space in queue, Consumer notified the producer")

            print("Converting frame {}".format(count))

            # convert the image to grayscale
            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
            
            # generate output file name
            outFileName = "{}/grayscale_{:04d}.jpg".format(outputDir, count)

            # write output file
            cv2.imwrite(outFileName, grayscaleFrame)

            #queue.append(count)
            count += 1

            # generate input file name for the next frame
            inFileName = "{}/frame_{:04d}.jpg".format(outputDir, count)

            # load the next frame
            inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

# class GrayscaleConsumerThread(Thread):
#     def run(self):
#         global queue
#         while True:
#             condition.acquire()
#             if not queue:
#                 print ("Nothing in queue, consumer is waiting")
#                 condition.wait()
#                 print ("Producer added something to queue and notified the consumer")
#             queue.pop(0)
#             condition.notify()
#             condition.release()
#             time.sleep(random.random())
