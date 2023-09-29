from tkinter import *
from tkinter import messagebox
import warnings
warnings.filterwarnings('ignore')

root = Tk()
root.title = '我的当一个GUI'
root.geometry('500x400+500+500')

btn01 = Button(root)
btn01['text'] = '按钮1'
btn01.pack()


def songhua(e):
    messagebox.showinfo('Message', '送你一朵小花花')
    print('已送花')


btn01.bind('<Button-1>', songhua)

root.mainloop()
