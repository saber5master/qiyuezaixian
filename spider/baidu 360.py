# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:19:44 2017

@author: ice-fire
"""

import requests

url = "http://www.baidu.com/s"
kv = {"wd":"太古神王"}
r = requests.get(url, params=kv)
print(r.status_code)
print(r.request.url)
print(len(r.text))


