# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 21:26:41 2017

@author: ice-fire
"""
#
#import random as r
#
#class Fish:
#    def __init__(self):
#        self.x = r.randint(0, 10)
#        self.y = r.randint(0, 10)
#    def move(self):
#        #所有鱼都向西
#        self.x -= 1
#        print("我的位置是：", self.x, self.y)
#class Goldfish(Fish):
#    pass
#class Carp(Fish):
#    pass
#class Salmon(Fish):
#    pass
#
#class Shark(Fish):
#    def __init__(self):
#        Fish.__init__(self) #方法一：调用未绑定的父类方法
#        super().__init__()  #方法二：使用super函数
#        self.hungry = True
#    def eat(self):
#        if self.hungry:
#            print("天天吃^-^")
#            self.hungry = False
#        else:
#            print("太撑了")
            
#菱形问题
class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")

class B(A):
    def __init__(self):
        print("进入B…")
        A.__init__(self)
        print("离开B…")
        
class C(A):
    def __init__(self):
        print("进入C…")
        A.__init__(self)
        print("离开C…")

class D(B, C):
    def __init__(self):
        print("进入D…")
        B.__init__(self)
        C.__init__(self)
        print("离开D…")

D()
#进入D…
#进入B…
#进入A…
#离开A…
#离开B…
#进入C…
#进入A…
#离开A…
#离开C…
#离开D…
#        