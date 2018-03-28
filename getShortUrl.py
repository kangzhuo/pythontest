# -*- coding: utf8 -*-

import logging
import time
import urllib
import urllib2
import sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='short.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(url):
    # url = 'http://sms.smspaas.com/mt.php'
    url1 = 'http://api.t.sina.com.cn/short_url/shorten.xml?source=3271760578&url_long=' + url
    logging.info(url1)
    req = urllib2.Request(url1)
    res = urllib2.urlopen(req)
    logging.info(res.read())
    logging.info('\n')

    #except Exception,ex:
    #    logging.error('Exception%s:%s\n'%(Exception,ex))
    #   pass

if __name__=='__main__':
    for i in range(1, 10000) :
        url = 'http://www.smspaas.com?a=' + str(i)
        test_http(url)
    input('Finished scanning.')
    sys.exit(0)



