# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys

iAll = 0
iSuccess = 0
iFail = 0
iExcpt = 0
iMaxTime = 0
iAllTime = 0

mutex = threading.Lock()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(appId, appKey, modeId, mobile, vars):
    # url = 'http://sms.smspaas.com/mt.php'
    url = 'http://115.238.54.178:8091/mt.php'

    m2 = hashlib.md5()
    m2.update(appKey + appId + mobile) #key + app_id + tel
    sign = m2.hexdigest()

    values = {'appId':appId, 'modeId':modeId, 'vars':vars, 'mobile':mobile, 'sign':sign}

    getUrl = url + '?appId=' + appId + '&modeId=' + modeId + '&vars=' + vars + '&mobile=' + mobile + '&sign=' + sign
    global mutex, iAll, iSuccess, iFail, iExcpt, iMaxTime, iAllTime
    try:
        logging.debug(getUrl)
        req = urllib2.Request(getUrl, '')
        start = int(round(time.time() * 1000))
        res = urllib2.urlopen(req).read()
        end = int(round(time.time() * 1000))
        after = end - start
        logging.debug('运行时间:' + str(after) + "-结果:" + res)
        if '\"code\":0,' in res:
            if mutex.acquire():
                iAll += 1
                iSuccess += 1
                if iMaxTime < after:
                    iMaxTime = after
                iAllTime += after
            mutex.release()
        else:
            if mutex.acquire():
                iAll += 1
                iFail += 1
                iAllTime += after
            mutex.release()
    except Exception,ex:
        logging.error('Exception%s:%s\n'%(Exception,ex))
        if mutex.acquire():
            iAll += 1
            iExcpt += 1
        mutex.release()
        pass

if __name__=='__main__':

    tel = '18858100583'
    threading.Thread(target = test_http, args = ('17','bd2b5922d3','1154',tel,'')).start()

    input('Finished scanning.')
    sys.exit(0)