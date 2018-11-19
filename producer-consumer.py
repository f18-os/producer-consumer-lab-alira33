from ExtractFrames import *
from ConvertToGrayscale import *
from DisplayFrames import *

from threading import Thread, Condition
import time
import random

queue = []
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
    def run(self):
        global queue
        i = 0
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print ("Queue full, producer is waiting")
                condition.wait()
                print ("Space in queue, Consumer notified the producer")

            # Extracting frames
            ExtractProducerThread().start()

             # Converting to Grayscale
            GrayscaleProducerThread().start()

             # Displaying frames
            DisplayProducerThread().start()

            # Adding to queue
            queue.append(i)
            i = i + 1
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            
            # Removing it from queue
            queue.pop(0)
            condition.notify()
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()