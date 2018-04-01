# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import requests
import re
from lxml import etree


def Spider(url):
    i = 0
    print "downloading ", url
    myPage = requests.get(url).content.decode("gbk")
    print "finish"



if __name__ == '__main__':
    print "start"
    start_url = "https://www.baidu.com/s?wd=00700&rsv_spt=1&rsv_iqid=0xd54a5cde00009c74&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100"
    Spider(start_url)
    print "end"