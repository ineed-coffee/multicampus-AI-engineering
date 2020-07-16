# a_func = lambda a,b : a+b

# def test_f (f):
#     result = f(10,20)
#     return result

# Ans = test_f(a_func) # argument 에 function을 넣는것도 파이썬은 가능

# #---------- adding ENV var.-------------------
# import  sys 
# sys.path.append('절대경로 입력')
# #---------------------------------------------

# #----------- File read&write -----------------
# f = open('0716.txt','w')
# for i in range(10):
#     data = f'this is {i+1}th line 아아아\n'       #write mode , add mode works same except over-writting
#     f.write(data)
# f.close()

# f = open('0716.txt','r')
# for i in range(4):
#     print(f.readline())                             #read mode
# k= f.readlines()
# print(k)
# f.close()
# #---------------------------------------------

# #-----------------Class Generation------------
# class Student():
#     Id = 0
#     grade = 0
#     name=''

#     def study(self,no,name,grade):
#         self.Id = no
#         self.name = name
#         self.grade = grade

# me = Student()
# me.study(10,'홍길동',3)

class Employee():

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def working(self):
        print(f'해당 근로자 정보 : 이름={self.name} , 나이={self.age}')
    
e1 = Employee('으아아아아',100)
e1.working()