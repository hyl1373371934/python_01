class  Students():
   # name='李四'
   # grade='5年级'
    def __init__(self,grade,name):
        self.grade=grade
        self.name=name

    def study(self):
        print("{}的{}正在学习".format(self.grade,self.name))


    def motion(self):
        print(self.grade,"零零", self.name)
s1=Students(2,3)
s1.motion()

