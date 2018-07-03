# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:46:37 2017

@author: ice-fire
"""
# 1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#方法一：
#count = 0
#for i in range(1,5):
#    for j in range(1,5):
#        for k in range(1,5):
#            if i != j and i !=k and j != k:
#                count += 1
#                print("第 %d 个方案：" %count , i,j,k)
#print("能组成 %d 个互不相同且无重复数字的三位数" %count)

#方法二：
#from itertools import permutations
#count = 0
#for i in permutations([1, 2, 3, 4], 3):
#    k = ''
#    for j in range(0, len(i)):
#        k = k + str(i[j])
#    count += 1
#    print ("第 %d 个方案：" %count, int(k))   
#print("能组成 %d 个互不相同且无重复数字的三位数" %count)

# 2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

#def bonus_sum(I):
#    if I <= 100000:
#        bonus = I * 0.1
#    if 100000 < I <= 200000:
#        bonus = 10000 + (I - 100000) * 0.075
#    if 200000 < I <= 400000:
#        bonus = 10000 + 7500 + (I - 200000) * 0.05
#    if 400000 < I <= 600000:
#        bonus = 10000 + 7500 + 10000 + (I - 400000) * 0.03
#    if 600000 < I <= 1000000:
#        bonus = 10000 + 7500 + 10000 + 6000 + (I - 600000) * 0.015
#    if I > 1000000:
#        bonus = 10000 + 7500 + 10000 + 6000 + 6000 + (I - 1000000) * 0.01
#    return bonus
#
#I = int(input("请输入利润I："))
#print(bonus_sum(I))

# 3.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#x + 100 = n2
#x + 100 + 168 = m2

#m2 - n2 = 168
#(m + n)(m - n) = 168

#n = np.sqrt(x + 100)
#m = np.sqrt(x + 100 + 168)
#n < m
#方法一：
#for m in range(100):
#    for n in range(m):
#        if (m + n)*(m - n) == 168:
#            x = n**2 - 100
#            print("符合条件的整数有:",x)
#方法二：
#import numpy as np
#for x in range(-99,10000,1):
#    if int(np.sqrt(x + 100)) == np.sqrt(x + 100) and int(np.sqrt(x + 100 + 168)) == np.sqrt(x + 100 + 168):
#        print("符合条件的整数有:",x)
        
# 4.输入某年某月某日，判断这一天是这一年的第几天？
#year = int(input("请输入年份year:"))
#month = int(input("请输入月份month:"))
#day = int(input("请输入日期day:"))
#print(" ")
#
#months_1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
#months_2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年
#
#if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#    sum = months_1[month - 1] + day
#    print("今年是闰年")
#else:
#    sum = months_2[month - 1] + day
#    print("今年是平年")
#print("%d - %d - %d 是该年的第 %d 天"  %(year,month,day,sum))

# 5.输入三个整数x,y,z，请把这三个数由小到大输出。
#import numpy as np
#x = int(input("x = "))
#y = int(input("y = "))
#z = int(input("z = "))
#
#a = [x,y,z]
#b = np.array(a)
#print(a)
#print(b)
#c = np.sort(b)
#print(c[0],c[1],c[2])

# 6.斐波那契数列
#递归
#def Fibonacci(i):
#    if i == 0:
#        return 1
#    if i == 1:
#        return 1
#    return Fibonacci(i - 1) + Fibonacci(i - 2)

#迭代：
#def Fibonacci(n):
#    a, b = 1, 1
#    for i in range(n):
#        a, b = b, a + b
#    return a
#
#i = int(input("请输入n = ："))
#print("结果：", Fibonacci(i))

# 7.将一个列表的数据复制到另一个列表中。

# 8.输出 9*9 乘法口诀表
#for i in range(10):
#    for j in range(1, i+1):
#        print("%d × %d = " %(j,i), i*j, end = " ")
#    print("\n")

# 9.暂停一秒输出








