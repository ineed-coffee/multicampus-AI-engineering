import time as t
import sqlite3

class EMP_MGMT():

    def __init__(self):
        self.ui_text=[]
        self.ui_text.append('# 사원 관리')
        self.ui_text.append('################################')
        self.ui_text.append('1. 전체사원검색')
        self.ui_text.append('2. 사원 검색')
        self.ui_text.append('3. 사원 추가')
        self.ui_text.append('4. 사원 수정')
        self.ui_text.append('5. 사원 삭제')
        self.ui_text.append('6. 종료')
        self.ui_text.append('################################')
        self.ui_text.append('메뉴를 선택해주세요. (1-6) : ')
        self.make_db()

    def make_db(self):
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        if not self.cur.fetchall():
            self.cur.execute('create table emp(id int primary key not null , name text not null)')
            self.db.commit()
        self.db.close()
        return

    def user_search_all(self):
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute('select * from emp')
        while True:
            info = self.cur.fetchone()
            if not info:
                break
            print(f'ID = {info[0]}  ,  NAME = {info[1]}')
        self.db.close()
        return

    def user_read(self,id_in,name_in):
        flag=False
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute(f'select * from emp where id={id_in} and name=\'{name_in}\'')
        if self.cur.fetchall():
            flag=True
        self.db.close()
        return flag

    def user_create(self,id_in,name_in):
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute(f'insert into emp values({id_in},\'{name_in}\')')
        self.db.commit()
        self.db.close()
        return

    def user_update(self,id_in,new_name_in):
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute(f'update emp set name=\'{new_name_in}\' where id={id_in}')
        self.db.commit()
        self.db.close()
        return

    def user_delete(self,id_in):
        self.db = sqlite3.connect('c:\\sqlite\\company.db')
        self.cur = self.db.cursor()
        self.cur.execute(f'delete from emp where id={id_in}')
        self.db.commit()
        self.db.close()
        return

    def run(self):

        while True:

            for i in self.ui_text:
                print(i)
            com = int(input())

            if com == 6:
                print('이용해주셔서 감사합니다.')
                break
            if com == 1:
                self.user_search_all()

            elif com == 2:
                id_in,name_in = input('검색하실 사원의 ID와 이름을 공백으로 구분하여 입력하세요. : ').rstrip().split()
                try:
                    val = self.user_read(int(id_in),name_in)
                    if val:
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 등록되어 있습니다.')
                    else:
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 등록되어 있지 않습니다.')
                except TypeError:
                    print('wrong type')
                    
            elif com == 3:
                id_in,name_in = input('추가하실 사원의 ID와 이름을 공백으로 구분하여 입력하세요. : ').rstrip().split()
                try:
                    val = self.user_read(int(id_in),name_in)
                    if val:
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 이미 등록되어 있습니다.')
                    else:
                        self.user_create(int(id_in),name_in)
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 등록 되었습니다.')
                except TypeError:
                    print('wrong type')

            elif com == 4:
                id_in,name_in = input('수정하실 사원의 ID와 이름을 공백으로 구분하여 입력하세요. : ').rstrip().split()
                try:
                    id_in=int(id_in)
                    val = self.user_read(id_in,name_in)
                    if val:
                        new_name_in = input(f'ID = {id_in} 인 사원의 새로운 이름을 입력하세요. : ').rstrip()
                        self.user_update(id_in,new_name_in)
                        print(f'사원정보 ID={id_in}  ,  NAME={new_name_in} 로 수정 되었습니다.')
                    else:
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 등록 되어있지 않습니다.')

                except TypeError:
                    print('wrong type')

            elif com == 5:
                id_in,name_in = input('삭제하실 사원의 ID와 이름을 공백으로 구분하여 입력하세요. : ').rstrip().split()
                try:
                    id_in=int(id_in)
                    val = self.user_read(id_in,name_in)
                    if val:
                        self.user_delete(id_in)
                        print(f'사원정보 ID={id_in}  ,  NAME={new_name_in} 가 삭제되었습니다.')
                    else:
                        print(f'사원정보 ID={id_in}  ,  NAME={name_in} 가 등록 되어있지 않습니다.')

                except TypeError:
                    print('wrong type')
            
            print()
            print()
            t.sleep(1.5)
        return

if __name__ == '__main__':

    my_emp_mgmt = EMP_MGMT()
    my_emp_mgmt.run()