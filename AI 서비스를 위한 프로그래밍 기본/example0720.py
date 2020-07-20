# adding ENV var.
# import sys
# sys.path.append('C:\\MyApp\\mypackage')
# # sys.path.append('C:\\강의노트\\multicamp-AIengineeringbasedondeeplearning\\AI 서비스를 위한 프로그래밍 기본')
# print(sys.path)

import time as t
import os

class UserMGMT():
    
    def __init__(self,*argm):
        self.Users = []
        if os.path.exists('user.txt'):
            self.User_txt = open('user.txt','r',encoding='utf-8')
            for name in self.User_txt.readlines():
                self.Users.append(name.rstrip())
            self.User_txt.close()
    def call(self,com_type):
        if com_type == 1:
            self.All_users()
        elif com_type == 2:
            name = input('검색할 이름을 입력하세요. : \n').rstrip()
            if self.search_User(name):
                print(f'{name}님은 회원으로 등록되어 있습니다.')
            else:
                print(f'{name}님은 회원으로 등록되어 있지 않습니다.')
            return
        elif com_type == 3:
            while True :
                name = input('추가할 이름을 입력하세요. : \n').rstrip()
                if self.search_User(name):
                    print(f'{name}님은 회원으로 이미 등록되어 있습니다. \n')
                else:
                    self.add_User(name)
                    return

        elif com_type == 4:
            while True :
                name = input('수정하실 이름을 입력하세요. : \n').rstrip()
                if not self.search_User(name):
                    print(f'{name}님은 회원으로 등록되어 있지 않습니다. \n')
                else:
                    while True :
                        mod_name = input('수정된 이름을 입력하세요. : \n').rstrip()
                        if self.search_User(mod_name):
                            print(f'{mod_name}님은 회원으로 이미 등록되어 있습니다. \n')
                        else:
                            self.modify_User(name,mod_name)
                            return

        elif com_type == 5:
            while True :
                name = input('삭제할 이름을 입력하세요. : \n').rstrip()
                if not self.search_User(name):
                    print(f'{name}님은 회원으로 등록되어 있지 않습니다. \n')
                else:
                    self.delete_User(name)
                    return
        elif com_type == 6:
            self.exit_mgmt()

    def All_users(self):
        for i in self.Users :
            print(i)

    def search_User(self,name):
        if name in self.Users :
            return True
        return False

    def add_User(self,name):
        self.Users.append(name)
        self.User_txt = open('user.txt','w',encoding='UTF-8')
        for i in self.Users :
            self.User_txt.write(i+'\n')
        self.User_txt.close()
        print(f'{name} 회원을 추가하였습니다.')

    def modify_User(self,name,mod_name):
        idx = self.Users.index(name)
        self.Users[idx]=mod_name
        self.User_txt = open('user.txt','w',encoding='UTF-8')
        for i in self.Users :
            self.User_txt.write(i+'\n')
        self.User_txt.close()
        print(f'{mod_name} 의 이름으로 수정하였습니다.')

    def delete_User(self,name):
        self.Users.remove(name)
        self.User_txt = open('user.txt','w',encoding='UTF-8')
        for i in self.Users :
            self.User_txt.write(i+'\n')
        self.User_txt.close()
        print(f'{name} 의 이름을 삭제하였습니다.')

    def exit_mgmt(self):
        pass
#        self.User_txt.close()

if __name__ == '__main__':

    my_MGMT = UserMGMT()


    while True:

        print('#회원관리')
        print('########################################')
        print(f'1. 전체 회원목록')
        print('2. 회원검색')
        print('3. 회원추가')
        print('4. 회원수정')
        print('5. 회원삭제')
        print('6. 종료')
        print('########################################')

        while True:
            try:
                command = int(input('메뉴를 선택해주세요. (1-6): \n'))
                break
            except TypeError:
                print('1-6 사이의 입력만 허용\n')
        
        my_MGMT.call(command)
        if command==6:
            print('이용해주셔서 감사합니다. \n')
            break
        t.sleep(2)
            
