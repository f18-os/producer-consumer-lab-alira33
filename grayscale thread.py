from threading import Thread, Lock
import time
import random
from threading import Condition
from ExtractFrames import *
from ConvertToGrayscale import *

queue = []
lock = Lock()
MAX_NUM = 10
condition = Condition()

class GrayProducerThread(Thread):
    def run(self):
        frames = extract()
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print ("Queue full, producer is waiting")
                condition.wait()
                print ("Space in queue, Consumer notified the producer")
            
            queue.append(frames)
            print ("Converting frames to grayscale")
            grayscale(frames)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class GrayConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            frame = queue.pop(0)
            #print ("Consumed", num)
            print ("Consumed extracting frames")
            condition.notify()
            condition.release()
            time.sleep(random.random())


GrayProducerThread().start()
GrayConsumerThread().start()