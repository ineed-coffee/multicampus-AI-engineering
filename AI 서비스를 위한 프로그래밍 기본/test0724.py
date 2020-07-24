# import requests

# url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=wMtQHCpU1eLCXZ15tASu9FFMYhKKFNkiqyVNWtTA2LF9HuhFiLXDX9Q36a3sBSAfOUpWxmL%2BPJ0gdG6iX5EgQQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200310&endCreateDt=20200315"

# res = requests.get(url)
# print(res.text)

# import xml.etree.ElementTree as xml

# def createXML(filename):
#     root = xml.Element('users')
#     children1 = xml.Element('user')
#     # == children1 = xml.SubElement(root,'user')
#     root.append(children1)

#     tree = xml.ElementTree(root)
#     with open(filename,'wb') as fh:
#         tree.write(fh)

# if __name__ == '__main__':
#     createXML('C:\multicamp-AIengineeringbasedondeeplearning\AI 서비스를 위한 프로그래밍 기본\\testXML.xml')

import requests
import xml.etree.ElementTree as xml
import time
from tkinter import *
import sys

class Console_UI:
    def __init__(self):
        self.ui_type=1
        self.ui_text = ['#######################################',
        '# 1. 기간별 조회','# 2. 사망자 조회','# 3. 종료',
        '#######################################','# 메뉴를 선택해주세요. (1-3) : \n']

        self.q1_1 = '시작기간을 입력해주세요. : '
        self.q1_2 = '종료기간을 입력해주세요. : '
        self.q2 = '사망자가 몇명 이상 되는 경우 : '

    def show_result(self,data):
        for row in data:
            print('stateDt=',row['stateDt'],end=' ')
            print('decideCnt=',row['decideCnt'],end=' ')
            print('clearCnt=',row['clearCnt'],end=' ')
            print('examCnt=',row['examCnt'],end=' ')
            print('deathCnt=',row['deathCnt'],end=' ')
            print('clearCnt=',row['clearCnt'],end=' ')
            print()
        return

    def show_client(self):
        for txt in self.ui_text:
            print(txt)
        return

class TK_UI:
    pass

class XML_MGMT:

    def __init__(self):
        url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=wMtQHCpU1eLCXZ15tASu9FFMYhKKFNkiqyVNWtTA2LF9HuhFiLXDX9Q36a3sBSAfOUpWxmL%2BPJ0gdG6iX5EgQQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20200302&endCreateDt=20200723"
        res = requests.get(url)
        root = xml.fromstring(res.text)

        self.data=[]
        for items in root.iter('items'):
            #print(items.tag)
            for item in items:
                #print(item.tag)
                day={}
                for i in item:
                    #print(i.tag,i.text)
                    day[i.tag]=i.text
                self.data.append(day)

    
    def search_by_duration(self,s,e):
        return_list = []
        for i in self.data:
            if (int(i['stateDt'])>=int(s)) and (int(i['stateDt'])<=int(e)):
                return_list.append(i)
        return return_list

    def search_by_death(self,cnt):
        return_list = []
        for i in self.data:
            if int(i['deathCnt'])>=cnt:
                return_list.append(i)
        return return_list

class APP_MGMT:
    
    def __init__(self,mg,ui):
        self.mgmt = mg
        self.ui = ui

    def run(self):

        while True:
            time.sleep(1.5)

            if self.ui.ui_type == 1:
                self.ui.show_client()
            else:
                pass
            command = int(input())

            if command == 3:
                print('이용해주셔서 감사합니다. 프로그램을 종료합니다. ')
                break
            elif command == 1:
                s_idx = input(self.ui.q1_1).strip()
                e_idx = input(self.ui.q1_2).strip()

                if (int(s_idx)<20200302) or (int(e_idx)>20200723):
                    print('잘못된 조회기간 입니다. (20200302~20200723)')
                    continue
                else:
                    self.output = self.mgmt.search_by_duration(s_idx,e_idx)

                    if self.ui.ui_type==1:
                        self.ui.show_result(self.output)
                    else:
                        pass

            elif command == 2:
                d_cnt = int(input(self.ui.q2))
                self.output = self.mgmt.search_by_death(d_cnt)

                if self.ui.ui_type==1:
                        self.ui.show_result(self.output)
                else:
                    pass

            else:
                print('잘못된 메뉴선택입니다. (1-3)')
                continue


if __name__=='__main__':

    my_mgmt = XML_MGMT()
    ui_select = int(input('UI 선택 (1: Console , 2: TKinter) : \n'))
    if ui_select==1:
        ui = Console_UI()
    elif ui_select==2:
        ui = TK_UI()
    else:
        print('잘못된 값 입력. 프로그램을 종료합니다.')
        print(ui_select)
        sys.exit()

    App = APP_MGMT(my_mgmt,ui)
    App.run()
