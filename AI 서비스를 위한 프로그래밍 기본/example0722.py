import sqlite3
from tkinter import *
from tkinter import messagebox

def insertion():
    con_db = sqlite3.connect('c:\\sqlite\\test2.db')
    cur = con_db.cursor()
    command = f"SELECT * FROM user WHERE ID = {int(id_e.get())} AND NAME = '{name_e.get()}'"
    cur.execute(command)
    if not cur.fetchall():
        command = f"INSERT INTO user VALUES({int(id_e.get())},'{name_e.get()}')"
        cur.execute(command)
        messagebox.showinfo('변경 사항',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보로 DB에 추가 되었습니다.')
        con_db.commit()
    else:
        messagebox.showerror('변경 사항',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보가 이미 등록되어 있습니다.')
    con_db.close()

def update():
    con_db = sqlite3.connect('c:\\sqlite\\test2.db')
    cur = con_db.cursor()
    command = f"SELECT * FROM user WHERE ID = {int(id_e.get())}"
    cur.execute(command)
    if cur.fetchall():
        command = f"UPDATE user SET NAME = '{name_e.get()}' WHERE ID = {int(id_e.get())}"
        cur.execute(command)
        con_db.commit()
        messagebox.showinfo('변경 사항',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보로 변경되었습니다.')
    else:
        messagebox.showerror('변경 사항',f'ID : {id_e.get()} 의 정보는 현재 등록되어 있지 않습니다.')

    con_db.close()

def deletion():
    con_db = sqlite3.connect('c:\\sqlite\\test2.db')
    cur = con_db.cursor()
    command = f"SELECT * FROM user WHERE ID = {int(id_e.get())} AND NAME = '{name_e.get()}'"
    cur.execute(command)
    if cur.fetchall():
        command = f"DELETE FROM user WHERE ID = {int(id_e.get())} AND NAME = '{name_e.get()}'"
        cur.execute(command)
        con_db.commit()
        messagebox.showinfo('변경 사항',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보가 삭제되었습니다.')
    else:
        messagebox.showerror('변경 사항',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보는 현재 등록되어 있지 않습니다.')

    con_db.close()

def search():
    con_db = sqlite3.connect('c:\\sqlite\\test2.db')
    cur = con_db.cursor()
    command = f"SELECT * FROM user WHERE ID = {int(id_e.get())} AND NAME = '{name_e.get()}'"
    cur.execute(command)
    if cur.fetchall():
        messagebox.showinfo('검색 결과',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보가 등록되어 있습니다.')
    else:
        messagebox.showerror('검색 결과',f'ID : {id_e.get()}, NAME : {name_e.get()} 의 정보는 현재 등록되어 있지 않습니다.')

    con_db.close()

def show_all():
    con_db = sqlite3.connect('c:\\sqlite\\test2.db')
    cur = con_db.cursor()
    command = f"SELECT * FROM user"
    cur.execute(command)
    while True:
        info = cur.fetchone()
        if not info:
            break
        print(f'ID = {info[0]}  ,  NAME = {info[1]}')
    con_db.close()

master=Tk()
id_L = Label(master,text='ID : ');id_L.grid(row=0,column=0)
name_L = Label(master,text='NAME : ');name_L.grid(row=1,column=0)
id_e = Entry(master);id_e.grid(row=0,column=1)
name_e = Entry(master);name_e.grid(row=1,column=1)
insert_b = Button(master,text='Add to DB',width=12,command=insertion,fg='green');insert_b.grid(row=0,column=2)
update_b = Button(master,text='Update to DB',width=12,command=update,fg='blue');update_b.grid(row=1,column=2)
delete_b = Button(master,text='Delete from DB',width=12,command=deletion,fg='red');delete_b.grid(row=2,column=2)
search_b = Button(master,text='Search from DB',width=12,command=search,);search_b.grid(row=3,column=2)
exit_b = Button(master,text='EXIT',width=15,command=quit,bg='red');exit_b.grid(row=3,column=1)
all_b = Button(master,text='Print all on terminal',width=15,command=show_all,fg='white',bg='skyblue');all_b.grid(row=2,column=1)

master.mainloop()