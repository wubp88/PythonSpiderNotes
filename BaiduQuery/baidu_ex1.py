# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import traceback
import re
import codecs
import sys
import csv


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getAppList(stockURL,output_file):
            count = 0
            url = stockURL
            html = getHTMLText(url)
            # infoDict = {}
            infoList = []
            soup = BeautifulSoup(html, 'html.parser')

            appInfoList = soup.find_all(attrs={'class': 'name ofh'})
            # print(appInfoList[0])
            for i in range(len(appInfoList)):
                # print(appInfoList[i].text)
                infoList.append(appInfoList[i].text.encode('utf-8').strip())
                # infoDict.update({i: appInfoList[i].text})










if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=%E5%90%8C%E7%A8%8B'
    output_file = '/Users/wubp88/PycharmProjects/PythonSpiderNotes/BaiduQuery/相似公众号'

    getAppList(url,output_file)



