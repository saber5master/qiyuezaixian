# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 10:42:59 2017

@author: ice-fire
"""

#==============================================================================
# 
#import requests as r
#r.status_codes : 1. 200 ; 2. 404 或其他某些原因出错 
#r.text
#r.encoding
#r.apparent_encoding
#r.content

#==============================================================================

#==============================================================================
# 
# import requests
# 
# r = requests.get("http://www.baidu.com")
# 
# print(r.status_code)
# 
# print("r.encoding:", r.encoding)
# # 如果header中不存在charset，　则认为编码为ISO-8859-1
# print("r.apparent_encoding:", r.apparent_encoding)
# # 根据网页内容分析出的编码方式
# r.encoding = "utf-8"
# 
# print(r.text)
#==============================================================================

#==============================================================================

# requests 库的异常
#import requests

#requests.ConnectionError : 网络连接异常，如 dns 查询失败，拒绝连接等
#requests.HTTPError : http错误异常
#requests.URLRequired : URl 缺失异常
#requests.TooManyRedirects : 超过最大重定向次数，产生重定向异常
#requests.ConnectTimeout : 连接远程服务超市异常
#requests.Timeout : 请求URl超市，产生超时异常

#r = requests.get("http://www.baidu.com")
#r.raise_for_status() 如果状态不是200 ， 引发httpError 异常
#
#def getHtmlText(url):
#    try:
#        r = requests.get(url, timeout = 30)
#        r.raise_for_status() #如果状态不是200 ， 引发httpError 异常
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return "产生异常"
#    
#if __name__ == "__main__":
#    url = "http://www.bidu.com"
#    print(getHtmlText(url))

#==============================================================================
#import requests

#r = requests.head("http://httpbin.org/get", data = "ABC")
#print("r.headers:",r.headers)
#print(r.text)  

#
#ua = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
#headers = {'user-agent':ua}
#url = "http://httpbin.org/"
#
#r_1 = requests.get(url + "get", headers = headers)
#r = requests.post(url + "post", headers = headers, data = "ABC")
#print(r_1.text)
#print(r.text) 

#==============================================================================

#import requests

#requests 的七种请求方法：方法 + url + **kwargs

# 1.requests.get:
# 2.requests.head:
# 3.requests.post:
# 4.requests.put:
# 5.requests.patch:
# 6.requests.delete:
# 7.requests.options:

# requests 的13种控制访问参数：

#1.params:字典或字节序列，作为参数增加到url中
#kv = {"key1":"value1", "key2":"value2"}
#r = requests.request("get", "http://python123.io/ws", params = kv)
#print(r.url)


#2.data:字典、字节序列或文件对象，作为request的内容
#kv = {"key1":"value1", "key2":"value2"}
#r = requests.request("post", "http://python123.io/ws", data = kv)
#body = "主题内容"
#r = requests.request("post", "http://python123.io/ws", data = body)


#3.josn:json 格式的数据，作为request的内容

#kv = {"key1":"value1"}
#r = requests.request("post", "http://python123.io/ws",json = kv)
#print(r.text)

#4.headers:字典，http定制头字段
#hd = {'user-agent':'Chorm/10'}
#r = requests.request('post', 'http://python123.io/ws', headers = hd)
#print(r.text)

#5.cookies:字典或cookiejar， request中的cookie

#6.auth：元组，支持http认证功能

#7.files:字典类型，传输文件
#fs = {'file':open('data.xls','rb')}
#r = requests.request('post', 'http://python123.io/ws', files = fs)

#8.timeout:设定超时时间，秒为单位

#9.proxies:字典类型，设定访问代理服务器，可以增加登录认证。 可以有效的防止爬虫的逆追踪。
#pxs = {'http': 'http://user:pass@10.10.10.1:1234'
#       'https': 'https://10.10.10.1:4321'}
#r = requests.request('get', 'http://www.baidu.com', proxies = pxs)

#高级功能：
#10. allow_redirects:True/False, 默认为 True, 重定向开关

#11. stream：True/False, 默认为 True, 获取内容立即下载开关

#12. verify: True/False, 默认为 True, 认证SSL证书开关

#13. cert: 本地SSL证书路径


#cookies:
#import requests
#
#cookies = {'k1':'v1', 'k2':'v2'}
#resp = requests.get('http://httpbin.org/cookies', cookies = cookies)
#print(resp.text)
##resp = requests.get('http://www.baidu.com')
#for key in resp.cookies.keys():
#    print('%s : %s' % (key, resp.cookies[key]))
   
































