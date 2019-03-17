class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.weight=w

    def speak(self):
        print("%s说：我今年%s岁，%s公斤."%(self.name,self.age,self.weight))

class student(people):
    grade = ''

    def __init__(self,n,a,w,g):
        #调用父类的方法
        people.__init__(self,n,a,w)
        self.grade = g

    #覆盖父类的方法
    def speak(self):
       # print("%s说：我今年%s岁，%s公斤,考了%s分."%(self.name,self.age,
       #                                  self.weight,self.grade))
        print(self.name)

s = student('FiringJ',20,80,100)
s.speak()

p = people('FiringJ',20,80)
p.speak()

    
        
    
