Types = [5,'6',10.5]
for t in Types:
    print(type(t))

f = 7/3
print(f,type(f))

s1 = 'Hello'
s2 = "안녕하세요 반갑습니다."
print(s1,s2)
print(s1+s2)

# 스트링 안에 '," 표현
food = "Python's favorite food is pearl"
say = '"Python is very easy." hey says.'
multiline = '''
... Life is too short
... You need python
...'''
print(multiline,len(multiline))

s4 = 'Lifeistooshort'
print(s4[:4])

k = 123456.789
print('This is %4.1f'%k) # basic formatting
print(f'This is {k:0.1f}') # String interpolation

msg = 'hi'
print(f'{msg:>10}') # 정렬 방법 반대는 <