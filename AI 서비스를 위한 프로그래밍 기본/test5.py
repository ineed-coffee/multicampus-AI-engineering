# name = input('이름 입력: ')

# if name=='이순신':
#     print('이순신이 맞습니다.')
# else:
#     print('이순신이 아닙니다.')

# Num = int(input('수를 하나 입력: '))
# print('your input is even number' if not Num%2 else 'your input is odd number')

print('Arithmetic Calculator')
print('#####################')
print('#1. Add')
print('#2. Subtract')
print('#3. Multiply')
print('#4. Divide')
print('#5. Exit')
print('#####################')
print('Select your operation (1~5) : \n')
op = input().rstrip()
try:
    op = int(op)
    a,b = map(int,input('Submit two numbers you want to operate \nMake sure to seperate them with space: \n').split())
except ValueError:
    print('Invalid operation selection')

if op==1:
    print(f'{a}+{b} = {a+b}.')
elif op==2:
    print(f'{a}-{b} = {a-b}.')
elif op==3:
    print(f'{a}*{b} = {a*b}.')
elif op==4:
    if not b:
        print('Can not divide with value 0')
    else:
        print(f'{a}/{b} = {a/b}.')



