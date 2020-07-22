# from tkinter import *
# from tkinter import messagebox

# def key_press(event):
#     print('pressed',repr(event.char))

# master = Tk()

# frame = Frame(master,width=100,height=100)
# frame.bind('<Key>',key_press)
# frame.bind('<Button-1>',c_l)

# master.mainloop()

# #-------------------------------------------------

import sqlite3

def insertion(table_name,*args):
    val=''
    for item in args:
        if type(item)!=str:
            val+=str(item)+','
        else:
            val+='\''+item+'\','
    val=val[:-1]
    command = f'''INSERT INTO {table_name} VALUES({val})'''
    return command 


#print(insertion('COMPANY',2,'강감찬',25,'texas',1515.65))
# sql = '''CREATE TABLE COMPANY2(
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     AGE INT NIT NULL,
#     ADDRESS CHAR(50),
#     SALARY REAL);'''

# sql1 = '''INSERT INTO COMPANY2 VALUES(2,'강감찬',25,'TEXAS',15000.0)'''

# sql2 = '''SELECT * FROM COMPANY'''

#cursor = conn.execute(sql2)
#for row in cursor:
#    print(*row)

conn = sqlite3.Connection('c:\\sqlite\\test2.db')
print('conn ok')
conn.execute(insertion('COMPANY',5,'이동재',28,'Seoul',345.543))
conn.commit()
conn.close()
print('Successfuly executed')


# import sqlite3
# from tkinter import *
# from tkinter import messagebox

# master=Tk()

# def insertion():
#     conn = sqlite3.connect('c:\\sqlite\\test2.db')
#     vals=''
#     vals+=str(id_e.get())+','
#     vals+='"'+name_e.get()+'",'
#     vals+=str(age_e.get())+','
#     vals+='"'+address_e.get()+'",'
#     vals+=str(salary_e.get())
#     command = f'INSERT INTO COMPANY VALUES({vals})'
#     print(command)
#     conn.execute(command)
#     conn.commit()
#     conn.close()
#     messagebox.showinfo('변경 사항','새로운 행이 추가되었습니다.')

# id_lb = Label(master,text='ID = ')
# name_lb = Label(master,text='Name = ')
# age_lb = Label(master,text='AGE = ')
# address_lb = Label(master,text='ADDRESS = ')
# salary_lb = Label(master,text='SALARY = ')

# id_lb.grid(row=0,column=0)
# name_lb.grid(row=0,column=1)
# age_lb.grid(row=0,column=2)
# address_lb.grid(row=0,column=3)
# salary_lb.grid(row=0,column=4)

# id_e = Entry(master)
# name_e = Entry(master)
# age_e = Entry(master)
# address_e = Entry(master)
# salary_e = Entry(master)

# id_e.grid(row=1,column=0)
# name_e.grid(row=1,column=1)
# age_e.grid(row=1,column=2)
# address_e.grid(row=1,column=3)
# salary_e.grid(row=1,column=4)

# save_b = Button(master,text='Save',bg='green',width=10,command=insertion)
# save_b.grid(row=0,column=5)
# find_b = Button(master,text='Find',bg='yellow',width=10)
# find_b.grid(row=1,column=5)
# exit_b = Button(master,text='Exit',bg='red',width=10,command=quit)
# exit_b.grid(row=2,column=5)

# master.mainloop()