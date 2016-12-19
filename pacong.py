# -*- coding: UTF-8 -*-

import os
import time
from selenium import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

# reload(sys)
# sys.setdefaultencoding('gbk')

def connect():
    chromedriver = "./chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    #profile = webdriver.FirefoxProfile()
    #profile.set_preference("network.proxy.type", 1)
    #profile.set_preference("network.proxy.http", "localhost")
    #profile.set_preference("network.proxy.http_port", 9638)
    #profile.set_preference("network.proxy.no_proxies_on", "")
    #profile.update_preferences()
    opts = Options()
    opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36")
    chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--proxy-server=http://%s' % proxy)

    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
    # browser = webdriver.Firefox() # Get local session of firefox
    driver.get("http://hd.hdc.zj.chinamobile.com/html/src/page/index.html?open_id=1234")
    # driver.get("http://ip.chinaz.com/getip.aspx") # Load page
    # assert '天猫tmall.com--上天猫，就够了' in driver.title
    while True :
        try :
            # elem = driver.find_element_by_xpath("//span[contains(text(),'即将开')]//u").text # Find the query box
            elem = driver.findElements(By.tagName("span")).text
            print elem
        except NoSuchElementException:
            time.sleep(1)
            pass
    # elem = driver.find_element_by_class("fr red") # Find the query box
    # elem.clear()
    # elem.send_keys("中国移动" + Keys.RETURN)

    # assert "No results found." not in driver.page_source
    # time.sleep(2) # Let the page load, will be added to the API
    # try:
    #    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
    # except NoSuchElementException:
    #    assert 0, "can't find seleniumhq"
    driver.close()


if __name__=='__main__':
    # 扫描ip
    connect()