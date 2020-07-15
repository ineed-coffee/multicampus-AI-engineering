#--------------Code09-02------------------
coffee=0

def coff_machine()button:
    print()
    print('#1. (자동으로) 뜨거운 물을 준비한다.')
    print('#2. (자동으로) 종이컵을 준비한다.')

    if button==1:
        print('#3. (자동으로) 보통커피를 탄다.')
    elif button==2:
        print('#3. (자동으로) 설탕커피를 탄다.')
    elif button==3:
        print('#3. (자동으로) 블랙커피를 탄다.')

    else:
        print('#3. (자동으로) 아무거나 탄다.')

    print('#4. (자동으로) 물을 붓는다.')
    print('#5. (자동으로) 스푼으로 젓는다.')
    print()


coffee = int(input('어떤 커피를 드릴까요? (1:보통 2:설탕 3:블랙)'))
coffee_machine(coffee)
print('손님 커피 여기 있습니다.')


#--------------Code09-06------------------
def func1():
    a=10
    print(f'func1()에서의 a값 {a}')

def func2():
    print(f'func2()에서의 a값 {a}')

a=20
func1()
func2()

#--------------Calculator using Function------------------

def Cal():

    while True:
        print('###################')
        print('#1. add')
        print('#2. subtract')
        print('#3. multiply')
        print('#4. divide')
        print('#5. exit')
        print('###################')
        print('Select Operation (1~5) : \n')
        op = int(input())

        print('Enter two numbers seperated by space : \n')
        a,b = map(int,input().split())
        if op==1:
            print(f'{a}+{b} = {a+b}')
        elif op==2:
            print(f'{a}-{b} = {a-b}')
        elif op==3:
            print(f'{a}*{b} = {a*b}')
        elif op==4:
            if not b:
                print('can not divide with value 0')
            else:
                print(f'{a}/{b} = {a/b}')
        elif op==5:
            print('exiting calculator function')
            return
        else:
            print('wrong command')

Cal()