# coding=utf-8
# using python 2.7


class Links:
    def __init__(self):
        print("init electiveLinks")

    @staticmethod
    def login():
        link = "https://iaaa.pku.edu.cn/iaaa/oauth.jsp?appID=syllabus&appName=学生选课系统" + \
               "&redirectUrl=http://elective.pku.edu.cn:80/elective2008/agent4Iaaa.jsp/../ssoLogin.do"
        return link

    @staticmethod
    def xuankejihua():
        return "/elective2008/edu/pku/stu/elective/controller/electivePlan/ElectivePlanController.jpf"

    @staticmethod
    def yuxuan():
        return "/elective2008/edu/pku/stu/elective/controller/electiveWork/ElectiveWorkController.jpf"

    @staticmethod
    def xuankejieguo():
        return "/elective2008/edu/pku/stu/elective/controller/electiveWork/showResults.do"
