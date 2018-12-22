# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 19:14:55 2018

@author: fuwen
"""

from bs4 import BeautifulSoup
from subprocess import call
import requests,re,time,os

BookUrl = 'http://www.ting89.com/books/8988.html'
FilePath = r'D:\有声小说\梦落芳华_陌悠曦'


IdmPath = 'C:\idman_lv\IDMan.exe'
def IdmDownLoad(DownloadUrl, Mp3Name):
    call([IdmPath, '/d',DownloadUrl,'/p',FilePath,'/f',Mp3Name,'/n'])

AlreadyDown = [FileName for FileName in os.listdir(FilePath)]
Response = requests.get(BookUrl)
Response.encoding = 'gb2312'
html_doc = Response.text
Soup = BeautifulSoup(html_doc,'lxml')
MainSoup = Soup.find_all('div', class_ = 'compress')[0]
Detail = MainSoup.find_all('li')
DetailUrlList = [re.findall('href="(.*html)',str(i)) for i in Detail]
DetailUrlList = ['http://www.ting89.com'+s[0] for s in DetailUrlList]

for DetailUrl in DetailUrlList :
    response = requests.get(DetailUrl)
    response.encoding = 'gb2312'
    html_doc = response.text
    Mp3Url = re.findall(r'datas=\(\"(.*?)&',html_doc)[0]
    Mp3Name = Mp3Url.split('/')[-1]
    if Mp3Name in AlreadyDown :
        print('%s已经下载，本集跳过……'%Mp3Name)
    IdmDownLoad(Mp3Url, Mp3Name)
    time.sleep(2)

