# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:23:15 2017

@author: ice-fire
"""

#import tkinter as tk
#root = tk.Tk()
#root.title('FishC Demo')
#theLabel = tk.Label(root, text = '我的窗口程序！')
#theLabel.pack()
#root.mainloop()
#==============================================================================
# 
#==============================================================================
#import turtle as tu
#
#tu.forward(100)
#tu.right(144)
#tu.forward(100)
#tu.right(144)
#tu.forward(100)
#tu.right(144)
#tu.forward(100)
#tu.right(144)
#tu.forward(100)
#tu.right(144)

#==============================================================================
# 
#==============================================================================
#import builtwith
#
#te = builtwith.parse('http://www.baidu.com')
#print(te)

import requests
from bs4 import BeautifulSoup
import time

ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
headers = {'user-agent':ua}

url = 'http://www.ip138.com/ips138.asp?ip='

iplist = ['125.219.45.21', '125.219.48.21', '125.219.48.21','1.2.1.2','34.34.5.6','0.0.0.0']
for ip in range(len(iplist)):
    try:
        ip = iplist[ip]

        data = {'Accept-Encoding':'gzip, deflate',
                'Accept-Language':'h-CN,zh;q=0.8,en;q=0.6',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Host':'www.ip138.com',
                'Referer':'http://www.ip138.com/',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
                }
        weizhuang = requests.post(url + ip, data=data)
        print(weizhuang)
        res = requests.get(url + ip, headers = headers)
        
        res.encoding = res.apparent_encoding
        bs = BeautifulSoup(res.text, 'html5lib')
        #ge_address = bs.select('body > table > tbody > tr:nth-of-type(3) > td > ul')
        ge_address = bs.select('ul.ul1 > li')
        print('ip:', ip)
        with open('D:\ip.csv', 'a') as f:
            f.write(ip + '\n')
            f.close()
            
        for address in ge_address:
            print(address.text)
            with open('D:\ip.csv', 'a') as f:
                f.write(address.text + '\n')
                f.close()
        time.sleep(5)
    except:
        print('获取失败')
    
























