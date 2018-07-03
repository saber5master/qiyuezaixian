# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:48:36 2017

@author: ice-fire
"""

import requests
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'
headers = {'user-agent':ua}

url = 'https://www.bilibili.com'
referer = 'https://bilibili.com'
session = requests.Session()
formdata = {'Accept-Encoding':'gzip, deflate, br', 'Accept-Language':'zh-CN,zh;q=0.8', 'Connection':'keep-alive'}


resp = session.post(url, 
                    data = formdata, 
                    headers = headers)

bs = BeautifulSoup(resp.text, 'html5lib')
#pic_url = bs.select('#bili_bangumi > div > div.new-comers-module.l-con > div.storey-box.clearfix > div:nth-child(1) > a > div > div.lazy-img > img')
pic_url = bs.select('div[class="lazy-img"]')
print(pic_url)

















