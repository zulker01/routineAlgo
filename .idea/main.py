import pandas as pd
from readWriteExcel import *
from Course import *
from Teacher import *
from batch import *

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


#open teacher free time
teachersFreeTime = pd.read_excel("Routine.xlsx",sheet_name='TeacherFreeSlot')
#print(teachersFreeTime)

for i in range (total_teachers):
    teacherTime.append(getTeacherTime(teachersFreeTime,i))
    #print(teacherTime[i])

TeacherClass = []
for i in range(total_teachers):
    courseChoice.append(getCourseChoiceFor(teachers,i))
    print(courseChoice[i])
    #print(getTeacherName(teachers,i))
    #print(getCourseChoiceFor(teachers,i))
    TeacherClass.append(Teacher(getTeacherName(teachers,i),courseChoice[i],teacherTime[i]))

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
   if teacherI>=total_teachers:
       return 1
   time = TeacherClass[teacherI].teacherTime[0]
   
   #print(courseNo)
   #print(CourseClass[courseNo].name)
   #print(TeacherClass[teacherI].courseChoice[courseI])
   
   time1 = time[0:time.find(";")]
   time2 = time[time.find(";")+1:len(time)]
   time1start = time1[0:time1.find("-")]
   time1end = time1[time1.find("-")+1:len(time1)]
   newtime1start = float(time1start)+float(CourseClass[courseNo].duration)
   #print(newtime1start)
   #print(time1)
   #print(time2)
   #print(CourseClass[courseI].duration)
   """
batch24 = batch("24")
def function(teacherI,courseI,coursesFilled,routine):

    time1 = 0
    time2 = 0
    time1i = 0
    time2i = 0
    doneFlag=0
    #print("in stack teacherI "+str(teacherI)+" courseI "+str(courseI)+" coursesFilled "+str(coursesFilled)+" routine ")
    if coursesFilled==total_courses:
        print("Successful routine")
        print(routine)
        return 1
    if teacherI>=total_teachers:
        return 0
    if len(TeacherClass[teacherI].courseChoice)<=courseI:
        return 0
    course = TeacherClass[teacherI].courseChoice[courseI]
    #print(course)
    courseNo = -1
    for i in range(total_courses):
        if CourseClass[i].name == course:
            courseNo = i
            break
    if CourseClass[courseNo].flag == 0:
        CourseClass[courseNo].flag = 1
    else:
        #print("impossible for "+course)
        return 0
    """
    if CourseClass[courseNo].credit == 1.5:
        for i in range(5):
            #print(len(TeacherClass[teacherI].timeHash[i]))
            if doneFlag==1:
                break
            if len(TeacherClass[teacherI].timeHash[i])>2:
                time1 = TeacherClass[teacherI].timeHash[i][0]
                TeacherClass[teacherI].timeHash[i].remove(time1)
                time1i = i
                #print(time1i)
                #print(str(TeacherClass[teacherI].name+str(time1i)+" -time 1  "+str(time1)))
                if time1 in batch24.availableSlots[i]:
                    batch24.availableSlots[i].remove(time1)
                    doneFlag==1
                    break
                else:
                    time1=0
                    time1i=0
                    continue
    else:
    """
    for i in range(5):
        #print(len(TeacherClass[teacherI].timeHash[i]))
        if doneFlag==1:
            break
        if len(TeacherClass[teacherI].timeHash[i])>1:
            time1 = TeacherClass[teacherI].timeHash[i][0]
            TeacherClass[teacherI].timeHash[i].remove(time1)
            time1i = i

            if time1 in batch24.availableSlots[i]:
                batch24.availableSlots[i].remove(time1)
            else:
                time1=0
                time1i=0
                continue
            for j in range(i+1,5):
                if len(TeacherClass[teacherI].timeHash[j])>1:
                    time2 = TeacherClass[teacherI].timeHash[j][0]
                    TeacherClass[teacherI].timeHash[j].remove(time2)
                    time2i = j
                    #print(str(TeacherClass[teacherI].name+str(time2i)+" -time 2  "+str(time2)))
                    print()
                    if time2 in batch24.availableSlots[j]:
                        batch24.availableSlots[j].remove(time2)
                        doneFlag=1
                        #print(str(batch24.availableSlots[j]))
                        break
                    else:
                        time2=0
                        time2i =0
                        continue
    if doneFlag==0:
        return 0
    #print(str(CourseClass[courseNo].name)+" "+str(TeacherClass[teacherI].name+str(time1i)+" - "+str(time1)+" "
                                                  #+str(time2i)+" - "+str(time2)+" "))


    routine = routine+str(CourseClass[courseNo].name)+" "+str(TeacherClass[teacherI].name)+"\n"+dayHashDictionary[str(time1i)]
    routine = routine+" "+timeHashDictionary[str(time1)]+"\n"+dayHashDictionary[str(time2i)]+" "+timeHashDictionary[str(time2)]+"\n\n"
    done1=0
    done2=0
    if teacherI+1<total_teachers and len(TeacherClass[teacherI].courseChoice)>courseI:
        done1 = function(teacherI+1,courseI,coursesFilled+1,routine)
        course = TeacherClass[teacherI+1].courseChoice[courseI]

        courseNo = -1
        for i in range(total_courses):
            if CourseClass[i].name == course:
                courseNo = i
                break
        if CourseClass[courseNo].flag == 1:
            CourseClass[courseNo].flag = 0
            #print("flag reset "+course)
    if teacherI<total_teachers and len(TeacherClass[teacherI].courseChoice)>courseI+1:
        done2 = function(teacherI,courseI+1,coursesFilled+1,routine)
        course = TeacherClass[teacherI].courseChoice[courseI+1]
        courseNo = -1
        for i in range(total_courses):
            if CourseClass[i].name == course:
                courseNo = i
                break
        if CourseClass[courseNo].flag == 1:
            CourseClass[courseNo].flag = 0
            #print("flag reset "+course)
    if time1!=0:
        #print("reset Time for "+TeacherClass[teacherI].name)
        TeacherClass[teacherI].timeHash[time1].append(time1i)
    if time2!=0:
        #print("reset Time for "+TeacherClass[teacherI].name)
        TeacherClass[teacherI].timeHash[time2].append(time2i)
    if (done1 or done2)==1 :

        return 1
    return 0

    #return done
function(0,0,0,"")
