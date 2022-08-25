# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 09:05:00 2022

@author: 山吹久远
"""

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://yz.tsinghua.edu.cn/zxgg.htm'
    header = {"user-agent":
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
    req = requests.get(url=url,headers=header)
    req.encoding = 'utf-8'
    html = req.text
    bes = BeautifulSoup(html,"lxml")
    texts = bes.find("div",class_ = "admission")
    print(texts)
    with open("C:/Users/666666/Desktop/req.txt","w") as file:
        for line in texts:
            file.write(str(line)+"/n")
            