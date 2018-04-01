# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import traceback
import re
import codecs
import sys


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""



def getQueryInfo(lst, stockURL, fpath):
    count = 0
    for query in lst:
        url = stockURL.replace("query_input",query)
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            #with open(fpath, 'wb') as f:
            with codecs.open(fpath, 'w', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print "\r当前进度: {:.2f}%".format(count * 100 / len(lst))
        except:
            count = count + 1
            print "\r当前进度: {:.2f}%".format(count * 100 / len(lst))
            continue

if __name__ == '__main__':
    query_info_url = 'https://www.baidu.com/s?wd=query_input'
    output_file = '/Users/wubp88/PycharmProjects/PythonSpiderNotes/Stock/BaiduStockInfo'
    print sys.getdefaultencoding()
    querylist = ['广州天气']
    print query_info_url.replace("query_input",querylist[0])
    getQueryInfo(querylist, query_info_url, output_file)



