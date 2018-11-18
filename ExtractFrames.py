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

queue = []
lock = Lock()
MAX_NUM = 20 #requirement completed: is being halved to 10
condition = Condition()

class ProducerThread(Thread):
  def run(self):
      global queue
      count = 0

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
        if len(queue) == MAX_NUM:
                  print ("Queue full, producer is waiting")
                  condition.wait()
                  queue = [] #space for queue
                  print ("Space in queue, Consumer notified the producer")

        # write the current frame out as a jpeg image
        cv2.imwrite("{}/frame_{:04d}.jpg".format(outputDir, count), image)   
        success,image = vidcap.read()
        queue.append(image)  
        print('Reading frame {}'.format(count))
        queue.append(count)
        count += 1

class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            queue.pop(0)
            print ("Consumed extracting frames")
            condition.notify()
            condition.release()
            time.sleep(random.random())
 
ProducerThread().start()
ConsumerThread().start()