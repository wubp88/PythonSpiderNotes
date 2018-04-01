import urllib2
import urllib
from bs4 import BeautifulSoup
import numpy as np
import json
def write2txt(data,filepath):
    with open(filepath,'a') as f:
        for d in data:
            f.write(d.encode('utf-8'))

def example3_bs4():
    #request = urllib2.Request('http://poi.mapbar.com/shanghai/')
    request = urllib2.Request('http://caipiao.163.com/order/')
    #request = urllib2.Request('https://www.baidu.com/')
    page = urllib2.urlopen(request)
    data = page.read()
    data = data.decode('utf-8')
    soup = BeautifulSoup(data,'html.parser')
    tags = soup.select('a')
    res = [ t['href']+'|'+t.get_text()+'\n' for t in tags]
    #print res
    #write2txt(res,'/Users/wubp88/PycharmProjects/PythonSpiderNotes/BaiduQuery/data/keyword1')


def getKeyWords():
    with open('/Users/wubp88/PycharmProjects/PythonSpiderNotes/BaiduQuery/data/keywordtmp') as f:
        for line in f:
            url,wd=line.decode('utf-8').split('|')
            print url,wd
            request = urllib2.Request(url)
            page = urllib2.urlopen(request)
            data = page.read().decode('utf-8')
            soup = BeautifulSoup(data,'html.parser')
            tags = soup.select('dd a')
            res = [wd[:-1]+'|'+t['href']+'|'+t.get_text()+'\n' for t in tags]
            print len(res)
            write2txt(res,'/Users/wubp88/PycharmProjects/PythonSpiderNotes/BaiduQuery/data/keyword2')


if __name__ == '__main__':
    example3_bs4()
    #getKeyWords()
