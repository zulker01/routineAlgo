import pandas as pd


def test():
    print("stfu")

def readExcel(name):
    courses = pd.read_excel(name)

def totalRowNum(file):
    glen = file.index
    total_courses = len(glen)
    return total_courses

def getCourseList(file):
    courseList = []
    total_course = totalRowNum(file)
    i=0
    for i in range(total_course):
        courseList.append(file['Course Code'][i])
    return courseList

def getCourseCredit(file):
    courseList = {}
    total_course = totalRowNum(file)
    i=0
    for i in range(total_course):
        courseList[file['Course Code'][i]] = file['credit'][i]
    return courseList