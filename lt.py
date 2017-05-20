#-*- coding:utf-8 -*-
import xlrd
import xlwt
import thulac
import jieba
import json
import re
import sys

from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QDesktopWidget, QTableWidgetItem, QHeaderView)


class table(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        a={1:2, 4:5}
        print(1 in a)


        self.resize(400, 400)
        self.setWindowTitle('TableWidget')


        self.table = QTableWidget(2, 3)
        self.table.setHorizontalHeaderLabels(['Team', 'Number', 'Name'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents | QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents | QHeaderView.Stretch)

        team = QTableWidgetItem('Arse\nnal\nsdfkl')
        number = QTableWidgetItem('11\ndfssdf\nfdf')
        name = QTableWidgetItem('Ozill\nddddd\ndsdlfkj\nsddf')
        self.table.setItem(0, 0, team)
        self.table.setItem(0, 1, number)
        self.table.setItem(0, 2, name)
        layout = QHBoxLayout()

        layout.addWidget(self.table)
        self.setLayout(layout)
        self.center()
        self.show()

        self.table.setRowCount(4)
        self.table.setColumnCount(5)

        a=QTableWidgetItem("a\nb\nc")
        self.table.setItem(3,4,a)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    exp = table()
    sys.exit(app.exec_())
"""
a={'a':'b', 'c':1}
b=str(a)
print(b)
p=r'(?P<negAdv>(不)|(没)|(无)|(非))(?P<positive>.*)'
m=re.match(p,"含123")
print(m.group("negAdv"),m.group('positive'))

def abbrMatch(s1, s2):
    p = [r'(.*)']
    for c in s2:
        p.append(c)
        p.append(r"(.*)")
    g = re.match("".join(p), s1)
    if (g == None):
        return 0.0
    avg=0.0
    for sub in g.groups():
        avg+= 0.5**len(sub)
    avg/=len(g.groups())
    print(avg)

abbrMatch("我是一个男人","是男")

a=[ [1,2] , [5,0], [7, 8]]
a.sort(key=lambda x: x[1], reverse=True)
print(a)

js={"name":"xiaoming", "age":10}
st=json.dumps(js)
print(st)
jj=json.loads(st)
print(jj)
print(jj["name"])
print(jj["age"])


request = input()
print(request)
print(request.encode('utf=8').decode('utf-8'))

thu1=thulac.thulac()
text=thu1.cut(request)
print(text)

jieba.load_userdict("public.txt")
s2=jieba.cut(request, cut_all=False)
print(s2)
s3=jieba.cut(request)
s4=jieba.cut_for_search(request)
print("/".join(s2))
print("/".join(s3))
print("/".join(s4))

for x in s2:
    print(x)
print("----")
for x in s2:
    print(x)
"""


