# coding=utf-8
# using python 2.7

import time
from splinter import Browser


def main():
    # 先读取用户名和密码
    infile = open("user.txt", "r")
    username = infile.readline()
    password = infile.readline()
    infile.close()
    url = "https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=syllabus&appName=学生选课系统" + \
          "&redirectUrl=http://elective.pku.edu.cn:80/elective2008/agent4Iaaa.jsp/../ssoLogin.do"
    browser = Browser('firefox')
    browser.visit(url)
    time.sleep(3)
    browser.find_by_id('user_name').fill(username)
    browser.find_by_id('password').fill(password)
    browser.find_by_id('submit_button').click()
    time.sleep(8)

    browser.quit()

if __name__ == '__main__':
    main()
