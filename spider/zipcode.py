""" 获取全国邮政编码和区号 """

import requests
from bs4 import BeautifulSoup

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

def parse_province(province, url):
    resp = requests.get(url, headers={'user-agent':UA})
    text = resp.text.encode('iso-8859-1').decode('gbk')
    bs = BeautifulSoup(text, 'html5lib')
    rows = bs.select('table.t12 > tbody > tr')
    for i in range(1, len(rows)):
        tds = rows[i].select('td')
        area_1 = tds[0].text.strip()
        if area_1:
            post = tds[1].text.strip()
            tel = tds[2].text.strip()
#            print('%s,%s,%s,%s' % (province, area_1, post, tel))
            with open('邮政.text','a') as f:
                f.write('%s,%s,%s,%s\n' % (province, area_1, post, tel))
                f.close()
        if len(tds) == 6:
            area_2 = tds[3].text.strip()
            if area_2:
                post = tds[4].text.strip()
                tel = tds[5].text.strip()
#                print('%s,%s,%s,%s' % (province, area_2, post, tel))
                with open('邮政.text','a') as f:
                    f.write('%s,%s,%s,%s\n' % (province, area_2, post, tel))
                    f.close()

def main():
    base_url = 'http://www.ip138.com'
    resp = requests.get(base_url + '/post', headers={'user-agent':UA})
    # 与实际编码不同，必须进行转换。
    text = resp.text.encode('iso-8859-1').decode('gbk')
    bs = BeautifulSoup(text, 'html5lib')
    provinces = bs.select('div#newAlexa > table > tbody > tr > td > a')
    for province in provinces:
        parse_province(province.text, base_url + province.get('href'))
    print("爬取完毕！")

if __name__ == '__main__':
    main()
