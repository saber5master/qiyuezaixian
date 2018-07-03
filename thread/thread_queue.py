# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:26:05 2017

@author: ice-fire
"""

# FIFO first in first out
# LIFO last in first out
# Priority Queue

#import queue
#import threading
#
#q = queue.Queue()
#for i in range(5):
#    q.put(i)
#
#while not q.empty():
#    print(q.get())
#
#q = queue.LifoQueue()
#for i in range(5):
#    print(q.get())
#
#class Task:
#    def __init__(self, priority, description):
#        self.priority = priority
#        self.description = description
#    
#    def __It__(self, other): # 比较函数
#        return self.priority < other.priority
#
#q = queue.PriorityQueue()
#q.put(Task(1, 'Important task'))
#q.put(Task(10, 'Normal task'))
#q.put(Task(100, 'Lazy task'))
#
#def job(q):
#    while True:
#        task = q.get()
#        print('Task:', )

#==============================================================================
# 
#==============================================================================

import urllib.request
import re, os

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
#    print(html)
    return html

def get_img(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    imglist = re.findall(p, html)
#    print(imglist)
    try:
        os.mkdir('NewPics')
    except FileExistsError:
        pass
    os.chdir('Newpics')
    for each in imglist:
#        print(each)
        filename = each.split('/')[-1][-9::]
        urllib.request.urlretrieve(each, filename, None)
        
if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3823765471'
    get_img(open_url(url))





























