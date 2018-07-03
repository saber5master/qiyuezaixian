# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 09:38:49 2017

@author: ice-fire
"""

#import re

# re.match：这个方法将会从string（我们要匹配的字符串）的开头开始，尝试匹配pattern，一直向后匹配，如果遇到无法匹配的字符，立即返回None，如果匹配未结束已经到达string的末尾，也会返回None。两个结果均表示匹配失败，否则匹配pattern成功，同时匹配终止，不再对string向后匹配。

#match = re.match(r'hello', 'hello world')
#if match:
#    print(match.span())
#    print(match.group())

#==============================================================================

# re.search：search方法与match方法极其类似，区别在于match()函数只检测re是不是在string的开始位置匹配，search()会扫描整个string查找匹配。
    
# 正则表达式不能有空格
#match = re.search(r'\d{3,3}-\d{8,8}', 'SH: 021-6666666666')
#if match:
#    print(match.span())
#    print(match.group())

#=============================================================================

# re.findall：搜索string，以列表形式返回全部能匹配的子串。

#match = re.findall(r'\d+', 'a12b123c1234')
#if match:
#    print(match)
    
#==============================================================================
#  
#==============================================================================

# ======下午的课=======

#css 选择器:
#1.class选择：tag#XXX id是# class是.
#2.属性选择：tag[type = ][value = ]
#3.层级关系：head > body > p
##    
#from selenium import webdriver
#
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors') #忽视证书
#driver = webdriver.Chrome(chrome_options=options)
#driver.get('http://www.weather.com.cn/weather/101180101.shtml')
#element = driver.find_element_by_css_selector('ul.t.clearfix')
#
#print(element.text)
#driver.quit()


#from selenium import webdriver
#import time
#
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors') #忽视证书
#driver = webdriver.Chrome(chrome_options=options)
#driver.get('http://www.baidu.com')
#element = driver.find_element_by_css_selector('imput#kw')
#element.send_keys('天气预报')
#element = driver.find_element_by_css_selector('imput#su')
#driver.execute_script('arugments[0].click;', element)
#time.sleep(10) # 等10秒，查看搜索结果
##
#=============================================================================    
    
#import re

#mr = re.match(r'\d{3}-\d{3,8}', '010-223456')
#print(mr.string)
#
#m = re.match(r'(\d{3})-(\d{3,8})$', '012-876543')
#print(m.groups())
#print(m.group(0))
#print(m.group(1))
#print(m.group(2))

# 时间字符串
#t = '20:15:45'
#m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
#print(m.groups())
#
## 分割
#p = re.compile(r'\d+')
#print(type(p))
#print(p.split('one1two3three3four4'))
#print(m.group(2))
 
    
    
    
    
    
    
    
    
    
    
    



