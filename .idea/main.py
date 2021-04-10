import pandas as pd
from readWriteExcel import *
from Course import *
from Teacher import *

#variables
courseList = []
courseCredit = {}
highestCourseChoiceForTeachers = 5
courseChoice = []
teacherTime = []

#open courses
courses = pd.read_excel("Routine.xlsx",sheet_name='Courses')
#print(type(courses))
total_courses = totalRowNum(courses)
#print(total_courses)

courseList = getCourseList(courses)
#print(courseList)
courseCredit = getCourseCredit(courses)
#print(courseCredit[courseList[2]])

#creating course class object array
CourseClass = []
for i in range(len(courseList)):

    #print(courseCredit[courseList[i]])
    #print(type(courseCredit[courseList[i]]))
    CourseClass.append(Course(courseList[i],courseCredit[courseList[i]]))
    #print(CourseClass[i].name+" "+str(CourseClass[i].credit)+" "+str(CourseClass[i].classes)+" "+str(CourseClass[i].duration))


#open teachers
teachers = pd.read_excel("Routine.xlsx",sheet_name='Teachers')
total_teachers = totalRowNum(teachers)
courseChoice = []
#print(total_teachers)
i = 0
#print(teachers)
#print(teachers[5][0])

#open teacher free time
teachersFreeTime = pd.read_excel("Routine.xlsx",sheet_name='TeacherFreeSlot')
#print(teachersFreeTime)

for i in range (0,2):
    teacherTime.append(getTeacherTime(teachersFreeTime,i))
    #print(teacherTime[i])

TeacherClass = []
for i in range(total_teachers):
    courseChoice.append(getCourseChoiceFor(teachers,i))
    #print(courseChoice[i])
    #print(getTeacherName(teachers,i))
    #print(getCourseChoiceFor(teachers,i))
    TeacherClass.append(Teacher(getTeacherName(teachers,i),courseChoice[i],teacherTime[i]))
    print(" for "+getTeacherName(teachers,i))
    TeacherClass[i].calculateTimeHash()
    #TeacherClass[i].calculateTimeHash()
    #print(TeacherClass[i].name+" "+str(TeacherClass[i].courseChoice)+" "+str(TeacherClass[i].teacherTime))
"""
def function(teacherI,courseI):
    print(str(TeacherClass[teacherI].teacherTime[0]))
    for i in range(5):
        if teachersFreeTime<=courseI.time:
            assign course time
            break
    for i in range(5): #each teacher can have 5 choices
        function(teacherI + 1, courseI)
        print( cours , teacher TIme)
"""
"""
def function(teacherI,courseI):
    if teacherI>=total_teachers:
        return 1
    time = TeacherClass[teacherI].teacherTime[0]
    course = TeacherClass[teacherI].courseChoice[courseI]
    courseNo = -1
    for i in range(total_courses):
        if CourseClass[i].name == course:
            courseNo = i
            break
    #print(courseNo)
    #print(CourseClass[courseNo].name)
    #print(TeacherClass[teacherI].courseChoice[courseI])
    if CourseClass[courseNo].flag == 0:
        CourseClass[courseNo].flag = 1
    else:
        print("impossible for "+course)
        return 0
    time1 = time[0:time.find(";")]
    time2 = time[time.find(";")+1:len(time)]
    time1start = time1[0:time1.find("-")]
    time1end = time1[time1.find("-")+1:len(time1)]
    newtime1start = float(time1start)+float(CourseClass[courseNo].duration)
    #print(newtime1start)
    #print(time1)
    #print(time2)
    #print(CourseClass[courseI].duration)
    function(teacherI+1,courseI)
    print(str(CourseClass[courseNo].name)+" "+str(TeacherClass[teacherI].name)+" "+str(time1start)+" - "+str(newtime1start))

function(0,0)
"""
print(str(TeacherClass[1].teacherTime))
