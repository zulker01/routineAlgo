class Teacher:
    flag = 0
    timeHash=[]
    slots={}
    slots["8.30"]=1
    slots["10.00"]=2
    slots["11.30"]=3
    slots["13.00"]=4
    slots["14.00"]=5
    slots["15.30"]=6
    slots["17.00"]=7

    def __init__(self,name,courseChoice,teacherTime):

        self.name = name
        self.courseChoice = courseChoice
        self.teacherTime = teacherTime
    def getName(self):
        return self.name

    def getcourseChoice(self):
        return self.courseChoice
    def getTeacherTime(self):
        return self.teacherTime
    def getTeacherFlag(self):
        return self.flag

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

    # this function hashes the starting time when teacher is available , end of free time not added
    def calculateTimeHash(self):
        for i in range(len(self.teacherTime)):
            time = self.teacherTime[i]
            temp = []
            #print(str(i))
            if time.find(";")!=-1:
                time1 = time[0:time.find(";")]
                time2 = time[time.find(";")+1:len(time)]
                time1start = time1[0:time1.find("-")]
                time1end = time1[time1.find("-")+1:len(time1)]
                time2start = time2[0:time2.find("-")]
                time2end = time2[time2.find("-")+1:len(time2)]
                #print(time1start+time1end+" "+time2start+" "+time2end)

                temp.append(self.slots[time1start])

                if self.slots[time1end]-self.slots[time1start]>1:
                    for i in range(self.slots[time1start]+1,self.slots[time1end]):
                        temp.append(i)
                #temp.append(self.slots[time1end])
                temp.append(self.slots[time2start])
                if self.slots[time2end]-self.slots[time2start]>1:
                    for i in range(self.slots[time2start]+1,self.slots[time2end]):
                        temp.append(i)
                #temp.append(self.slots[time2end])
                #print(str(temp))
            elif time =="no":

                temp.append(0)

            else:
                #print(time)
                time1start = time[0:time.find("-")]
                time1end = time[time.find("-")+1:len(time)]

                temp.append(self.slots[time1start])

                if self.slots[time1end]-self.slots[time1start]>1:
                    for i in range(self.slots[time1start]+1,self.slots[time1end]):
                        temp.append(i)
                #print(str(temp))

            self.timeHash.append(temp)
            #print(str(self.timeHash))
