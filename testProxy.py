# -*- coding: utf8 -*-
# nohup python pyScnPort.py > 1.log 2>&1 &
# 测试代理
from threading import Thread, activeCount
import socket
import urllib
import string
import time

arrIp = []

# 测试ip和端口是否开放
def test_port(dst,port,f,flog):
    url = 'http://ip.chinaz.com/getip.aspx'
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.settimeout(5)
    try:
        flog.write('test:%s:%s\n'%(dst,port))
        flog.flush()
        #t0=time.time()
        indicator = cli_sock.connect_ex((dst,string.atoi(port)))
        #t1=time.time()
        cli_sock.settimeout(None)
        if indicator == 0:
            flog.write('connect:%s:%s\n'%(dst,port))
            flog.flush()
            proxy_host = 'http://%s:%s'%(dst,port)
            proxy_temp = {"http":proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
            if res.find("ip:") > 0:
                flog.write(res)
                flog.flush()
                f.write('%s:%s\n'%(dst,port))
                f.flush()
        #print t1-t0
        cli_sock.close()
    except Exception,ex:
        flog.write('Exception%s:%s\n'%(Exception,ex))
        flog.flush()
        cli_sock.settimeout(None)
        pass

def getIp(useIp):
    arr = useIp.split(':')
    return arr[0]

def getPort(useIp):
    arr = useIp.split(':')
    return arr[1]


if __name__=='__main__':
    f = open('proxy','w+')
    flog = open('log','w+')
    # 扫描ip
    for useIp in arrIp:
        dstIp = getIp(useIp)
        dstPort = getPort(useIp)
        Thread(target = test_port, args = (dstIp, dstPort, f, flog)).start()

    while True:
        if activeCount() <= 2:
            break

    f.close()
    flog.close()
    input('Finished scanning.')