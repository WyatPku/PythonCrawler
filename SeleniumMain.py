# coding=utf-8
# using python 2.7


import time
from selenium import webdriver
from pkulinks import *
from SePkuGet import PkuGet
from selenium import common
from selenium.webdriver.common.keys import Keys


# 先读取用户名和密码
infile = open("user.txt", "r")
username = str(infile.readline())
password = str(infile.readline())
infile.close()
print "使用用户", username
#打开浏览器
driver = webdriver.Firefox()
url = Links.login()
driver.get(url)
# driver.save_screenshot('login.png')
driver.find_element_by_id("user_name").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("submit_button").click()
# 通过命令行来控制抓取
print "ready to catch information!"
cmd = raw_input()
while cmd != "exit":
    strlst = cmd.split(' ')
    cmd0 = strlst[0]
    if cmd0 == "get":
        print "begin catching information"
        pkuget = PkuGet(driver, 5)
        if pkuget.state == 1:
            pkuget.getinfo(strlst)
    cmd = raw_input()



driver.fin
time.sleep(5)
driver.close()
driver.quit()

