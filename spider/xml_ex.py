# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:06:10 2017

@author: ice-fire
"""

from xml.dom import minidom

doc = minidom.parse("books.xml")
root = doc.documentElement
print(type(root))
print(root.nodeName)
#print(dir(root))
books = root.getElementsByTagName('book')
for book in books:
    titles = book.getElementsByTagName('title')
    prices = book.getElementsByTagName('price')
    title = titles[0].childNodes[0].nodeValue
    price = prices[0].childNodes[0].nodeValue
    print(title, "-", price)
    
    