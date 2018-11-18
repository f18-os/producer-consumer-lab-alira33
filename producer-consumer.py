from threading import Thread, Lock
import time
import random
from threading import Condition
import threading
from ConsumerThread import * 
from ExtractFrames import *
from ConvertToGrayscale import *
from DisplayFrames import *

queue = []
lock = Lock()
MAX_NUM = 10
condition = Condition()

# class ProducerThread(Thread):
#     def run(self):
#         global queue
#         i = 0
#         while True:
#             condition.acquire()
#             if len(queue) == MAX_NUM:
#                 print ("Queue full, producer is waiting")
#                 condition.wait()
#                 print ("Space in queue, Consumer notified the producer")

#             print ("Extrating frames")
#             frames = extract()
#             queue.append(i)
            
#             condition.notify()
#             condition.release()
#             time.sleep(random.random())


# class ConsumerThread(Thread):
#     def run(self):
#         global queue
#         while True:
#             condition.acquire()
#             if not queue:
#                 print ("Nothing in queue, consumer is waiting")
#                 condition.wait()
#                 print ("Producer added something to queue and notified the consumer")
#             frame = queue.pop(0)
#             #print ("Consumed", num)
#             print ("Consumed extracting frames")
#             condition.notify()
#             condition.release()
#             time.sleep(random.random())


extract(Thread)
