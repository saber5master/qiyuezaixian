# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 22:39:41 2017

@author: ice-fire
"""

import urllib.request
import urllib.parse
import json

UA = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
referer = 'http://fanyi.youdao.com/'
head = {'Referer':referer, 'User-Agent':UA}

content = input('请输入需要翻译的内容：')
data = {'type':'AUTO','i':content,'doctype':'json','xmlVersion':'1.6','keyfrom':'fanyi.web','ue':'UTF-8','typeResult':'true'}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
#print(response)
html = response.read().decode('utf-8')
#print(html)
target = json.loads(html)
print(type(target))
print("翻译结果： %s" % (target['translateResult'][0][0]['tgt']))
