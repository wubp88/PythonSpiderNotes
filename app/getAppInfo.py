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


def getAppList(stockURL,output_file,app_category):
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

            thefile = open(output_file, 'a')
            for item in infoList:
                print>> thefile, app_category+':'+ item








if __name__ == '__main__':
    url_pre = 'http://sj.qq.com/myapp/category.htm?orgame=1&categoryId='
    output_file = '/Users/wubp88/PycharmProjects/PythonSpiderNotes/app/应用宝.txt'
    # print sys.getdefaultencoding()
    app_category_list = ['购物','阅读','新闻','视频','旅游','工具','社交','音乐','美化','摄影','理财','系统','生活','出行','安全','健康','娱乐','儿童','办公','通讯']
    app_url_list = ['122','102','110','103','108','115','106','101','119','104','114','117','107','112','118','109','105','100','113','116']

    print(len(app_category_list))
    print(len(app_url_list))
    for i in range(len(app_category_list)):
        url = url_pre+app_url_list[i]
        print(app_category_list[i])

        getAppList(url,output_file,app_category_list[i])



