class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w

    def speak(self):
        print("%s说：我今年%s岁"%(self.name,self.age))
        print(self.__weight)

p = people('FiringJ',20,80)
p.speak()
