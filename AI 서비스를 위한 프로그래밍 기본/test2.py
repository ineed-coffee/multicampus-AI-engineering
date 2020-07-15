# a = input('첫 번째 숫자 : \n')
# b = input('두 번째 숫자 : \n')
# c = int(a)+int(b)
# print(f'{a}+{b}={c}')

money = int(input('금액 입력'))

c500 = money//500
money%=500

c100 = money//100
money%=100

c50 = money//50
money%=50

c10 = money//10
money%=10

print('----------------')
print(f'500원짜리 ==> {c500}개')
print(f'100원짜리 ==> {c100}개')
print(f'50원짜리 ==> {c50}개')
print(f'10원짜리 ==> {c10}개')
print(f'거스름돈 ==>{money}원')