# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 20:24:40 2017

@author: ice-fire
"""

def hannoi(n, x, y, z):
    if n == 1:
        print(x, '-->', z)
    else:
        hannoi(n - 1, x, z, y)#将前n - 1个盘子从X移动到Y上
        print(x, '-->', z)    #将最底下的第n个盘子从X移动到Z上
        hannoi(n - 1, y, x, z)#将Y上的n - 1个盘子移动到Z上
        
n = int(input('请输入汉诺塔的层数：'))
hannoi(n, 'X', 'Y', 'Z')






