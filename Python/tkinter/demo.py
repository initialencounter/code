# from tkinter import *
# from tkinter.messagebox import *
# import sqlite3
from tkinter import ttk
# root = Tk()
# root.geometry('700x1000')
# root.title('学生画像系统')
# Label(root, text="姓名：").place(relx=0, rely=0.05, relwidth=0.1)
# Label(root, text="身高：").place(relx=0.5, rely=0.05, relwidth=0.1)
# Label(root, text="体重：").place(relx=0, rely=0.1, relwidth=0.1)
# Label(root, text="爱好：").place(relx=0.5, rely=0.1, relwidth=0.1)

# name = StringVar()
# weight = StringVar()
# height = StringVar()
# hobby = StringVar()
# Entry(root, textvariable=name).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
# Entry(root, textvariable=weight).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
# Entry(root, textvariable=height).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
# Entry(root, textvariable=hobby).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)
# Label(root, text='学生信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

# var = StringVar()
# l = Label(root,textvariable=var,bg='green',font=('Arial',12),width=15,height=2)
# l.pack()
#
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit == False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
#
# b = Button(root,text='hit me', width = 15 ,height = 2,command=hit_me)
# b.pack()
# li = ['C', 'python', 'php', 'html', 'SQL', 'java']
# movie = ['CSS', 'jQuery', 'Bootstrap']
# listb = Listbox(root)  # 创建两个列表组件
# listb2 = Listbox(root)
# for item in li:  # 第一个小部件插入数据
#     listb.insert(0, item)
#
# for item in movie:  # 第二个小部件插入数据
#     listb2.insert(0, item)
#
# listb.pack()  # 将小部件放置到主窗口中
# listb2.pack()
#
# root.mainloop()
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫


# import tkinter as tk  # 使用Tkinter前需要先导入
#
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
#
# # 第4步，在图形界面上设定输入框控件entry并放置控件
# e1 = tk.Entry(window, show='*', font=('Arial', 14))  # 显示成密文形式
# e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
# e1.pack()
# e2.pack()
#
# # 第5步，主窗口循环显示
# window.mainloop()


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

# import tkinter as tk  # 使用Tkinter前需要先导入
#
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
#
# # 第4步，在图形界面上设定输入框控件entry框并放置
# e = tk.Entry(window, show=None)  # 显示成明文形式
# e.pack()
#
#
# # 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
# def insert_point():  # 在鼠标焦点处插入输入内容
#     var = e.get()
#     t.insert('insert', var)
#
#
# def insert_end():  # 在文本框内容最后接着插入输入内容
#     var = e.get()
#     t.insert('end', var)
#
#
# # 第6步，创建并放置两个按钮分别触发两种情况
# b1 = tk.Button(window, text='insert point', width=10,
#                height=2, command=insert_point)
# b1.pack()
# b2 = tk.Button(window, text='insert end', width=10,
#                height=2, command=insert_end)
# b2.pack()
#
# # 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
# t = tk.Text(window, height=3)
# t.pack()
#
# # 第8步，主窗口循环显示
# window.mainloop()
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

# import tkinter as tk  # 使用Tkinter前需要先导入
#
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
#
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
# l = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
# l.pack()
#
#
# # 第6步，创建一个方法用于按钮的点击事件
# def print_selection():
#     value = lb.get(lb.curselection())  # 获取当前选中的文本
#     var1.set(value)  # 为label设置值
#
#
# # 第5步，创建一个按钮并放置，点击按钮调用print_selection函数
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
#
# # 第7步，创建Listbox并为其添加内容
# var2 = tk.StringVar()
# var2.set((1, 2, 3, 4))  # 为变量var2设置值
# # 创建Listbox
# lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox
# # 创建一个list并将值循环添加到Listbox控件中
# list_items = [11, 22, 33, 44]
# for item in list_items:
#     lb.insert('end', item)  # 从最后一个位置开始加入值
# lb.insert(1, 'first')  # 在第一个位置加入'first'字符
# lb.insert(2, 'second')  # 在第二个位置加入'second'字符
# # lb.delete(2)  # 删除第二个位置的字符
# lb.pack()
#
# # 第8步，主窗口循环显示
# window.mainloop()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

# import tkinter as tk  # 使用Tkinter前需要先导入
#
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
#
# # 第4步，在图形界面上创建一个标签label用以显示并放置
# var = tk.StringVar()  # 定义一个var用来将radiobutton的值和Label的值联系在一起.
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
#
#
# # 第6步，定义选项触发函数功能
# def print_selection():
#     l.config(text='you have selected ' + var.get())
#
#
# # 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
# r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
# r1.pack()
# r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
# r2.pack()
# r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
# r3.pack()
#
# # 第7步，主窗口循环显示
# window.mainloop()

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# author:洪卫

# import tkinter as tk  # 使用Tkinter前需要先导入
#
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
#
# # 第2步，给窗口的可视化起名字
# window.title('My Window')
#
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上创建一个标签label用以显示并放置
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
#
#
# # 第6步，定义触发函数功能
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):  # 如果选中第一个选项，未选中第二个选项
#         l.config(text='I love only Python ')
#     elif (var1.get() == 0) & (var2.get() == 1):  # 如果选中第二个选项，未选中第一个选项
#         l.config(text='I love only C++')
#     elif (var1.get() == 0) & (var2.get() == 0):  # 如果两个选项都未选中
#         l.config(text='I do not love either')
#     else:
#         l.config(text='I love both')  # 如果两个选项都选中
#
#
# # 第5步，定义两个Checkbutton选项并放置
# var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
#                     command=print_selection)  # 传值原理类似于radiobutton部件
# c1.pack()
# c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()

# dataTreeview = ttk.Treeview(window, show='headings', column=('name', 'weight', 'height', 'hobby'))
# dataTreeview.column('name', width=150, anchor="center")
# dataTreeview.column('weight', width=150, anchor="center")
# dataTreeview.column('height', width=150, anchor="center")
# dataTreeview.column('hobby', width=150, anchor="center")
#
# dataTreeview.heading('name', text='姓名')
# dataTreeview.heading('weight', text='身高')
# dataTreeview.heading('height', text='体重')
# dataTreeview.heading('hobby', text='爱好')
# # 第7步，主窗口循环显示
# window.mainloop()
list = [12,21,2,13]
print("insert into student values"+str(tuple(list)))