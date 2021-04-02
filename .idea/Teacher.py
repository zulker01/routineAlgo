class Teacher:
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