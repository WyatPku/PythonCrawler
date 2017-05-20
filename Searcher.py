#-*- coding:utf-8 -*-
import jieba
import xlrd
import TimeParser
import re

def multi(x,y):
    z=list(y)
    for i in range(len(x)):
        z[i]*=x
    return z

def dot(x,y):
    assert len(x)==len(y)
    z=list(x)
    for i in range(len(x)):
        z[i] = x[i] * y[i]
    return z

def add(x,y):
    assert len(x)==len(y)
    z=list(x)
    for i in range(len(x)):
        z[i]=x[i]+y[i]
    return z

class Searcher:
    def __init__(self):
        self.inf=1e20
        self.acceptRatio=0.7
        self.decreaseRate=0.6
        self.matchThreshold=1e-2
        self.courses=[]
        self.nCourses=0
        self.loaded=False

    def loadPublic(self,dct):
        print("加载公选课")
        workbook = xlrd.open_workbook("公选课.xls")
        table = workbook.sheet_by_name("basic")
        nCourses = table.nrows - 1
        self.nCourses += nCourses
        noCut = {"ID", "score","grade","time&location"}
        propName=["ID","name","type","score","teacher","classID","school","specialty","grade","time&location","note","description"]
        for i in range(1, nCourses + 1):
            c=dict()
            for j in range(1, table.ncols):
                prop = propName[j-1]
                content = table.cell(i, j).value
                c[prop] = content
                if (prop!="time&location"):
                    dct.write(content + '\n')
                if (prop not in noCut):
                    ls = jieba.cut(content)
                    for x in ls:
                        dct.write(x + '\n')
            times,other = TimeParser.parse(c["time&location"])
            for s in times+other:
                dct.write(s+'\n')
            self.courses.append(c)
        print("完成")

    def load(self):
        dct = open("courses.txt", encoding='utf-8', mode='w')
        self.loadPublic(dct)
        dct.close()
        jieba.load_userdict("courses.txt")
        self.loaded=True

    def parseEach(self,request):
        print("解析检索条件:",request)
        p = r'(?P<negAdv>(不)|(没)|(无)|(非)|(!))(?P<des>.*)'
        m = re.match(p, request)
        if m:
            type=-1
            des = m.group('des')
        else:
            type=1
            des=request
        times,others = TimeParser.parse(des)
        afterCut=[]
        for other in others:
            afterCut+=list(jieba.cut(other))
        return (type,times+afterCut)

    def search(self,requests):
        if not self.loaded:
            print("尚未加载课程，加载中")
            self.load()

        if ( self.nCourses ==0):
            print("没有课程")
            return None

        totV=[1.0]*self.nCourses
        for req in requests.split():
            type, des = self.parseEach(req)
            preV = [0.0] * self.nCourses
            for key in des:
                curV=self.searchForOneKey(key)
                preV=add(preV, curV)
            if (type==-1):
                for i in range(len(preV)):
                    if (preV[i]>self.matchThreshold):
                        preV[i]=0.0
                    else:
                        preV[i]=1.0-preV[i]
            print(preV)
            totV=dot(totV, preV)
        print(totV)
        pairs = [[i,totV[i]] for i in range(self.nCourses)]
        pairs.sort(key=lambda x:x[1], reverse=True)
        maxV=pairs[0][1]
        if (maxV<self.matchThreshold):
            print("没有符合条件的课程")
            return None;
        res=[]
        for pair in pairs:
            if (pair[1] >= maxV*self.acceptRatio):
                res.append(self.courses[pair[0]])
                print(pair[1])
                self.printCourse(pair[0])
        return res

    def resToString(self,res):
        s=[]
        for pair in res:
            s.append(str(self.courses[pair[0]]))
        return "\n".join(s)


    def printCourse(self, i):
        print(i,self.courses[i])

    def searchForOneKey(self,key):
        print("处理关键词：",key)
        res=[0.0]*self.nCourses
        for i in range(self.nCourses):
            #self.printCourse(i)
            for (p,v) in self.courses[i].items():
                if (p=="time&location"):
                    m=self.timeLocationMatch(v,key)
                else:
                    m=self.abbrMatch(v,key)
                res[i]+=m
                if (m>self.matchThreshold):
                    break
            #print(res[i])
       # print(res)
        return res

    def containMatch(self,s1, s2):
        pos = s1.find(s2)
        if (pos == -1):
            return 0.0
        else:
            return 1.0

    def abbrMatch(self,s1, s2):
        p = [r'(.*)']
        for c in s2:
            p.append(c)
            p.append(r"(.*)")
        g = re.match("".join(p), s1)
        if (g == None):
            return 0.0
        avg = 0.0
        for sub in g.groups():
            avg += self.decreaseRate ** len(sub)
        avg /= len(g.groups())
        return avg

    def timeLocationMatch(self,s1,s2):
        pos=s1.find(s2)
        if (pos==-1):
            return 0.0
        else:
            return 1.0

if __name__=="__main__":
    notice="""
使用说明：
检索条件用若干个用空格分开的句子表示，各句子之间为“且”的关系，单个句子中的各词为“或”的关系
可在句子开头使用否定副词
支持缩写
时间格式参考示例
示例：
周一1~4节 不是信科 开卷考试
"""
    searcher = Searcher()
    print(notice)
    print("请输入检索条件（exit退出）：")
    requests=input()
    while (requests.upper()!='EXIT'):
        searcher.search(requests)
        print("请输入检索条件（exit退出）：")
        requests=input()