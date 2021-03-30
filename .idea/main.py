import pandas as pd
from readWriteExcel import *


courseList = []
courseCredit = {}
"""
excel_file = 'Courses.xlsx'

#cell_value_class = courses.loc[2,2]
print(courses['Course Code'][1])
glen = courses.index
total_courses = len(glen)
i=0
"""

courses = pd.read_excel("Courses.xlsx")
print(type(courses))
total_courses = totalRowNum(courses)
print(total_courses)

courseList = getCourseList(courses)
print(courseList)
courseCredit = getCourseCredit(courses)
print(courseCredit)
"""
for i in range(total_courses):
    courseList.append(courses['Course Code'][i])
    # courseCredit.update({courses['Course Code'][i],courses['credit'][i]})
    courseCredit[courses['Course Code'][i]] = courses['credit'][i]
print(courseList)
print(courseCredit)
print()
test()
print(len(glen))
print(type(courses))
print(courses)
print(courses.shape)
print()
#print(cell_value_class)
"""
"""
https://pythoninoffice.com/get-values-rows-and-columns-in-pandas-dataframe/
https://www.journaldev.com/33306/pandas-read_excel-reading-excel-file-in-python
d = {}
wb = xlrd.open_workbook('foo.xls')
sh = wb.sheet_by_index(2)
for i in range(138):
    cell_value_class = sh.cell(i,2).value
    cell_value_id = sh.cell(i,0).value
    d[cell_value_class] = cell_value_id

"""