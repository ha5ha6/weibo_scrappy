#-*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re

driver=webdriver.Chrome()
driver.get("https://passport.weibo.cn/signin/login")
time.sleep(3)

print(driver.current_url)

#your weibo id and password
email='abc@efg.jp'
password='abcdef'
userId='abcde'

driver.find_element_by_id("loginName").send_keys(email)
driver.find_element_by_id("loginPassword").send_keys(password)
driver.find_element_by_id("loginAction").click()

cookies = driver.get_cookies()
cookie_list = []
for dict in cookies:
    cookie = dict['name'] + '=' + dict['value']
    cookie_list.append(cookie)
cookie = ';'.join(cookie_list)
print (cookie)
#driver.close()

time.sleep(20)
driver.get('http://weibo.cn/' + userId)

print('user info')

# show userid
print('---------------------')
print('user id:' + userId)
pageList = driver.find_element_by_xpath("//div[@class='pa']")
print(pageList.text)
pattern = r"\d+\d*"
pageArr = re.findall(pattern, pageList.text)
totalPages = pageArr[1]
print(totalPages)
print('---------------------')

pageNum = 1
numInCurPage = 1
curNum = 0
contentPath = "//div[@class='c'][{0}]"
while(pageNum <= 705):
#while(pageNum <= int(totalPages)):
    try:
        contentUrl = "http://weibo.cn/2178816443/profile?page=" + str(pageNum)
        #contentUrl = "http://weibo.cn/" + userId + "?page=" + str(pageNum)
        driver.get(contentUrl)
        content = driver.find_element_by_xpath(contentPath.format(numInCurPage)).text
        #print("\n" + content)
        if "设置:皮肤.图片.条数.隐私" not in content:
            numInCurPage += 1
            curNum += 1
            with open("weibocontent.txt", "a") as file:
                file.write(str(curNum) + '\r\n' + content + '\r\n\r\n')
        else:
            pageNum += 1
            numInCurPage = 1
            time.sleep(20)
    except Exception as e:
        print("curNum:" + str(curNum))
        print(e)
    finally:
        pass
        
print("Load weibo content finished!")
