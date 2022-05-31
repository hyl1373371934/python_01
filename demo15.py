class People():
    age=0
    def human(self,hh):
        print(hh,"开始了")

class Students(People):
    pass

class Teacher(People):
    pass

s=Students()
s.human('k')
print(s.age)