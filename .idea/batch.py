class batch:
    flag = 0
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
    availableSlots=[]
    for i in range(5):
        availableSlots.append([1,2,3,4,5,6,7])
    def __init__(self,name):

        self.name = name