
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import re
import MySQLdb as mysql

db = mysql.connect(user="sms_backend",passwd="smscom_1qaz123409",db="sms_agent",host="rds1k3igl3nc1z0w186q.mysql.rds.aliyuncs.com")

db.autocommit(True)
cur = db.cursor()
cur.execute('set names utf8')

def querydb():
    sql = 'SELECT code_type,code_value from `sms_agent`.`sys_static_data` where `code_type` like "mode%"'
    print sql
    cur.execute(sql)
    result = cur.fetchall()
    return result

def insertdb(code, value):
    sql = 'insert into `sms_agent`.`tmp_data` values ("%s","%s")' % (code, value)
    print sql
    result = cur.execute(sql)
    return result

if __name__ == '__main__':
    qryRes = querydb()
    for i in range(len(qryRes)):
        codeType = qryRes[i][0]
        codeValue = qryRes[i][1]
        values = codeValue.split(',')
        for j in range(len(values)):
            value = values[j]
            insertdb(codeType, value)

