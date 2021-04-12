import pandas as pd

timeHashDictionary={}
"""
    slots   meaning
     1       8:30  (can be used as lab )
     2       10:00 (can be used as lab )
     3       11:30
     4       13:00
     5       14:00  (can be used as lab )
     6       15:30
     7       17:00
     
     
     
    """
timeHashDictionary["1"] = "8:30"
timeHashDictionary["2"] = "10:00"
timeHashDictionary["3"] = "11:30"
timeHashDictionary["4"] = "13:00"
timeHashDictionary["5"] = "14:00"
timeHashDictionary["6"] = "15:30"
timeHashDictionary["7"] = "17:00"

dayHashDictionary={}
dayHashDictionary['0'] = "Sunday"
dayHashDictionary["1"] = "Monday"
dayHashDictionary["2"] = "Tuesday"
dayHashDictionary["3"] = "WednesDay"
dayHashDictionary["4"] = "ThursDay"

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
