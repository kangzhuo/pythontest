# -*- coding: utf8 -*-
# 爬代理
from threading import Thread, activeCount
import socket
import urllib
import time

arrIp = ["58.14.0.0",
         "58.30.0.0",
         "58.66.0.0",
         "58.68.128.0",
         "58.82.0.0",
         "58.87.64.0",
         "58.99.128.0",
         "58.116.0.0",
         "58.128.0.0",
         "58.144.0.0",
         "58.154.0.0",
         "58.192.0.0",
         "58.240.0.0",
         "59.32.0.0",
         "59.107.0.0",
         "59.151.0.0",
         "59.155.0.0",
         "59.172.0.0",
         "59.191.0.0"]

# 测试ip和端口是否开放
def test_port(dst,port, f, flog):
    url = 'http://ip.chinaz.com/getip.aspx'
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.settimeout(5)
    try:

        #t0=time.time()
        indicator = cli_sock.connect_ex((dst, port))
        #t1=time.time()
        cli_sock.settimeout(None)
        if indicator == 0:
            flog.write('%s:%s\n'%(dst,port))
            flog.flush()
            proxy_host = 'http://%s:%s'%(dst,port)
            proxy_temp = {"http":proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
            if res.find("ip:") >= 0:
                f.write('%s:%s\n'%(dst,port))
                f.flush()
        #print t1-t0
        cli_sock.close()
    except Exception,ex:
        flog.write('Exception%s:%s\n'%(Exception,ex))
        flog.flush()
        cli_sock.settimeout(None)
        cli_sock.close()
        pass

def getIp(useIp):
    ret = []
    arr = useIp.split('.')
    str = '%s.%s.'%(arr[0],arr[1])
    for i in range(1,254):
        for j in range(1,254):
            strRet = '%s%s.%s'%(str,i,j)
            ret = ret + [strRet]
    return ret


if __name__=='__main__':
    # 扫描ip
    f = open('proxy','w+')
    flog = open('log','w+')
    for useIp in arrIp:
        dstIps = getIp(useIp)
        for dstIp in dstIps:
            flog.write('%s %s\n'%(dstIp,time.strftime('%X', time.localtime())))
            flog.flush()
            i = 100
            while i < 10000:
                while activeCount() > 500:
                    i = i

                Thread(target = test_port, args = (dstIp, i, f, flog)).start()
                i = i + 1

    while True:
        if activeCount() <= 2:
            break

    f.close()
    flog.close()
    input('Finished scanning.')