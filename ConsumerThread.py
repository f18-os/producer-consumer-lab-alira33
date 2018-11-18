from threading import Thread, Lock
import time
import random
from threading import Condition
import threading

lock = Lock()
condition = Condition()

class ConsumerThread(Thread):
    def run(self, queue):
        while True:
            condition.acquire()
            if not queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            queue.pop()
            print ("Consumed extracting frames")
            condition.notify()
            condition.release()
            time.sleep(random.random())