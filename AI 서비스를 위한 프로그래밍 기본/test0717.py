# #-----review : class --------------

# class person():

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.acc_dist=0
#         self.hp = 100

#     def walk(self,amount):
#         if self.hp:
#             self.acc_dist+=amount
#             self.hp-=amount//2
#             print(f'{amount}km 를 산책하여 현재까지 누적거리는 {self.acc_dist}km 입니다.')
#         else:
#             print(f'현재 체력이 부족하여 이동할 수 없습니다.')
    
#     def eat(self,amount):
#         if self.hp>=400:
#             print(f'현재 체력은 {self.hp}로 꽉 찬 상태입니다.')
#         else:       
#             self.hp+=amount
#             print(f'{amount}만큼의 체력을 보충하여 현재 체력은 {self.hp}입니다.')


# P = person('하이',25)
# P.walk(30)
# P.eat(40)
# #---------------------------------------------

# class testing():
#     i=0
#     def __init__(self):
#         self.j=0

# print(testing.i)
# testing.i+=100              # Verifying instance can not change class var.
# print(testing.i)

# t = testing()
# print(t.i)
# print(t.__dict__)
# t.i+=100
# print(t.i)
# print(t.__dict__)

# #-------------------------------------------------

# class Employee():
#     emp_cnt=0

#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         Employee.emp_cnt+=1

#     def disp_cnt(self):
#         print(Employee.emp_cnt)
#     def disp_info(self):
#         print(f'name={self.name} , salary={self.salary}')

#     def __del__(self):
#         cls_name = self.__class__.__name__
#         print(cls_name+'destroyed')

# ee = Employee('asg',300)
# ee.__del__
# #---------------------------------------------------

# class Animal():
    
#     def __init__(self,category):
#         self.category=category

#     def breathing(self):
#         print('breathing now')

# class Bird(Animal):
    
#     def __init__(self,category='bird'):
#         pass


# b = Bird()
# print(b.__dict__)
# #----------------------------------------------------

# class Point():
    
#     def __init(self):
#         self.x=1
#         self.y=1

#     def __del__(self):
#         pass


# p1 =Point()
# p2=p1
# p3=p2
# print(id(p1),id(p2))
# del(p1)
# print(p2.x)
# print(p1)
# #-----------------------------------------------------

# # over-riding
# class Animal():
#     def breathing(self):
#         print('Animal breathing')
# class Bird(Animal):
#     def breathing(self):
#         print('Bird breathing')

# #----------------------------------------------------

# class Database():

#     def open(self):
#         print('Database open')

# class Oracle(Database):
    
#     def open(self):
#         print('Oracle open')

# class MySql(Database):

#     def open(self):
#         print('MySql open')

# #-----------------------------------------------------

class Account():
    
    def __init__(self,accNo,name,balance):
        self.__accNo = accNo
        self.__name = name
        self.__balance = balance
                                        # balance 필드 변수에 직접적으로 접근할 수 없도록 private 접근자 이용

    def withdraw(self,amount):
        self.__balance-=amount

    def deposit(self,amount):
        self.__balance+=amount

    def get_balance(self):
        return [self.__name , self.__accNo, self.__balance]
    

c = Account(1,'wow',2000)
print(*c.get_balance())
c.deposit(1500)
print(*c.get_balance())
c.withdraw(2500)
print(*c.get_balance())    