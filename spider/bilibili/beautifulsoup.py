# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:59:37 2017

@author: saber_master
"""

import requests
from bs4 import BeautifulSoup
import bs4

UA = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'


headers = {'User-Agent':UA}

# 获取url信息, 输出url内容模块
def getHTMLText(url):
    try:
        r = requests.get(url, headers = headers, timeout = 30)
        r.raise_for_status() # 异常信息
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 提取html信息并存入ulist列表中
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds  = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])
        
        
def printUnivList(ulist, num):
    tplt = "{0:10}\t{1:{3}^10}\t{2:^10}" # {3} 使用第三个元素进行填充
    print(tplt.format("排名", "学校名称", "省份", chr(12288))) # chr(12288):用中文空格进行填充
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))
    
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html' # 2017 年的模式和2016年的不一样
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)
main()





















