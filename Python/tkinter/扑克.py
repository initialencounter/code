from tkinter import *
from tkinter import messagebox
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.creatwidget()

    def creatwidget(self):
        global img
        img = PhotoImage(file='g.gif')
        Label(self, image=img).grid(row=1, column=1, columnspan=2)
        for i in range(10):


            Label(self,image = img).grid(row=1,column=i,columnspan=2)


    def songhua(self):
        messagebox.showinfo('Message', '送你一朵小花花')

if __name__ == '__main__':
    root = Tk()
    root.title = '我的第一个GUI'
    root.geometry('500x400+500+500')
    app = Application(root)


    root.mainloop()