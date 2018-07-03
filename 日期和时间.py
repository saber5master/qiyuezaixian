# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 09:35:09 2017

@author: ice-fire
"""

import time # 引入time模块
import datetime
# python提供了一个 time 和 calendar 模块可以用于格式化日期和时间。

# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
ticks = time.time() #函数time.time()用于获取当前时间戳,
print("当前时间戳为:", ticks)

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" %i)