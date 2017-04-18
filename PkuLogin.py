# coding=utf-8
# using python 2.7

import urllib2


def pku_login():
    # request = urllib2.Request("http://wuyue98.cn/owncloud")
    # request = urllib2.Request("http://www.baidu.com")
    # request = urllib2.Request("http://elective.pku.edu.cn")
    request = urllib2.Request("https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=syllabus&appName=学生选课系统" +
                              "&redirectUrl=http://elective.pku.edu.cn:80/elective2008/agent4Iaaa.jsp/../ssoLogin.do")
    response = urllib2.urlopen(request)
    page = response.read()
    return page
