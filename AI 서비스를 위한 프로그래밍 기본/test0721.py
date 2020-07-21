from tkinter import *
from tkinter import messagebox

# top=Tk()
# top.title('Practicing Window programming')
# top.geometry('600x600')
# top.resizable(width=True,height=True)

# photo = PhotoImage(file='cat2.gif')
# lb1 = Label(top,text = 'Hi this is tkinter')
# lb2 = Label(top,text = 'Hi this is tkinter',font=('궁서체',30),fg='blue')
# lb3 = Label(top,text = 'Hi this is tkinter',bg='yellow',width=20,height=12,anchor=CENTER)
# lb4 = Label(top,image=photo,width=100,height=100)


# btnlist = [0]*3
# for i in range(3):
#     btnlist[i]=Button(top,text=f'버튼 {i+1}')

# btnlist[0].pack(side=TOP,fill=X,padx=15,pady=10)
# btnlist[1].pack(side=LEFT,ipadx=15,ipady=10)
# btnlist[2].pack(side=RIGHT,fill=X)

# def myf():
#     messagebox.showinfo('로그인 버튼','정말 로그인하시겠습니까?')

# def mycheck():
#     if chk.get():
#         messagebox.showinfo('체크 알림','체크박스가 현재 켜저있습니다.')
#     else:
#         messagebox.showinfo('체크 알림','체크박스가 현재 꺼저있습니다.')

# b1 = Button(top,text='Login',command=myf)
# b2 = Button(top,text='Exit',command=quit)
# chk=IntVar()
# b3 = Checkbutton(top,text='동의하시겠습니까?',variable=chk,command=mycheck)

# lb1.pack()
# lb2.pack()
# lb3.pack()
# lb4.pack()
# b1.pack()
# b3.pack()
# b2.pack()
# top.mainloop()


# #------------------------------------------------------------------------------------
# def mycal():
#     n1=int(e1.get())
#     n2=int(e2.get())
#     lb3.configure(text=f'{n2+n1}')
#     print(n1+n2)

# window = Tk()
# window.title('Practicing window programming')
# window.resizable(width=True,height=True)
# window.geometry('300x150')
# lb1 = Label(window,text='Num1')
# lb2 = Label(window,text='Num2')
# lb1.grid(row=0,column=0)
# lb2.grid(row=1,column=0)
# e1 = Entry(window)
# e2 = Entry(window)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# lb3 = Label(window,text='Result')
# lb3.grid(row=4,column=1)
# b1 = Button(window,text='Calculate',command=mycal)
# b1.grid(row=3,column=1)

# window.mainloop()
# #------------------------------------------------------------------------------------

# def mycopy():
#     s = input.get()
#     lb2.configure(text=s)

# t = Tk()
# input = StringVar()
# t.title('Login Page')

# lb1 = Label(t,text='ID')
# lb1.grid(row=0,column=0)
# e1 = Entry(t,textvariable=input)
# e1.grid(row=0,column=1)
# b1 = Button(t,text='copy',command=mycopy)
# b1.grid(row=1,column=0)
# lb2 = Label(t,text='copied text')
# lb2.grid(row=1,column=1)
# b2 = Button(t,text='Exit',command=quit)
# b2.grid(row=2,column=0)
# t.mainloop()
# #--------------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox

def checkval():
    ID = id_e.get()
    PW = pw_e.get()
    if not ID or not PW:
        messagebox.showerror('로그인 화면','아이디나 패스워드 중 비어있는 곳이 있습니다.')
        return
    
    if chk.get():
        if ID=='1' and PW=='1':
            messagebox.showinfo('로그인 화면','로그인에 성공하였습니다. 사용자 정보는 기억됩니다.')
        else:
            messagebox.showerror('로그인 화면','로그인에 실패하였습니다.')
    else:
        if ID=='1' and PW=='1':
            messagebox.showinfo('로그인 화면','로그인에 성공하였습니다.')
        else:
            messagebox.showerror('로그인 화면','로그인에 실패하였습니다.')

def remem():
    if chk.get():
        messagebox.showinfo('','사용자를 기억합니다.')
    else:
        messagebox.showinfo('','사용자를 기억하지 않습니다.')


T = Tk()
T.title('Login page')
T.resizable(width=False,height=False)
T.geometry('300x150')

id_lb = Label(T,text='ID : ',bg='gray',width=15)
id_e = Entry(T)
id_lb.grid(row=0,column=0)
id_e.grid(row=0,column=1)

pw_lb = Label(T,text='PW : ',bg='gray',width=15)
pw_e = Entry(T)
pw_lb.grid(row=1,column=0)
pw_e.grid(row=1,column=1)

chk=IntVar()
remember_ck = Checkbutton(T,text='Remember me',variable=chk,command=remem)
remember_ck.grid(row=2,column=0)
log_b = Button(T,text='Log in',command=checkval)
log_b.grid(row=2,column=1)
exit_b = Button(T,text='Exit',command=quit)
exit_b.grid(row=2,column=2)

T.mainloop()