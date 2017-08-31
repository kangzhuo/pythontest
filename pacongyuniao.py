# -*- coding: UTF-8 -*-

import os
import time
import urllib
import urllib2
import re


# reload(sys)
# sys.setdefaultencoding('gbk')

def scan():
    url = 'http://www.jadebird-kg.org/New/Index/1?fathId=6'
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    page = response.read().decode('utf-8')
    pattern = re.compile('<span>(.*?)</span>',re.S)
    items = re.findall(pattern,page)
    for item in items:
        if '2017' in item or '2016' in item:
            url = 'http://sms.smspaas.com/mt.php?appId=107&modeId=200045&vars=&mobile=18858100583&sign=1888a85441bfe89f0abb0e530c8aea16'
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read().decode('utf-8')
            print item

if __name__=='__main__':
    while True:
        scan()
        time.sleep(3600*12)