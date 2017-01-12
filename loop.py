#!/usr/bin/env python
#_*_coding:utf-8 _*_
import MySQLdb as mysql
import sys, os, re, time, pyinotify, base64
from user_agents import parse
import urllib2,urllib
import SimpleHTTPServer

db = mysql.connect(user="sdk",passwd="sdk-ksl_ds12dss",db="sdk",host="rdsb849k9kv0wz12281f.mysql.rds.aliyuncs.com")
db.autocommit(True)
cur = db.cursor()
cur.execute('set names utf8')

ip_re = r"?P<ip>[\d.]*"
date_re = r"?P<date>\d+"
month_re = r"?P<month>\w+"
year_re = r"?P<year>\d+"
log_time_re = r"?P<time>\S+"
method_re = r"?P<method>\S+"
request_re = r"?P<request>\S+"
status_re = r"?P<status>\d+"
bodyBytesSent_re = r"?P<bodyBytesSent>\d+"
refer_re = r"""?P<refer>
            [^\"]*
            """
userAgent_re = r"""?P<userAgent>
                 .*
                """
domainName_re =  r"?P<domainName>\S+"
domainName2_re =  r"?P<domainName2>\S+"
user_re =  r"?P<user>\S+"  
host_re =  r"?P<host>\S+"  
param_re =  r"?P<param>\S+"  
port_re =  r"?P<port>\S+"                 
net_re =  r"?P<net>\S+"  
netPro_re =  r"?P<netPro>\S+"  
url_re =  r"?P<url>.*"  
extra1_re =  r"?P<extra1>\S+"  
extra2_re =  r"?P<extra2>\S+"  
extra3_re =  r"?P<extra3>\S+"  
extra4_re =  r"?P<extra4>\S+"  

#p = re.compile(r"(%s)\ -\ -\ \[(%s)/(%s)/(%s)\:(%s)\ [\S]+\]\ \"(%s)?[\s]?(%s)?.*?\"\ (%s)\ (%s)\ \"(%s)\"\ \"(%s).*?\"" %( ip_re, date_re, month_re, year_re, log_time_re, method_re, request_re, status_re, bodyBytesSent_re, refer_re, userAgent_re ), re.VERBOSE)
p = re.compile(r"\"(%s)/(%s)/(%s)\:(%s)\ [\S]+\"\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ -\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" %(date_re, month_re, year_re, log_time_re, domainName_re, user_re, host_re, method_re, request_re, param_re, port_re, ip_re, net_re, netPro_re, userAgent_re, url_re, domainName2_re, status_re, bodyBytesSent_re, extra1_re, extra2_re, extra3_re, extra4_re), re.VERBOSE)
class ProcessTransientFile(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self,event):
        line = file.readline()
        if ".mms" in line:
        #if line:
           m = re.findall(p, line)
           print m
           intodb(m)
def parserequest(rqst):
    param = r"?P<param>.*"
    p = re.compile(r"abc\=(%s)" %param, re.VERBOSE)
    return re.findall(p, rqst)

def parsetime(date, month, year, log_time):
    time_str = '%s%s%s %s' %(year, month, date, log_time)
    timeStruct = time.strptime(time_str, '%Y%b%d %H:%M:%S')
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

def intodb(m):
    ip = m[0][11]
    date = m[0][0]
    month = m[0][1]
    year = m[0][2]
    log_time = m[0][3]
    method = m[0][7]
    request = m[0][8]
    param = m[0][9]
    status = m[0][17]
    bodyBytesSent = m[0][18]
    userAgent = m[0][14]
    userAgent = userAgent.replace('\"', '')
    #createTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) 
    param = param.replace('\"', '')
    paramList = param.split('&') 
    cellParam = paramList[0]
    dateTime = parsetime(date, month, year, log_time)
    req = parserequest(cellParam)
    if len(req):
        cellno = req[0]
        #cellno = base64.b64decode(cellno)
    else:
        cellno = ''
    print cellno
    user_agent = parse(userAgent)
    phoneModel = user_agent.device.family
    phoneInfo = str(user_agent)


    ordNo = '' + request
    ordNo = ordNo.replace('\/llg\/llg','')
    ordNo = ordNo.replace('\/l\/lg','')
    ordNo = ordNo.replace('.mms','')
    url = 'http://notify.liulianggo.com/feinengkami/notify?ordNo='+ordNo+'&status=success'
    result = urllib2.urlopen(url).read()
    i = 1
    while "0" != result and i <= 3:
        result = urllib2.urlopen(url).read()
        i = i + 1

    sql = 'insert access_log values ("%s",now(),"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s", "%s")' % (ip, dateTime, method, request, status, bodyBytesSent, param, userAgent, cellno, phoneModel, phoneInfo, result)
    print sql
    cur.execute(sql)


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename,'r')
    st_results = os.stat(filename)
    st_size = st_results[6]
    file.seek(st_size)

    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm)
    wm.watch_transient_file(filename, pyinotify.IN_MODIFY, ProcessTransientFile)
    notifier.loop()
