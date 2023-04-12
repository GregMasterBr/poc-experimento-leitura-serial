import multiprocessing
import os
import time

the_queue = multiprocessing.Queue()

def worker_main(queue):
    print (os.getpid(),"working")
    while True:
        item = queue.get(True)
        print (os.getpid(), "got", item)
        time.sleep(1) # simulate a "long" operation

the_pool = multiprocessing.Pool(3, worker_main,(the_queue,))
#                           don't forget the comma here  ^

for i in range(5):
    the_queue.put("hello")
    the_queue.put("world")


time.sleep(10)