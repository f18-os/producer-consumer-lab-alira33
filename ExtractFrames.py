#!/usr/bin/env python3

import cv2
import os
from threading import Thread, Lock
import time
import random
from threading import Condition
import threading
from ConvertToGrayscale import *
from DisplayFrames import *
import sys

queue = []
queue_frames = []
# globals
outputDir    = 'frames'
clipFileName = 'clip.mp4'
# initialize frame count

queue = []
lock = Lock()
terminate = False
MAX_NUM = 10 #requirement completed: is being halved to 10
condition = Condition()

class ProducerThread(Thread):
  def run(self):
      global queue
      global queue_frames
      global terminate
      count = 0
      i = 0

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
        print('Reading frame {}'.format(count))
        success,image = vidcap.read()
        
        #pylint: disable-msg=R0913
        grayFrame = GrayscaleThread(Thread, image, i)

        queue_frames.append(grayFrame)
        queue.append(count)
        count += 1
        i += 1

        if(image is None):
            terminate = True
            condition.wait()

      cv2.destroyAllWindows()

class ConsumerThread(Thread):
    def run(self):
        global queue
        global queue_frames
        global terminate
        i = 0

        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            while i < len(queue_frames):
                #pylint: disable-msg=R0913
                display(Thread, queue_frames[i], i)
                i += 1
            queue.pop(0)
            print ("Consumed extracting frames")
            condition.notify()
            condition.release()
            time.sleep(random.random())

            if(terminate):
                cv2.destroyAllWindows()
                try:
                    sys.exit()  # this always raises SystemExit
                except SystemExit:
                    print("sys.exit() worked as expected")
                except:
                    # some other exception got raised
                    print("Something went horribly wrong")
 
ProducerThread().start()
ConsumerThread().start()