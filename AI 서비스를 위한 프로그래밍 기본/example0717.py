# #----------- Using super() method to call superior class method or fields
# class person():

#     def __init__(self,name='hi'):
#         self.name = name

# class student(person):

#     def __init__(self):
#         super().__init__('wow')

# s=student()

# #accessor : public , private(__) , protected(_)

# class Emp():

#     def __init__(self,name,salary):

#         self._name = name
#         self._salary = salary

# e = Emp('이순신',200)

# #--------------- modifying magic method----------------------
# class Line:

#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __add__(self,other):
#         return Line(self.a+other.a,self.b+other.b)
    

# l1 = Line(1,2)
# l2 = Line(3,4)
# l3 = l1+l2
# print(l3.__dict__)


class Point():
    
    def __init__(self,length):
        self.length = length

    def add(self,other):
        return self+other
    
    def __add__(self,other):
        return Point(self.length+other.length)
    
    def __repr__(self):
        return f'이 오브젝트의 선분 길이 : {self.length}'

p1=Point(30)
p2=Point(20)
p3 = p1.add(p2)
print(p3.length)
print(p3.add(p1))
