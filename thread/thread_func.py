# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:16:48 2017

@author: ice-fire
"""

import threading

def thread_func(x):
    print("%d\n" %(x * 100))

threads = []
for i in range(6):
    threads.append(threading.Thread(target=thread_func, args=(100,)))
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()  #等进程结束
    
#import logging # 打日志
#logging.info()
#logging.debug()


