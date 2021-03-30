import pandas as pd
from readWriteExcel import *


courseList = []
courseCredit = {}


courses = pd.read_excel("Courses.xlsx")
print(type(courses))
total_courses = totalRowNum(courses)
print(total_courses)

courseList = getCourseList(courses)
print(courseList)
courseCredit = getCourseCredit(courses)
print(courseCredit)
