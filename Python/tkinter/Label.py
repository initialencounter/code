from tkinter import *
from tkinter import messagebox


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.creatwidget()

    def creatwidget(self):
        self.label1 = Label(self,text = '标签1', width = 6, height = 2, bg = 'black',fg = 'white'
                            ,font = ('黑体',20))
        self.label1.pack()
        global img
        img = PhotoImage(file = './g.gif')
        # self.label2 = Label(self, image = img)
        # self.label2.pack()
        self.label3 = Label(self,text = '第一行文字\n第二行文字\n末尾',borderwidth = 1,
                            relief = 'solid',justify='left')
        self.label3.pack()
        self.btn = Button(self,image = img,command = self.songhua)
        self.btn.pack()
    def songhua(self):
        messagebox.showinfo('Message', '送你一朵小花花')


if __name__ == '__main__':
    root = Tk()
    root.geometry('2000x1800+100+50')
    app = Application(root)
    root.mainloop()