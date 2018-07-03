# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 15:18:42 2017

@author: ice-fire
"""
#
#import urllib.request, random
#
#url = 'http://www.whatismyip.com.tw/'
#
##print('添加代理IP地址(ip：端口号), 多个IP地址间用英文的分号隔开！')
##iplist = input("请开始输入：").split(sep=";")
### 124.254.57.150:8118;61.184.192.42:80;88.88.88.88:88
#iplist = ['124.254.57.150:8118', '61.184.192.42:80', '88.88.88.88:88']
#print('iplist:', iplist)
#print('type(iplist):', type(iplist))
#while True:
#    ip = random.choice(iplist)
#    proxy_suport = urllib.request.ProxyHandler({'http':ip})
#    opener = urllib.request.build_opener(proxy_suport)
#    UA = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
#    opener.addheaders = [('User-Agent', UA)]
#    urllib.request.install_opener(opener)
#    try:
#        print('正在尝试使用 %s 访问...' % ip)
#        response = urllib.request.urlopen(url)
#    except urllib.request.URLError:
#        print('访问出错')
#    else:
#        print('访问成功')
#    if input('请问是否继续？(Y/N)') == 'N':
#        break
#==============================================================================
# 
#==============================================================================
import urllib.request

url = 'http://www.whatismyip.com.tw/'

#print('添加代理IP地址(ip：端口号), 多个IP地址间用英文的分号隔开！')
#iplist = input("请开始输入：").split(sep=";")
## 124.254.57.150:8118;61.184.192.42:80;88.88.88.88:88
iplist = ['124.254.57.150:8118', '61.184.192.42:80', '88.88.88.88:88']
print('iplist:', iplist)
print('type(iplist):', type(iplist))
for ip in range(len(iplist)):
    ip = iplist[ip]
    proxy_suport = urllib.request.ProxyHandler({'http':ip})
    opener = urllib.request.build_opener(proxy_suport)
    UA = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    opener.addheaders = [('User-Agent', UA)]
    urllib.request.install_opener(opener)
    try:
        print('正在尝试使用 %s 访问...' % ip)
        response = urllib.request.urlopen(url)
    except urllib.request.URLError:
        print('访问出错')
    else:
        print('访问成功')
    
