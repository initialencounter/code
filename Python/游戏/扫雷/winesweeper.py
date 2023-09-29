import time
import tkinter as tk  # 导入tkinter库
from PIL import ImageTk
from PIL import Image as imim #要用别名
from tkinter import *
import random
import os
def leftclick(event):
    print("left")
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

root = tk.Tk()  # 建立程序主窗口
root.title("Winesweeper")  # 设置主窗口的标题


n,m,k,mode = 22,16,99,0
# add_user = tk.Label(root, height=m*35, width=n*35 ,text="sign up a user")
# add_user.place(x= 20, y = 30)

show_list = [['■' for _ in range(n)] for _ in range(m)]
text = ''
# input_text= input()
# m = input_text.split(' ')[0]
# n = input_text.split(' ')[1]
# k = input_text.split(' ')[2]
def random_mine(m,n,k):
    game_space = [[0 for _ in range(n)] for _ in range(m)]
    i = 0
    while i < k:
        a = random.randint(0, m - 1)
        b = random.randint(0, n - 1)
        if game_space[a][b] != '*':
            i += 1

            # 产生数据
            game_space[a][b] = '*'
            c = [-1, 0, 1]
            for x in c:
                if 0 <= a + x < m:
                    for y in c:
                        if 0 <= b + y < n:
                            if game_space[a + x][b + y] != '*':
                                game_space[a + x][b + y] += 1
    # print(game_space)
    return game_space
def automatic_input(show_list):
    pass

flag = k
game_space = random_mine(n,m,k)
def look_zero(self, a: int, b: int, show_list):
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            if 0 <= i < m and 0 <= j < n:
                if show_list[i][j] == '■':
                    if game_space[i][j] == 0:
                        show_list[i][j] = 0
                        look_zero(i, j, show_list)
                    else:
                        show_list[i][j] = game_space[i][j]


# if text == 'Game Over!':
#     exit(0)
# text = ''

# 检测是否结束
# row = m
# for i in show_list:
#     if '■' not in i:
#         row -= 1
# if row == 0:
#     print('Victory!')
#     exit(1)

# # 输入坐标及操作
# if mode == 0:
#     a, b, c = callback(event)
# else:
#     a, b, c = automatic_input(show_list)
#
# # 进行处理
# if c == 0:
#     if flag > 0:
#         if show_list[a][b] == '■':
#             show_list[a][b] = '□'
#             flag -= 1
#         elif show_list[a][b] == '□':
#             show_list[a][b] = '■'
#             flag += 1
#         else:
#             text = 'Error! Is number'
#     else:
#         text = 'Error! No flag'
# elif c == 1:
#     if show_list[a][b] == '■':
#         if game_space[a][b] == '*':
#             show_list[a][b] = '*'
#             text = 'Game Over!'
#         elif game_space[a][b] == 0:
#             show_list[a][b] = game_space[a][b]
#             look_zero(a, b, show_list)
#         else:
#             show_list[a][b] = game_space[a][b]
#     else:
#         text = 'Error! No Click'
# elif c == 2:
#     if show_list[a][b] == '■':
#         show_list[a][b] = '?'
#     elif show_list[a][b] == '?':
#         show_list[a][b] = '■'
#     else:
#         text = 'Error! Open'
#







for i in game_space:
    print(i)
show_list = game_space
xy = 2
for i in range(len(show_list)):
    for j in range(len(show_list[i])):
        if show_list[i][j] == '■':
            Button(root, text='■', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0, pady=0)
        elif show_list[i][j] == 0:
            Button(root, text=' ', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0, pady=0)
        elif show_list[i][j] == 1:
            Button(root, text='1', fg="blue", width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                        pady=0)
        elif show_list[i][j] == 2:
            Button(root, text='2', fg="green", width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                         pady=0)
        elif show_list[i][j] == 3:
            Button(root, text='3', fg="red", width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                       pady=0)
        elif show_list[i][j] == xy:
            Button(root, text='xy', fg='#0033FF', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                            pady=0)
        elif show_list[i][j] == 5:
            Button(root, text='5', fg='#993333', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                           pady=0)
        elif show_list[i][j] == 6:
            Button(root, text='6', fg='#33CCFF', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                           pady=0)
        elif show_list[i][j] == 7:
            Button(root, text='7', fg='black', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                         pady=0)
        elif show_list[i][j] == 8:
            Button(root, text='8', fg='gray', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0,
                                                                        pady=0)
        elif show_list[i][j] == '*':
            Button(root, text='*', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0, pady=0)
        elif show_list[i][j] == '□':
            Button(root, text='!', width=xy, height=xy).grid(row=i, column=j, ipadx=0, ipady=0, padx=0, pady=0)

# root = tk.Tk()

root.mainloop()