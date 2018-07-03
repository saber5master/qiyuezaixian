""" 使用selenium模拟百度搜索 """

from selenium import webdriver
import time

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('http://www.baidu.com')
    element = driver.find_element_by_css_selector('input#kw')
    element.send_keys('天气预报')
    element = driver.find_element_by_css_selector('input#su')
    driver.execute_script('arguments[0].click();', element)
    time.sleep(10) # 等10秒，查看搜索结果。

if __name__ == '__main__':
    main()
