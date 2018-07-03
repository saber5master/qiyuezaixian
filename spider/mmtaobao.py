import requests
import random
from bs4 import BeautifulSoup
import json

ua_list = ['Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)']
ua = random.choice(ua_list)
headers = {'user-agent':ua}

# url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'

def get_url_list(url):
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'html.parser')
    user_id_list = json.dumps()
    print(user_id_list)
    
    # user_id_list = soup.

    # return user_id
    
    
# def get_album(self, user-id):
#     req = 

# def get_info(self, user-id):

get_url_list(url)




