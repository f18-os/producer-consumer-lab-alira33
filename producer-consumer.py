from threading import Thread, Lock
import time
import random
from threading import Condition
from ExtractFrames import *

queue = []
lock = Lock()
MAX_NUM = 10
condition = Condition()

class ProducerThread(Thread):
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
            print ("Produced", frames)
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
            num = queue.pop(0)
            print ("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()