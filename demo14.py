class  Students():

    name="张三"
    __score="76"

    def __set_score(self,score):
        self.__score=score

    def get_score(self):
        return self.__score

s1=Students()
s1.get_score()