# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:27:42 2017

@author: ice-fire
"""

#import threading
#
#def loop():
#    thread_name = threading.current_thread().name
#    print('Thread %s is running...' % thread_name)
#    n = 0
#    while n < 5:
#        n += 1
#        print('Thread %s >>> %d' % (thread_name, n))
#    print('Thread %s ends.' % thread_name)
#
#thread_name = threading.current_thread().name
#print('Thread %s is running...' % thread_name)
#t = threading.Thread(target=loop, name='loopThread')
#t.start()
#t.join()
#print('Thread %s end.' % thread_name)

#==============================================================================

#from multiprocessing import Process
#import os
#
#def run_peoc(name):
#    print('Run child process %s (%s)' % (name, os.getpid()))
#
#if __name__ == '__main__':
#    print('Parent process %s. ' % os.getpid())
#    p = Process(target = run_peoc, args = ('test',))
#    p.start()
#    p.join()
#    print('End')

#==============================================================================
# 
import threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n + 1
    balance = balance - n

def run_thread(n):
    for i in range(100):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(1, )) # 每次修改多少 5
t2 = threading.Thread(target=run_thread, args=(1, )) # 每次修改 10
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#==============================================================================























