import pandas as pd
from readWriteExcel import *
from Course import *
from Teacher import *

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
print(courseCredit[courseList[2]])

#creating course class object array
CourseClass = []
for i in range(len(courseList)):

    #print(courseCredit[courseList[i]])
    #print(type(courseCredit[courseList[i]]))
    CourseClass.append(Course(courseList[i],courseCredit[courseList[i]]))
    print(CourseClass[i].name+" "+str(CourseClass[i].credit)+" "+str(CourseClass[i].classes)+" "+str(CourseClass[i].duration))


#open teachers
teachers = pd.read_excel("Routine.xlsx",sheet_name='Teachers')
total_teachers = totalRowNum(teachers)
courseChoice = []
print(total_teachers)
i = 0
print(teachers)
print(teachers[5][0])

#open teacher free time
teachersFreeTime = pd.read_excel("Routine.xlsx",sheet_name='TeacherFreeSlot')
TeacherClass = []
for i in range(total_teachers):
    courseChoice.append(getCourseChoiceFor(teachers,i))
    print(courseChoice[i])
    print(getTeacherName(teachers,i))
    print(getCourseChoiceFor(teachers,i))
    TeacherClass.append(Teacher(getTeacherName(teachers,i),courseChoice[i]))
    print(TeacherClass[i].name+" "+str(TeacherClass[i].courseChoice))