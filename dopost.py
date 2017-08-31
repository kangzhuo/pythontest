# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys
from sys import argv
import json

mutex = threading.Lock()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='dopost.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http():
    # url = 'http://sms.smspaas.com/mt.php'
    url = 'http://10.78.200.72:8001/MCP/MCPNewController/queryTmallProduct'
    channelId = '10164'
    timestamp = '20170818221100'
    appSecret = '27xnt83n6gsc9dujd9nzl1'
    m2 = hashlib.md5()
    m2.update(channelId + timestamp + appSecret) #key + app_id + tel
    sign = m2.hexdigest()
    param = {'channelId':channelId,'timestamp':timestamp,'sign':sign}
    in_json = json.dumps(param)

    url1 = 'http://imcdinterface2.zj.chinamobile.com/MCP/MCPNewController/queryTmallProduct?channelId=10164&timestamp=' + timestamp + '&sign=' + sign

    # values = {"sendId":148906114006866700,"status":2,"sendTime":"2017-03-09 20:05:43","mobile":"18650092137"}

    # getUrl = url + '?appId=' + appId + '&modeId=' + modeId + '&vars=' + vars + '&mobile=' + mobile + '&sign=' + sign
    #try:
    # data = urllib.urlencode(values)
    print url1
    req = urllib2.Request(url1)
    res = urllib2.urlopen(req)
    print res.read()

    #except Exception,ex:
    #    logging.error('Exception%s:%s\n'%(Exception,ex))
    #   pass

if __name__=='__main__':
    test_http()
    input('Finished scanning.')
    sys.exit(0)



