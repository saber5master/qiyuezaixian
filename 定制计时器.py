# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:41:04 2017

@author: ice-fire
"""

import time as t

class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
        
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    
    # 重写一个方法， 让两个计时器对象相加会自动返回时间的和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop（） 开始计时"
        print("计时开始...")
    
    #停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start（） 开始计时")
        else:
            self.end = t.localtime()  #.localtime 返回的是一个时间元组的结构
            self._calc()
            print("计时结束...")
    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.stop[index] - self.start[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        print(self.prompt)
        # 为下一轮计算初始化变量
        self.begin = 0
        self.end = 0


#t1 = MyTimer()
#t1.start()
