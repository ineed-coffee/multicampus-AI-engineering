# Function--

# Generic Form
def sum(a,b):
    result  = a+b
    return result

# Input-free Form
def say():
    return 'hi'

# Return-free Form
def sum_2(a,b):
    print(f'{a}+{b} 의 결과값은 {a+b}입니다.')

# Input-free , Return-free Form
def say_2():
    print('hi')

# Variable Input arguments : *args , **kwargs
def Show_names(*args):
    print(type(args))
    for idx,name in enumerate(args):
        print(f'{idx+1}번째 사람의 이름은 {name}입니다.')

#Name = ['이순신','홍길동','강감찬','권율']
#Show_names(*Name)

def Show_names_kw(**kwargs):
    print(type(kwargs))
    for idx,name in enumerate(kwargs.items()):
        print(f'{idx+1}번째 사람의 이름은 {name}입니다.')

#Name = ['이순신','홍길동','강감찬','권율']
#Show_names(*Name)

# arguments with initial values : *warning - always put it at the end
def info(name,age = 20):
    print(f'{name}님의 나이는 {age}세 입니다.')

#info('이동재',28)
#info('켈라니')

# Call be value , Call by reference <=> immutable , mutable
def Append(list_type):
    list_type.append('a') # reference

def Add(value_type):
    value_type+=1         # value    


import calc_module as cm

Ans = cm.Add(1,2)
print(Ans)