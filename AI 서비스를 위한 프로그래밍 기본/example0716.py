# f = open('gugudan.txt','w')
# for i in range(2,10):
#     for j in range(1,10):
#         S = f'{i}X{j} = {i*j}\n'
#         f.write(S)
# f.close()

# #---------------------------------------------------------

# # code12-01
# class Car():
#     color=''
#     speed=0

#     def upspeed(self,value):
#         self.speed+=value
#         print(f'현재 속도 {self.speed}')

#     def downspeed(self,value):
#         self.speed-=value
#         print(f'현재 속도 {self.speed}')
    
#     def printmsg(self):
#         print('test printing')

# car1 = Car()
# car1.upspeed(100)
# car1.downspeed(40)
# #----------------------------------------------------------

# code12-03
class Car_c():
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed
        print(f'Your car just arrived , color:{self.color} , speed:{self.speed}km/h')

    def upspeed(self,amount):
        self.speed+=amount
        print(f'Current speed became {self.speed}km/h')

    def downspeed(self,amount):
        self.speed-=amount
        print(f'Current speed became {self.speed}km/h')
    
    def changecolor(self):
        var = input('Enter new color for change: ')
        self.color = var
        print(f'Current color became {self.color}')


mycar = Car_c('white',40)
mycar.upspeed(50)
mycar.downspeed(60)
mycar.changecolor()