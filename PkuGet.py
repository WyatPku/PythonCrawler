# coding=utf-8
# using python 2.7

import time
from splinter import Browser
from pkulinks import *


class PkuGet:
    def __init__(self, browser, delay=1):
        self.browser = browser  # type: Browser
        self.delay = delay
        print("get going")
        self.browser.click_link_by_href(Links.xuankejihua())
        time.sleep(delay)
        self.browser.click_link_by_href("../courseQuery/CourseQueryController.jpf");
        time.sleep(delay)
        self.state = 1  # 判断一下如果页面错误，返回0，现在先这样写
        print "initial finished"

    def getinfo(self, strlst):
        print "getting information!"
        if len(strlst) > 1:
            if strlst[1] == "培养方案":
                print "这里面没有东西啊？？？"
                self.browser.find_by_id("education_plan_bk").click()
            if strlst[1] == "专业课":
                print "getting speciality"
                self.browser.find_by_id("speciality").click()
                self.browser.execute_script('''document.getElementById("myForm").submit()''')
                time.sleep(0.5)
                pagelist = self.browser.find_by_name("netui_row")
                pagenum = len(pagelist.text.splitlines())
                print "find pagelist :", pagenum
            if strlst[1] == "公选课":
                print "getting pub_choice"
                self.browser.find_by_id("pub_choice").click()
                self.browser.execute_script('''document.getElementById("myForm").submit()''')
                time.sleep(0.5)
                pagelist = self.browser.find_by_name("netui_row")
                pagenum = len(pagelist.text.splitlines())
                print "find pagelist :", pagenum
        else:
            print "you want to find what?"


