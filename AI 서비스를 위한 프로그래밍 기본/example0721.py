from tkinter import *
from tkinter import messagebox

class Login():
    
    def __init__(self,master):
        self.master = master
        master.title('Login Page')
        master.geometry('300x150')
        self.id_l = Label(self.master,text='ID : ',width=15)
        self.id_l.grid(row=0,column=0)
        self.id_e = Entry(self.master,width=25)
        self.id_e.grid(row=0,column=1)
        self.log_b = Button(self.master,text='Log in',width=15,command=self.check_log)
        self.log_b.grid(row=1,column=0)
        self.exit_b = Button(self.master,text='Exit',width=25,command=quit)
        self.exit_b.grid(row=1,column=1)
        
    def check_log(self):
        check_id = self.id_e.get()
        if check_id == '1':
            messagebox.showinfo('Log status','Successfully logged in')
        else:
            messagebox.showerror('Log status','Log in failed, check your ID or PW')

if __name__ == '__main__':
    root=Tk()
    gui=Login(root)
    root.mainloop()