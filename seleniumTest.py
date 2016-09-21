# -*- coding: gbk -*-
# 刷淘宝页面
import os
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

reload(sys)
sys.setdefaultencoding('gbk')

arrIp = [
    "113.85.207.125:3128","222.76.181.122:8118","220.248.230.217:3128","58.67.159.50:80","60.209.188.221:9999",
    "27.158.140.81:9999","14.208.90.104:3128","121.10.234.15:3128","112.91.208.78:9999","222.174.72.122:9999"
        ]

def connect(proxy,i):
    flog = open('log','w+')
    flog.write('%s\n'%proxy)
    flog.close()
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    #profile = webdriver.FirefoxProfile()
    #profile.set_preference("network.proxy.type", 1)
    #profile.set_preference("network.proxy.http", "localhost")
    #profile.set_preference("network.proxy.http_port", 9638)
    #profile.set_preference("network.proxy.no_proxies_on", "")
    #profile.update_preferences()
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36%d"%i)
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--proxy-server=http://%s' % proxy)

    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    # browser = webdriver.Firefox() # Get local session of firefox
    driver.get("https://www.tmall.com")
    # driver.get("http://ip.chinaz.com/getip.aspx") # Load page
    # assert '天猫tmall.com--上天猫，就够了' in driver.title
    try:
        elem = driver.find_element_by_name("q") # Find the query box
        elem.clear()
        elem.send_keys("中国移动" + Keys.RETURN)
        f = open('proxy','w+')
        f.write('%s\n'%proxy)
        f.close()
        # assert "No results found." not in driver.page_source
        time.sleep(2) # Let the page load, will be added to the API
        # try:
        #    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
        # except NoSuchElementException:
        #    assert 0, "can't find seleniumhq"
        driver.close()
    except NoSuchElementException:
        driver.close()
        pass


if __name__=='__main__':
    # 扫描ip
    i = 1
    for useIp in arrIp:
        i += 1
        connect(useIp, i)
    input('Finished scanning.')