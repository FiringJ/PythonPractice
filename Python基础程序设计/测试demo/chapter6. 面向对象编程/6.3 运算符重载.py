class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return "Vector(%d,%d)"%(self.a,self.b)

    #重载运算符‘+’
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(1,2)
v2 = Vector(5,-1)
print(v1+v2)
