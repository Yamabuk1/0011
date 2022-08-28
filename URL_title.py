import re   #正则表达式的库
from bs4 import BeautifulSoup   #从网页中提取数据的库
import requests     #爬取网页的库


def return_dict(un = 1) :                               #un是大学标志
    if un == 0 :
        url = 'https://yz.tsinghua.edu.cn/zxgg.htm'     
        #该大学信息发布的网站
        header = {"user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        #请求头
        req = requests.get(url=url,headers=header)          #爬取网站
        req.encoding = 'utf-8'                              #确定字体编码
        html = req.text                                     #把网站内容写入文件
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("div",class_ = "admission")        #从网站容中获取文本

        with open(r"C:\Users\86183\Desktop\营\req.txt","w") as file:
            for line in texts:
                file.write(str(line)+"/n")
        #打开文件，写入文本
        file = open(r'C:\Users\86183\Desktop\营\req.txt')
        txt = file.read()              
        file.close()                
        #打开文件，读取文本
        pattern1 = re.compile(r'href=\"([^\"]+).*?')   
        tuple1=re.findall(pattern1,txt)
        #通过正则获取网址，返回一个元组
        pattern2 = re.compile(r'title=\"([^\"]+)')
        tuple2=re.findall(pattern2,txt)
        #通过正则获取标题，返回一个元组
        return(dict(zip(tuple2, tuple1)))
        #将两元组转换为字典，并返回
        
        
    #下面基本是一样的
    elif un == 1 :
        global strinfo
        url = 'https://admission.pku.edu.cn/xxgk/xxgkssbm/index.htm?CSRFT=2PHA-DZ90-R1Y4-JCWS-LKQD-PR1L-66US-X5F3'
        header = {"user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        req = requests.get(url=url,headers=header)
        req.encoding = 'utf-8'
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("ul",class_ = "zsxx_cont_list")
        
        with open(r"C:\Users\86183\Desktop\营\req.txt","w") as file:
            for line in texts:
                file.write(str(line)+"/n")
        print("into final")

        file = open(r"C:\Users\86183\Desktop\营\req.txt")
        txt = file.read()              
        file.close()                

        pattern1 = re.compile(r'href=\"([^\"]+).*?')   
        tuple1=re.findall(pattern1,txt)
        
        pattern2 = re.compile(r'fl\">\s*(\S*)')
        tuple2=re.findall(pattern2,txt)
        

        return(dict(zip(tuple2, tuple1)))

    elif un == 2: 
        global strinfo
        url = 'http://www.grs.zju.edu.cn/yjszs/28498/list.htm'
        header = {"user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        req = requests.get(url=url,headers=header)
        req.encoding = 'utf-8'
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("ul",class_ = "common-news-list")
    
        with open(r"C:\Users\86183\Desktop\营\req.txt","w") as file:
            for line in texts:
                file.write(str(line)+"/n")
        print("into final")

        file = open(r"C:\Users\86183\Desktop\营\req.txt")
        txt = file.read()              
        file.close()                

        pattern1 = re.compile(r'href=\"([^\"]+).*?')   
        tuple1=re.findall(pattern1,txt)
        list1=list(tuple1)
        new_list = ['http://www.grs.zju.edu.cn'+x for x in list1]
        
        pattern2 = re.compile(r'title=\"(\S*)\"')
        tuple2=re.findall(pattern2,txt)
        

        return(dict(zip(tuple2, new_list)))

    elif un == 3:
        global strinfo
        url = 'https://gsao.fudan.edu.cn/15014/list.htm'
        header = {"user-agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"}
        req = requests.get(url=url,headers=header)
        req.encoding = 'utf-8'
        html = req.text
        bes = BeautifulSoup(html,"lxml")
        texts = bes.find("ul",class_ = "cols_list clearfix")
        
        with open(r'C:\Users\86183\Desktop\营\req.txt',"w") as file:
            for line in texts:
                file.write(str(line)+"/n")
        print("into final")

        file = open(r'C:\Users\86183\Desktop\营\req.txt')
        txt = file.read()              
        file.close()                

        pattern1 = re.compile(r'href=\"([^\"]+).*?')   
        tuple1=re.findall(pattern1,txt)
        list1=list(tuple1)
        new_list = ['https://gsao.fudan.edu.cn'+x for x in list1]
        
        pattern2 = re.compile(r'title=\"(\S*)\"')
        tuple2=re.findall(pattern2,txt)

        return(dict(zip(tuple2, new_list)))
        




