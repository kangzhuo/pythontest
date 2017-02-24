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

global iFail, iSucc, iOther

mutex = threading.Lock()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(smsId, status, mobile, sendTime):
    global iFail, iSucc, iOther

    url = 'http://121.41.36.93:8191/callback/hs.php'

    #m2 = hashlib.md5()
    #m2.update(appKey + appId + mobile) #key + app_id + tel
    #sign = m2.hexdigest()
    data = {"Dest_Id":"1", "Msg_Id":smsId, "Status":status, "Mobile":mobile, "sendTime":sendTime}
    in_json = json.dumps(data)

    #global mutex, iAll, iSuccess, iFail, iExcpt, iMaxTime, iAllTime
    try:
        #logging.debug(getUrl)
        print 'req:' + url
        logging.info('req:' + url + '|' + in_json)
        req = urllib2.Request(url, in_json)
        res = urllib2.urlopen(req).read()
        logging.info('resp:' + res)
        if 'FAIL' in res:
            iFail += 1
        elif 'SUCCESS' in res:
            iSucc += 1
        else:
            iOther += 1

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

    global iFail, iSucc, iOther

    iFail = 0
    iSucc = 0
    iOther = 0

    file_object = open('kk')
    try:
        lines = file_object.readlines()
        for line in lines:
            sendTime = line[0:19]
            smsId = line[line.index('backOrder=')+10:line.index(',reportCode')]
            status = line[line.index('reportCode=')+11:line.index(',mobile')]
            mobile = line[line.index('mobile=')+7:line.index('mobile=')+18]

            print line
            print 'sendTime:' + sendTime + 'smsId:' + smsId + 'status:' + status + 'mobile:' + mobile

            test_http (smsId, status, mobile, sendTime)
    finally:
        file_object.close()
        print iFail
        print iSucc
        print iOther

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