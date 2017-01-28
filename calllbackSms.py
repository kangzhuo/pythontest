# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys
import json

#iAll = 0
#iSuccess = 0
#iFail = 0
#iExcpt = 0
#iMaxTime = 0
#iAllTime = 0

mutex = threading.Lock()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(smsId, status, mobile, sendTime):
    url = 'http://121.41.36.93:8191/callback/test.php'

    #m2 = hashlib.md5()
    #m2.update(appKey + appId + mobile) #key + app_id + tel
    #sign = m2.hexdigest()
    data = [{"smsId":smsId, "status":status, "mobile":mobile, "sendTime":sendTime}]
    in_json = json.dumps(data)

    #global mutex, iAll, iSuccess, iFail, iExcpt, iMaxTime, iAllTime
    try:
        #logging.debug(getUrl)
        logging.info('req:' + url)
        req = urllib2.Request(url, in_json)
        res = urllib2.urlopen(req).read()
        logging.info('resp:' + res)
        #start = int(round(time.time() * 1000))
        #res = urllib2.urlopen(req).read()
        #end = int(round(time.time() * 1000))
        #after = end - start
        #logging.debug('运行时间:' + str(after) + "-结果:" + res)
        #if '\"code\":0,' in res:
        #    if mutex.acquire():
        #        iAll += 1
        #        iSuccess += 1
        #        if iMaxTime < after:
        #            iMaxTime = after
        #        iAllTime += after
        #    mutex.release()
        #else:
        #    if mutex.acquire():
        #        iAll += 1
        #        iFail += 1
        #        iAllTime += after
        #    mutex.release()
    except Exception,ex:
        logging.error('Exception%s:%s\n'%(Exception,ex))
        pass

if __name__=='__main__':
    smsId = ''
    status = '2'
    mobile = '18858100583'
    sendTime = ''
    if len(sys.argv[1]) > 0:
        smsId = sys.argv[1]
    if len(sys.argv[2]) > 0:
        status = sys.argv[2]
    if len(sys.argv[3]) > 0:
        mobile = sys.argv[3]

    test_http (smsId, status, mobile, sendTime)

#    while i < sys.argv[1]:
#        while threading.activeCount() > 4000:
#            i = i
        # test_http('17','e341bacf6d','111168','18858100583','')
#        tel = '1885810058' + str(i)
#        threading.Thread(target = test_http, args = ('17','e341bacf6d','111168',tel,'')).start()
#        i = i + 1
#
#    while True:
#        logging.debug('当前活跃线程数:' + str(threading.activeCount()))
#        if threading.activeCount() < 2:
#            break
#        time.sleep(1)
#    logging.debug('执行完毕, 总数量:' + str(iAll) + ', 成功数量:' + str(iSuccess) + ", 失败数量:" + str(iFail) + ", 异常数量:" + str(iExcpt))
#    logging.debug('最大耗时:' + str(iMaxTime) + ', 平均耗时:' + str(float(iAllTime)/float(i+1)))
    input('Finished scanning.')
    sys.exit(0)