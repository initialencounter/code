# import tkinter as tk
# def mousedown(event):
#     widget=event.widget
#     widget.startx=event.x # 开始拖动时, 记录控件位置
#     widget.starty=event.y
# def drag(event):
#     widget=event.widget
#     dx=event.x-widget.startx
#     dy=event.y-widget.starty
#     # winfo_x(),winfo_y() 方法获取控件的坐标
#     if isinstance(widget,tk.Wm):
#         widget.geometry("+%d+%d"%(widget.winfo_x()+dx,widget.winfo_y()+dy))
#     else:
#         widget.place(x=widget.winfo_x()+dx,y=widget.winfo_y()+dy)
# def draggable(tkwidget):
#     # tkwidget为一个控件(Widget)或一个窗口(Wm)
#     tkwidget.bind("<Button-1>",mousedown,add='+')
#     tkwidget.bind("<B1-Motion>",drag,add='+')
#
# root=tk.Tk()
# root.title("Test")
# button=tk.Button(root,text="Drag!")
# button.place(width=80,height=30)
# draggable(button)
# root.mainloop()
#
# from PIL import Image
# # img_name=['type0.png', 'type1.png','type2.png', 'type3.png', 'type4.png', 'type5.png', 'type6.png', 'type7.png', 'type8.png', 'mine.png', 'closed.png', 'mine_red.png', ]
# img_name  = ['flag.png']
# img_path = ("/Users/mac/PycharmProjects/pythonProject1/tkinter/扫雷图标/")
# list_p = []
# for i in img_name:
#     list_p.append(img_path+i)
# for infile in list_p:
#     im = Image.open(infile)
#     (x, y) = im.size  # 读取图片尺寸（像素）
#     x_s = 30  # 定义缩小后的标准宽度
#     y_s = int(y * x_s / x)  # 基于标准宽度计算缩小后的高度
#     out = im.resize((x_s, y_s), Image.ANTIALIAS)  # 改变尺寸，保持图片高品质
#     out.save('./缩放图片/{}'.format(infile.split("/")[-1]))
# # ————————————————
# 版权声明：本文为CSDN博主「肥学」的原创文章，遵循CC
# 4.0
# BY - SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https: // blog.csdn.net / jiahuiandxuehui / article / details / 122985386
import time
import tkinter as tk  # 导入tkinter库
from PIL import ImageTk
from PIL import Image as imim #要用别名
from tkinter import *
import random
import os
n,m=16,16

def leftclick(event):
    print("left")
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root = tk.Tk()
add_user = tk.Button(root, height=63, width=195 ,text="sign up a user")
add_user.place(x= 20, y = 30)
root.bind("<Button-1>", leftclick)
root.mainloop()

# root = tk.Tk()  # 建立程序主窗口
# root.title("Winesweeper")  # 设置主窗口的标题
# def callback(event):
#     print(event.x,event.y)
#     print(121)
# frame = Frame(root, width = 2560,height = 1600)
# frame.bind("<Button -1>",callback)
# root.mainloop()