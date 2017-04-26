# coding=utf-8
# using python 2.7

import time
from splinter import Browser
from pkulinks import *
from PkuGet import PkuGet
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    # 先读取用户名和密码
    infile = open("user.txt", "r")
    username = str(infile.readline())
    password = str(infile.readline())
    print "username", username, type(username)
    infile.close()
    url = Links.login()
    browser = Browser('firefox')
    browser.visit(url)
    time.sleep(1)
    browser.find_by_id('user_name').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('submit_button').click()
    time.sleep(1)
    browser.click_link_by_href(Links.xuankejieguo())
    # time.sleep(8)
    # 通过命令行来控制抓取
    print "ready to catch information!"
    cmd = raw_input()
    while cmd != "exit":
        strlst = cmd.split(' ')
        cmd0 = strlst[0]
        if cmd0 == "get":
            print "begin catching information"
            pkuget = PkuGet(browser, 3)
            if pkuget.state == 1:
                pkuget.getinfo(strlst)
        cmd = raw_input()
    browser.quit()

if __name__ == '__main__':
    main()
