""" bs4使用例子 """

from bs4 import BeautifulSoup

def main():
    bs = None
    with open('shanghai_weather_20170812.shtml', 'r') as f:
        bs = BeautifulSoup(f.read(), 'html5lib')
        elements = bs.find_all('meta')
        print(elements)
        element = bs.find(id='colorid')
        print(element)
        element = bs.find(text='预警')
        print(element)
        element = bs.find(attrs={'class':'shengjz'})
        print(element)

if __name__ == '__main__':
    main()
