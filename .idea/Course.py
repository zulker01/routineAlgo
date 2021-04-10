class Course:
    classes = 0
    duration = 0
    flag = 0
    def __init__(self,name,credit):

        self.name = name
        self.credit = credit
        if credit==1.5:
            self.classes = 1
            self.duration = 3
        elif credit==3:
            self.classes = 2
            self.duration = 1.5
        elif credit == 2:
            self.classes = 2
            self.duration = 1.5
    def getName(self):
        return self.name

    def getCredit(self):
        return self.credit
    def getClasses(self):
        return self.classes
    def getDuration(self):
        return self.duration
    def getCourseFlag(self):
        return self.flag