# i=1

# while True:
#     n = input('Enter any number : \n')
#     print(f'number {n} recieved')


#--------------- break & continue-----------------------

coffee = 10
money = 300

while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee-=1
    print(f'남은 커피 판매랴은 {coffee}개 입니다.')
    if not coffee:
        print('커피가 다 떨어져 판매를 중지합니다.')
        break
    else:
        continue

#--------------- for statement structure-----------------------

s = 'hello'
for i in s:
    print(i)

L = [1,2,3,4,5,6,7]
for i in L:
    print(i)

#---------------- for statement practice-----------------------

n = int(input('원하는 단수 입력 : \n'))

for i in range(1,10):
    print(f'{n} X {i} = {n*i}')
