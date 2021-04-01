import pandas as pd
from readWriteExcel import *

#variables
courseList = []
courseCredit = {}
highestCourseChoiceForTeachers = 5
courseChoice = []

#open courses
courses = pd.read_excel("Routine.xlsx",sheet_name='Courses')
print(type(courses))
total_courses = totalRowNum(courses)
print(total_courses)

courseList = getCourseList(courses)
print(courseList)
courseCredit = getCourseCredit(courses)
print(courseCredit)

#open teachers
teachers = pd.read_excel("Routine.xlsx",sheet_name='Teachers')
total_teachers = totalRowNum(teachers)
courseChoice = []
print(total_teachers)
i = 0
print(teachers)
print(teachers[5][0])



for i in range(total_teachers):
    courseChoice.append(getCourseChoiceFor(teachers,i))
    print(courseChoice[i])
    #print(i)
    print(getCourseChoiceFor(teachers,i))

