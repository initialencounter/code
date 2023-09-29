from tkinter import *
from tkinter import messagebox
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.creatwidget()

    def creatwidget(self):
        self.label1 = Label(self, text = '用户名')
        self.label1.pack()

        v1 = StringVar()
        self.entry1 = Entry(self, textvariable = v1)
        self.entry1.pack()
        v1.set('admin')

        self.label2 = Label(self, text='密码')
        self.label2.pack()

        v2 = IntVar()
        self.entry2 = Entry(self,textvariable = v2, show = '*')
        self.entry2.pack()

        self.btn02 = Button(self, text = '登陆', command = self.songhua)
        self.btn02.pack()

    def songhua(self):
        print('用户名：{0}密码：{1}'.format(self.entry1.get(),self.entry2.get()))
        messagebox.showinfo('Message', '登陆成功')

if __name__ == '__main__':

    root = Tk()
    root.title = '我的第一个GUI'
    root.geometry('500x400+500+500')
    app = Application(root)


    root.mainloop()