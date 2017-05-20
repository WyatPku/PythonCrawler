#-*- coding:utf-8 -*-
import xlrd
import jieba

def publicToDict():
    print("Making directory for public elective courses")
    workbook = xlrd.open_workbook("公选课.xls")
    table=workbook.sheet_by_name("basic")
    dct = open("public.txt",encoding='utf-8',mode='w')
    nRow=table.nrows
    nCol=table.ncols
    nCourse=nRow-1
    words=[]
    noCut={"课程号", "学分"}
    for i in range(1,nCourse+1):
        for j in range(1,nCol):
            type = table.cell(0,j).value
            content = table.cell(i,j).value
            dct.write(content+'\n')
            if (type not in noCut):
                ls=jieba.cut(content)
                for x in ls:
                    dct.write(x+'\n')
    print("done")

if __name__=="__main__":
    publicToDict()
