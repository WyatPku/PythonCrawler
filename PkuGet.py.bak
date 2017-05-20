# coding=utf-8
# using python 2.7

import time
import xlwt
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
                time.sleep(self.delay)
                pagelist = self.browser.find_by_name("netui_row")
                pagenum = len(pagelist.text.splitlines())
                print "find pagelist :", pagenum
            if strlst[1] == "公选课":
                ifrequirej = False
                if len(strlst) > 2 and strlst[2] == "more":
                    ifrequirej = True
                glocount = 0
                print "creating excel book"
                workbook = xlwt.Workbook()
                basic = workbook.add_sheet('basic', cell_overwrite_ok=True)
                basic.write(0, 0, u"本地序号")
                basic.write(0, 1, u"课程号")
                basic.write(0, 2, u"课程名")
                basic.write(0, 3, u"课程类别")
                basic.write(0, 4, u"学分")
                basic.write(0, 5, u"教师")
                basic.write(0, 6, u"班号")
                basic.write(0, 7, u"开课单位")
                basic.write(0, 8, u"专业")
                basic.write(0, 9, u"开课年级")
                basic.write(0, 10, u"上课时间及地点")
                basic.write(0, 11, u"备注")
                print "getting pub_choice"
                self.browser.find_by_id("pub_choice").check()
                self.browser.execute_script('''document.getElementById("myForm").submit()''')
                nowpage = int(1)
                pagenum = 1
                while nowpage <= pagenum:
                    time.sleep(self.delay)
                    pagelist = self.browser.find_by_name("netui_row").first
                    optionlist = pagelist.find_by_tag("option")
                    valuelist = [str(i.value) for i in optionlist]
                    print valuelist
                    # print len(optionlist), optionlist
                    # pagenum = len(pagelist.text.splitlines())
                    pagenum = len(optionlist)
                    print "find page :", pagenum
                    # catching information
                    tbodylist = self.browser.find_by_tag("tbody")
                    trlist = tbodylist[4].find_by_tag("tr")
                    classlen = len(trlist) - 3
                    print "found", classlen, "on this page"
                    classElement = [trlist[i] for i in range(1, classlen + 1)]  # 这些都是课程的数据了
                    for i in range(0, classlen):
                        glocount = glocount + 1
                        info = classElement[i].find_by_tag("td")  # 获得每一个信息
                        kechenghao_a = info[0].find_by_tag("a")[0]
                        kechenghao_href = kechenghao_a["href"]
                        kechenghao = str(kechenghao_a.text)
                        kechengming = str(info[1].text)
                        kechengleibie = str(info[2].text)
                        xuefen = str(info[3].text)
                        jiaoshi = str(info[4].text)
                        banhao = str(info[5].text)
                        kaikedanwei = str(info[6].text)
                        zhuanye = str(info[7].text)
                        kaikenianji = str(info[8].text)
                        shangkeshijianjijiaoshi = str(info[9].text)
                        beizhu = str(info[10].text)
                        basic.write(glocount, 0, glocount)
                        basic.write(glocount, 1, kechenghao.decode("utf-8"))
                        basic.write(glocount, 2, kechengming.decode("utf-8"))
                        basic.write(glocount, 3, kechengleibie.decode("utf-8"))
                        basic.write(glocount, 4, xuefen.decode("utf-8"))
                        basic.write(glocount, 5, jiaoshi.decode("utf-8"))
                        basic.write(glocount, 6, banhao.decode("utf-8"))
                        basic.write(glocount, 7, kaikedanwei.decode("utf-8"))
                        basic.write(glocount, 8, zhuanye.decode("utf-8"))
                        basic.write(glocount, 9, kaikenianji.decode("utf-8"))
                        basic.write(glocount, 10, shangkeshijianjijiaoshi.decode("utf-8"))
                        basic.write(glocount, 11, beizhu.decode("utf-8"))
                        print "finished basic info catch of", kechengming
                        if ifrequirej:
                            kechenghao_a.click()
                            time.sleep(self.delay / 2)
                            # print self.browser.title
                            outputfile = open("gongxuanke/" + str(glocount) + ".htm", 'w')
                            self.browser.windows.current = self.browser.windows[1]
                            outputfile.write(str(self.browser.html).replace(
                                """<link href="/elective2008/resources/css/style.css" rel="stylesheet" type="text/css">""",
                                """<meta charset="utf-8"><link href="style.css" rel="stylesheet" type="text/css">"""))
                            outputfile.close()
                            self.browser.windows[1].close()
                            time.sleep(1)
                            # print self.browser.title
                            print "finished more info catch"
                        # while True:
                        # exec raw_input(">>>")
                    # end catching
                    if nowpage < pagenum:
                        print "going to page", nowpage, valuelist[nowpage]
                        pagelist.select(valuelist[nowpage])
                    nowpage = nowpage + 1
                workbook.save(u"公选课.xls")
        else:
            print "you want to find what?"


