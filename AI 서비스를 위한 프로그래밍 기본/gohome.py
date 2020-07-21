import time
from tkinter import *

def t_cal():
    t = t=time.localtime()
    tot=0
    End = 18*3600
    tot+=t.tm_sec
    tot+=t.tm_min*60
    tot+=t.tm_hour*3600
    rest=End-tot
    r_h=rest//3600
    rest%=3600
    r_m = rest//60
    rest%=60
    r_s=rest
    lb2.configure(text=f'남은 시간: {r_h}시 {r_m}분 {r_s}초')

T = Tk()
T.title('우리는 언제 집에 갈 수 있을까?')
T.geometry('650x650')
T.resizable(width=False,height=False)

img = PhotoImage(file='clock.gif')
lb1 = Label(T,image=img,width=650,height=420)
lb1.pack(side=TOP)
b1=Button(T,text='남은 시간 확인하기',bg='black',fg='white',command=t_cal,width=300,height=5)
lb2 = Label(T,text='남은 시간: 0시 0분 0초',bg='yellow',width=300,height=5)
b2 = Button(T,text='종료',command=quit,bg='red',width=300,height=5)
b1.pack(side=TOP)
lb2.pack(side=TOP)
b2.pack(side=TOP)
T.mainloop()