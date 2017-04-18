# coding=utf-8
# using python 2.7

import time
from splinter import Browser
from pkulinks import *


def main():
    # 先读取用户名和密码
    infile = open("user.txt", "r")
    username = infile.readline()
    password = infile.readline()
    infile.close()
    url = Links.login()
    browser = Browser('firefox')
    browser.visit(url)
    # time.sleep(3)
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
        if cmd.startswith("get "):
            print "begin catching information"
        cmd = raw_input()
    browser.quit()

if __name__ == '__main__':
    main()
