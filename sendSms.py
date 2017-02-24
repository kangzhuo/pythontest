# -*- coding: utf8 -*-

import threading
import logging
import time
import urllib
import urllib2
import hashlib
import sys

tels = []

var1 = '''【赛会通】您报名的活动，请于2月10日晚20:00在地铁5、10号线惠新西街南口B出口准时集合出发，请勿晚点.\n\
领队:纸小鸢·$$$$，收到请回复姓名以及人数，请带好保暖衣物和有效身份证件，报名不到者需A费用 ！车牌号京AT0001\n\
退订TD'''

var2 = '【赛会通】感谢参加2月11日《爱旅》红螺寺 祈福求缘一日游活动，请于2月11日早 08:15在宋家庄地铁站D口找蓝色爱旅旗帜签到集合 8:30 活动准时出发迟到不等 领队-剑星18810392873  车号：京B07390 提示：请自带午餐或下山后大家AA用餐，穿舒适的鞋子和服装 收到请给转发给您一起参加活动的朋友！退订TD'

var3 = '【赛会通】感谢参加2月11日红螺寺 祈福求缘一日游活动，请于2月11日早 08:15在宋家庄地铁站D口签到集合 8:30 活动准时出发迟到不等 领队-剑星18810392873  车号：京B07390 提示：请自带午餐或下山后大家AA用餐，穿舒适的鞋子和服装 收到请给转发给您一起参加活动的朋友！退订TD'

var4 = '【自游人】本周日马拉松早八点半中信银行红旗街支行集合。详情点击：http://t.cn/RJL4UVU 内容重要，请仔细阅读。退订TD'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='batch.log',
                    filemode='w')

# 测试ip和端口是否开放
def test_http(appId, appKey, modeId, mobile, vars):
    url = 'http://182.92.224.167:8888/statusApi.aspx'

    m2 = hashlib.md5()
    m2.update(appKey + appId + mobile) #key + app_id + tel
    sign = m2.hexdigest()

    values = {'appId':appId, 'modeId':modeId, 'vars':vars, 'mobile':mobile, 'sign':sign}

    getUrl = url + '?appId=' + appId + '&modeId=' + modeId + '&vars=' + urllib.quote(vars) + '&mobile=' + mobile + '&sign=' + sign
    try:
        req = urllib2.Request(getUrl, '')
        res = urllib2.urlopen(req).read()
        logging.debug('结果:' + res)
    except Exception,ex:
        logging.error('Exception%s:%s\n'%(Exception,ex))
        pass

if __name__=='__main__':
    for i in range(len(tels)):
        var = var3.replace('$$$$', tels[i])

        test_http('10131', 'a64860b233', '111282', tels[i], var2)
    input('Finished scanning.')
    sys.exit(0)