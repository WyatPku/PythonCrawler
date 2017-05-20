#-*- coding:utf-8 -*-
#python 3

import Searcher

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication,
                             QTextEdit,QLabel,QGridLayout,QLineEdit,QTextBrowser,
                             QTableWidget, QTableWidgetItem, QHeaderView,QAbstractItemView,
                             QMessageBox)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.searcher = Searcher.Searcher()

    def initUI(self):
        self.idLabel= QLabel("学号：")
        self.pwLabel=QLabel("密码：")
        self.idText = QLineEdit()
        self.pwText= QLineEdit()
        self.searchLabel=QLabel("输入检索条件:")
        self.searchText=QLineEdit()
        self.resLabel=QLabel("检索结果：")
        self.resText=QTextBrowser()
        self.table=QTableWidget()

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents | QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents | QHeaderView.Stretch)
        self.table.verticalHeader().setHidden(True)

        self.crawlButton = QPushButton("获取信息")
        self.searchButton = QPushButton("搜！")

        self.crawlButton.clicked.connect(self.crawlButtonClicked)
        self.searchButton.clicked.connect(self.searchButtonClicked)

        grid=QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.idLabel, 1,0)
        grid.addWidget(self.idText, 1,1)
        grid.addWidget(self.pwLabel, 2,0)
        grid.addWidget(self.pwText, 2,1)
        grid.addWidget(self.crawlButton, 3,1)
        grid.addWidget(self.searchLabel,4,0)
        grid.addWidget(self.searchText,4,1)
        grid.addWidget(self.searchButton,5,1)
        grid.addWidget(self.resLabel,6,0)
        grid.addWidget(self.table,6,1)

        self.pwText.setEchoMode(QLineEdit.Password)

        self.setLayout(grid)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Courses')
        self.show()

    def searchButtonClicked(self):
        print(self.searchText.text())
        courses = self.searcher.search(self.searchText.text())
        if not courses:
            self.table.setRowCount(1)
            self.table.setColumnCount(1)
            self.table.setItem(0,0,QTableWidgetItem("没有符合条件的课程"))
            return
        prop=[]
        for c in courses:
            for p in c.keys():
                if p not in prop:
                    prop.append(p)
        nProp=len(prop)
        nCourses=len(courses)
        self.table.setRowCount(nCourses)
        self.table.setColumnCount(nProp+1)
        self.table.setHorizontalHeaderLabels(["Num."]+prop)
        for i in range(nCourses):
            item=QTableWidgetItem(str(i+1))
            self.table.setItem(i,0,item)
            for j in range(len(prop)):
                if prop[j] in courses[i]:
                    item=QTableWidgetItem(str(courses[i][prop[j]]))
                    self.table.setItem(i, j+1,item)

    def crawlButtonClicked(self):
        OK = QMessageBox.information(self, ("这是标题"), ("""开发者很懒，没有写这个功能"""),  # 除了information还有warning、about等
                                     QMessageBox.StandardButton(QMessageBox.Yes))

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
