#!/usr/bin/env python3

import cv2
import os
from threading import Thread, Lock
import time
import random
from threading import Condition
import threading

queue = []
# globals
outputDir    = 'frames'
clipFileName = 'clip.mp4'
# initialize frame count

lock = Lock()
MAX_NUM = 10 #requirement completed
condition = Condition()

class ExtractProducerThread(Thread):
  def run(self):
      #global queue
      count = 0

      # Condition aquired
      condition.acquire()
      
      # open the video clip
      vidcap = cv2.VideoCapture(clipFileName)

      # create the output directory if it doesn't exist
      if not os.path.exists(outputDir):
        print("Output directory {} didn't exist, creating".format(outputDir))
        os.makedirs(outputDir)

      # read one frame
      success,image = vidcap.read()

      print("Reading frame {} {} ".format(count, success))
      while success:
        cv2.imwrite("{}/frame_{:04d}.jpg".format(outputDir, count), image)   
        success,image = vidcap.read()
        print('Reading frame {}'.format(count))
        count += 1