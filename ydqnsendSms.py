# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys

tels = ['18858100583']

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(appId, appKey, modeId, mobile):
    url = 'http://send.smspaas.zj.chinamobile.com/mt.php'
    #url = 'https://sms.smspaas.com/mt.php'
    m2 = hashlib.md5()
    m2.update(appKey + appId + mobile) #key + app_id + tel
    sign = m2.hexdigest()

    # values = {'appId':appId, 'modeId':modeId, 'vars':vars, 'mobile':mobile, 'sign':sign}

    param = {'appId':appId,'modeId':modeId,'vars':'地方[http://www.baidu.com]','mobile':mobile,'sign':sign}
    param = urllib.urlencode(param)
    print url + '?' + param
    getUrl = url + '?appId=' + appId + '&modeId=' + modeId + '&vars=' + '&mobile=' + mobile + '&sign=' + sign
    try:
        req = urllib2.Request(url, param)
        res = urllib2.urlopen(req).read()
        logging.debug('结果:' + res)
    except Exception,ex:
        logging.error('Exception%s:%s\n'%(Exception,ex))
        pass

if __name__=='__main__':
    for tel in tels:
        # test_http('17', 'c5f4abbb64', '205546', '18858100583')
        test_http('10198', '3764daa1e6', '200816', '13588143705') #appid appkey modeid tel 13605808369 13505715513 18405815660
    time.sleep(15)
    input('Finished scanning.')
    sys.exit(0)