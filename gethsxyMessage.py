# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='hsyx.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http():
    url = 'http://182.92.224.167:8888/statusApi.aspx?userid=377&account=santiyx&password=st201608231156&action=query'

    try:
        while True:
            logging.info(url)
            req = urllib2.Request(url, '')
            res = urllib2.urlopen(req).read()
            logging.info('结果:' + res)
            if len(res) > 0:
                print len(res)
            else:
                break

    except Exception,ex:
        logging.error('Exception%s:%s\n'%(Exception,ex))
        pass

if __name__=='__main__':
    test_http()