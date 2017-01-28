
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import re
import MySQLdb as mysql

db = mysql.connect(user="sdk",passwd="sdk-ksl_ds12dss",db="sdk",host="rdsb849k9kv0wz12281f.mysql.rds.aliyuncs.com")

db.autocommit(True)
cur = db.cursor()
cur.execute('set names utf8')

def querydb(m):
    sql = 'select * from access_log where request like %s'% m
    print sql
    result = cur.execute(sql)
    return result


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.process(1)

    def process(self,type):

        content="hello world"
        if '?' in self.path:
                path = self.path.split('?')[0]
        else:
                path = self.path
        path = path.replace('/','')
        print path
        path = '\'%'+path+'%\''
        res = querydb(path)
        print res
        if type==1:
            enc="UTF-8"
            if res!=0:
                self.send_response(200)
                content = "Success"
            else:
                self.send_response(0)
                content = "Fail"
            content=content.encode(enc)
            self.send_header("Content-type","text/html; charset=%s" % enc)
            self.send_header("Content-Length",str(len(content)))
            self.end_headers()
            self.wfile.write(content)

server=HTTPServer(('',8100), MyRequestHandler)
print'started httpserver...'
server.serve_forever()
