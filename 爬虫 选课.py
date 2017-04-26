import re
import os
import  xdrlib ,sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import xlrd
import xlwt

input = open("/Users/cz/Desktop/elective.html","r")
str = input.read()
reg = r'''<td .+><span>(.+?)</span></td>|(</tr>)'''

data = []
lst = []
for i in re.finditer(reg, str):
	if i.group(2) == "</tr>":
		data.append(lst)
		lst = []
	else : lst.append(i.group(1))

os.chdir("/Users/cz/Desktop/")
workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet')
for i in range(len(data)):
	for j in range(len(data[i])):
		worksheet.write(i, j, label = data[i][j])
workbook.save('have_try.xls')