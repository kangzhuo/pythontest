# -*- coding: utf8 -*-
# 爬代理
from threading import Thread, activeCount
import urllib
import urllib2
import hashlib

# 测试ip和端口是否开放
def test_http(flog):
    url = 'http://121.41.36.93:8091/mt.php'
    appId = '13'
    appKey = 'e2c7107176'
    modeId = '111168'
    mobile = '18858100583'
    vars = '123|456'
    m2 = hashlib.md5()
    m2.update(appKey + appId + mobile) #key + app_id + tel
    sign = m2.hexdigest()

    values = {'appId':appId, 'modeId':modeId, 'vars':vars, 'mobile':mobile, 'sign':sign}
    try:
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        res = urllib2.urlopen(req).read()
        flog.write(res)
        flog.write('\n')
        flog.flush()
    except Exception,ex:
        flog.write('Exception%s:%s\n'%(Exception,ex))
        flog.flush()
        pass

if __name__=='__main__':
    # 扫描ip
    flog = open('1.log','w+')
    i = 0
    while i < 1:
        while activeCount() > 2000:
            i = i
        Thread(target = test_http, args = (flog,)).start()
        i = i + 1

    while True:
        if activeCount() <= 2:
            break

    flog.close()
    input('Finished scanning.')