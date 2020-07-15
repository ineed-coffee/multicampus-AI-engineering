num1 = int(input('num1의 값을 입력하세요. : \n'))
op = input('원하는 사칙 연산자를 입력하세요. : \n').rstrip()
num2 = int(input('num2의 값을 입력하세요. : \n'))

if op=='+':
    print(f'{num1}+{num2}는 {num1+num2}입니다.')
elif op=='-':
    print(f'{num1}-{num2}는 {num1-num2}입니다.')
elif op=='*':
    print(f'{num1}*{num2}는 {num1*num2}입니다.')
elif op=='/':
    if not num2:
        print('올바르지 않은 연산 형식')
    else:
        print(f'{num1}/{num2}는 {num1/num2}입니다.')
else:
    print('올바르지 않은 연산자')