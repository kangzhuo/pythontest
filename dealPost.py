# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys
import datetime
import json

tels = ['18858100583']

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(appId, appKey, modeId, mobile):
    #url = 'http://send.smspaas.zj.chinamobile.com/mt.php'
    url = 'http://sms.liulianggo.com/mt.php'
    title = '测试1'
    name = '测试1'
    context = '[{"type":"text","content":"abcd"},{"type":"image","content":"http://content-management.b0.upaiyun.com/1509536824877.jpeg"},{"type":"video","content":"http://content-management.b0.upaiyun.com/1509536864275.mp4"}]'
    timestamp = str(time.mktime(datetime.datetime.now().timetuple()))[:-2]
    pp = (urllib.quote(appKey + appId + modeId + name + title + context + timestamp)).replace('/','%2F')
    print pp
    m2 = hashlib.md5()
    m2.update(pp) #key + app_id + tel
    sign = m2.hexdigest()

    # values = {'appId':appId, 'modeId':modeId, 'vars':vars, 'mobile':mobile, 'sign':sign}

    param = {"appId":appId,"modeId":modeId,"name":name,"title":title,"context":context,"timestamp":timestamp,"sign":sign}
    headers = {'Content-Type': 'application/json'}
    print param
    try:
        req = urllib2.Request(url, headers=headers, data=json.dumps(param))
        res = urllib2.urlopen(req).read()
        print '结果:' + res
    except Exception,ex:
        print 'Exception%s:%s\n'%(Exception,ex)
        pass

if __name__=='__main__':
    for tel in tels:
        test_http('17', 'c5f4abbb64', '200783', '18858100583') #appid appkey modeid tel
    time.sleep(15)
    input('Finished scanning.')
    sys.exit(0)