# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:28:30 2017

@author: ice-fire
"""
# 方法一：
import requests
from PIL import Image
from io import BytesIO

url = "http://www.ttpaihang.com/image/vote/u150125085054190183.jpg"

re = requests.get(url)
image = Image.open(BytesIO(re.content))
image.save('heimao1.jpg')  # 必须以英文命名文件


# 方法二：
#import requests
#
url = "http://www.ttpaihang.com/image/vote/u150125085054190183.jpg"
r = requests.get(url)
#print(r.status_code)
with open ("黑猫2.jpg",'wb') as f:
    f.write(r.content)  #返回内容的二进制形式


# 方法三：
#import requests
#
url = "http://www.ttpaihang.com/image/vote/u150125085054190183.jpg"
r = requests.get(url, stream = True)
with open('黑猫3.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)
    
 

