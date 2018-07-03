import requests
import re

def getHTMLText(url):
	try:
		r = requests.get(url, timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
	

def parsePage(ilt, html):
	print("")

def  printGoodsList(ilt):
	tplt = "{:4}\t{:8}\t{:16}"
	print("")

def main():
	goods = '耳机'
	depth = 2		# 访问深度
	start_url = 'https://s.taobao.com/search?q=' + goods
	
	infoList = []
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44 * i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList)
main()