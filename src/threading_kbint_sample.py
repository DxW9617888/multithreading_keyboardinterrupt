#!/usr/bin/env python3
# @author: Bruce Wan

from queue import Queue
import threading
from time import sleep
import sys

def world(outq):
      while True:
          if outq.qsize() > 0:
              data = outq.get()
              print('Get the queue: %s' %data)
              if data == 'QUIT':
                  sys.exit('world will be exit...')
          print('world checking...')
  
def hello(outq):
      while True:
          if outq.qsize() > 0:
              data = outq.get()
              print('Get the queue: %s' %data)
              if data == 'QUIT':
                  sys.exit('hello will be exit...')
          print('hello checking...')


if __name__ == '__main__':
     q1 = Queue()    # th1 專用
     q2 = Queue()    # th2 專用
     th1 = threading.Thread(target=hello, args=(q1,))
     th2 = threading.Thread(target=world, args=(q2,))
     th1.start()
     th2.start()
     while True:
         try:
             sleep(1)
             if not th1.is_alive() and not th2.is_alive():
                 print('Child threading all exited.')
                 break
         except KeyboardInterrupt:
             q1.put('QUIT')
             q2.put('QUIT')
             th1.join()
             th2.join()
     sys.exit('main thead has be exit')
 