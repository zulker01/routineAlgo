import pandas as pd

#testing function
def test():
    print("stfu")

def readExcel(name):
    courses = pd.read_excel(name)

#total row number from excel
def totalRowNum(file):
    glen = file.index
    total_courses = len(glen)
    return total_courses

#getting course list from Courses sheet
def getCourseList(file):
    courseList = []
    total_course = totalRowNum(file)
    i=0
    for i in range(total_course):
        courseList.append(file['Course Code'][i])
    return courseList

#getting course credit from Courses Sheet
def getCourseCredit(file):
    courseList = {}
    total_course = totalRowNum(file)
    i=0
    for i in range(total_course):
        courseList[file['Course Code'][i]] = file['credit'][i]
    return courseList


def getCourseChoiceFor(file,i):
    courseList = []
    totat_teachers = totalRowNum(file)
    j=1
    for j in range(1,5):
        #print(file[j][i])
        courseList.append(file[j][i])
    return courseList

def getTeacherName(file,i):
    return file['Teacher Initial'][i]
    #      file['column name'][index]

def getTeacherTime(teachersFreeTime,i):
    freetime= []
    freetime.append(teachersFreeTime['Sunday'][i])
    freetime.append(teachersFreeTime['Monday'][i])
    freetime.append(teachersFreeTime['Tuesday'][i])
    freetime.append(teachersFreeTime['Wednesday'][i])
    freetime.append(teachersFreeTime['Thursday'][i])
    return freetime
