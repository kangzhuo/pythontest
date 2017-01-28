# -*- coding:utf-8 -*-

import os
import commands

(status, output) = commands.getstatusoutput('/root/moni/moni_grace.sh')
ar=output.split('\n')
print ar

from binascii import  unhexlify as unh

output = open('faillog', 'a')

def sb2db(ia):
    tmpa=[]
    xrctBytes=[]
    for i in range(len(ia)):
        tmpa.append(ia[i])
        if i%2==1:
            xrctBytes.append(''.join(tmpa))
            tmpa=[]
    return xrctBytes

writelist=[]
for n in range(len(ar)):
    a=ar[n]
    tmpa=[]
    newrstBytes=sb2db(a)
    print '----'
    cellno=unh(''.join(newrstBytes[42:55]))
    print 'cellno:',cellno
    msgct=newrstBytes[65:125]
    statusrstBytes=msgct
    reason=unh(''.join(statusrstBytes[8:15]))
    print 'reason:',reason
    tsraw=unh(''.join(statusrstBytes[15:25]))
    tsrenew=tsraw[2:6]+'_'+tsraw[6:8]+':'+tsraw[8:10]
    print 'timestamp:',tsrenew
    forwriteline=tsrenew+','+cellno[2:]+','+reason
    if len(forwriteline)>10 and reason!='DELIVRD':
        writelist.append(forwriteline)
    output.write(forwriteline+'\n')

output.close()

import requests,datetime,time,hashlib
from urllib import quote

if len(writelist)>0:
    x_url='http://183.136.236.79:19090/warn'
    x_content='\\n'.join(writelist)
    print 'content:',x_content
    x_r_content='{"msg":"流量营销蕾丝监控:\\n'+x_content+'","to":"轻鸟养成","channel":"yfcz"}'
    print 'x_r_content:',x_r_content
    x_map=quote(x_r_content)
    x_key='2a7f5f07'
    x_keysec='24132553a86ed6ca6c54afdf'
    dtime = datetime.datetime.now()
    x_ts=str(int(time.mktime(dtime.timetuple())))
    m2 = hashlib.md5()
    m2.update(x_map+x_ts+x_keysec)
    x_sign=m2.hexdigest()
    print 'js:',x_map
    print 'ts:',x_ts
    print 'sec:',x_keysec
    print 'readyforsig:',x_map+x_ts+x_keysec
    print 'sign:',x_sign

    r=requests.get(x_url,params={
        'ts':x_ts,
        'js':x_map,
        'appkey':x_key,
        'sign':x_sign
    })
    print r.url
    print r.status_code
    print r.text