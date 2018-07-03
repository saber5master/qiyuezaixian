# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:39:41 2017

@author: ice-fire
"""

#import requests

#UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
#kv = {'user-agent':UA}
#
#url = "https://www.amazon.cn/%E5%80%BE%E5%9F%8E%E4%B9%8B%E6%81%8B-%E5%BC%A0%E7%88%B1%E7%8E%B2/dp/B0084XA1JA/ref=sr_1_1?m=A1AJ19PSB66TGU&s=books&ie=UTF8&qid=1503391277&sr=1-1"
#
#r = requests.get(url, headers = kv)
#print(r.status_code)
#print(r.text[1000:2000])

#
#import requests
#
#UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
#kv = {'user-agent':UA}
#
#url = "https://www.amazon.cn/%E5%80%BE%E5%9F%8E%E4%B9%8B%E6%81%8B-%E5%BC%A0%E7%88%B1%E7%8E%B2/dp/B0084XA1JA/ref=sr_1_1?m=A1AJ19PSB66TGU&s=books&ie=UTF8&qid=1503391277&sr=1-1"
#
#try:
#    r = requests.get(url, headers = kv)
#    r.raise_for_status()
#    r.encoding = r.apparent_encoding
#    print(r.text[1000:2000])
#except:
#    print("爬取失败！")
#    
    
#==============================================================================
# 
#==============================================================================

import requests
from bs4 import BeautifulSoup

UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
kv = {'user-agent':UA}

url = "https://www.amazon.cn/%E5%80%BE%E5%9F%8E%E4%B9%8B%E6%81%8B-%E5%BC%A0%E7%88%B1%E7%8E%B2/dp/B0084XA1JA/ref=sr_1_1?m=A1AJ19PSB66TGU&s=books&ie=UTF8&qid=1503391277&sr=1-1"


resp = requests.get(url, headers = kv)
text = resp.text.encode('iso-8859-1').decode('gbk')
bs = BeautifulSoup(text, 'html5lib')
row_1 = bs.select('span.a-size-base.a-color-price')
row_2 = bs.select('span#productTitle.a-size-large')


















































