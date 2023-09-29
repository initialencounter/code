from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image as imim #要用别名
import random
import os
class SaoLei(Frame):
    m: int
    n: int
    k: int
    mode: int
    coordinate_list = []
    # game_space: list[list[int or str]]

    def __init__(self,Frame, m: int, n: int, k: int, mode: int):
        """
        初始化游戏
        :param m: m行, m >= 8
        :param n: n列, n >= 8
        :param k: k个雷, 10 <= k <= m*n*0.3
        :param mode: 0：手动模式，1：全自动模式 2：半自动模式
        """
        print(m,n)
        if m == 8:
            self.m = m
        else:
            messagebox.showinfo('Message', "row Error!")
            print("row Error!")
            exit(0)
        if n == 8:
            self.n = n
        else:
            messagebox.showinfo('Message', "col Error!")
            print("col Error!")
            exit(0)
        if 10 <= k <= m * n * 0.3:
            self.k = k
            self.flag = self.k
        else:
            messagebox.showinfo('Message', "k Error!")
            print("k Error!")
            exit(0)
        if mode in (0, 1, 2):
            self.mode = mode
        else:
            messagebox.showinfo('Message', "Mode Error!")
            print("Mode Error!")
            exit(0)

        # 生成区域
        self.game_space = [[0 for _ in range(n)] for _ in range(m)]
        # print(self.game_space)
        print("game_space create success!")

        # 随机雷的位置
        i = 0
        while i < self.k:
            a = random.randint(0, m - 1)
            b = random.randint(0, n - 1)
            if self.game_space[a][b] != '*':
                i += 1

                # 产生数据
                self.game_space[a][b] = '*'
                c = [-1, 0, 1]
                for x in c:
                    if 0 <= a + x < m:
                        for y in c:
                            if 0 <= b + y < n:
                                if self.game_space[a + x][b + y] != '*':
                                    self.game_space[a + x][b + y] += 1

        # 调用游戏进程
        self.game_window()

    def game_window(self):
        show_list = [['■' for _ in range(self.n)] for _ in range(self.m)]
        self.img_name = ['type0.png', 'type1.png', 'type2.png', 'type3.png', 'type4.png', 'type5.png', 'type6.png',
                    'type7.png', 'type8.png', 'mine.png', 'closed.png', 'mine_red.png', 'flag.png' ]
        self.img_path = ("/Users/mac/PycharmProjects/pythonProject1/tkinter/缩放图片/")
        self.img_type0 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[0]))
        self.img_type1 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[1]))
        self.img_type2 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[2]))
        self.img_type3 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[3]))
        self.img_type4 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[4]))
        self.img_type5 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[5]))
        self.img_type6 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[6]))
        self.img_type7 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[7]))
        self.img_type8 = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[8]))
        self.img_mine = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[9]))
        self.img_closed = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[10]))
        # self.img_mine_red = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[11]))
        self.img_flag = ImageTk.PhotoImage(imim.open(self.img_path + self.img_name[12]))

        self.img_list = []
        text = ''
        while True:
            for i in show_list:
                for j in i:
                    if j=='■':
                        self.img_list.append(Button(root, image=self.img_closed))
                    elif j==0:
                        self.img_list.append(Button(root, image=self.img_type0))
                    elif j==1:
                        self.img_list.append(Button(root, image=self.img_type1))
                    elif j==2:
                        self.img_list.append(Button(root, image=self.img_type2))
                    elif j==3:
                        self.img_list.append(Button(root, image=self.img_type3))
                    elif j==4:
                        self.img_list.append(Button(root, image=self.img_type4))
                    elif j==5:
                        self.img_list.append(Button(root, image=self.img_type5))
                    elif j==6:
                        self.img_list.append(Button(root, image=self.img_type6))
                    elif j==7:
                        self.img_list.append(Button(root, image=self.img_type7))
                    elif j==8:
                        self.img_list.append(Button(root, image=self.img_type7))
                    elif j=='□':
                        self.img_list.append(Button(root, image=self.img_flag))
            count2 = 0
            print(self.img_list)
            for i in range(len(self.img_list)-62):
                # print('bt'+str(i),((i-1)%(self.m)), ((i)//self.n))
                self.img_list[0].grid(row=(i)%self.m, column=(i)//self.n)
            # 输出画面
            # for i in range(10):
            #     print()
            # print(text)
            # print("+++" * self.n, end='+\n')
            # print(' │ ', end='')
            # for k in range(1, self.n + 1):
            #     print('%d' % (k % 10), end='  ')
            # print('\n─┼─', end='')
            # print('───' * (self.n - 1), end='─\n')
            # k = 1
            # for i in range(self.m):
            #     print(k, end='│ ')
            #     for j in range(self.n):
            #         print(show_list[i][j], end='  ')
            #     print()
            #     k = (k + 1) % 10
            if text == 'Game Over!':
                exit(0)
            text = ''

            # 检测是否结束
            row = self.m
            for i in show_list:
                if '■' not in i:
                    row -= 1
            if row == 0:
                print('Victory!')
                exit(1)

            # 输入坐标及操作
            if self.mode == 0:
                a, b, c = self.input_set()
            else:
                a, b, c = self.automatic_input(show_list)

            # 进行处理
            if c == 0:
                if self.flag > 0:
                    if show_list[a][b] == '■':
                        show_list[a][b] = '□'
                        self.flag -= 1
                    elif show_list[a][b] == '□':
                        show_list[a][b] = '■'
                        self.flag += 1
                    else:
                        text = 'Error! Is number'
                else:
                    text = 'Error! No flag'
            elif c == 1:
                if show_list[a][b] == '■':
                    if self.game_space[a][b] == '*':
                        show_list[a][b] = '*'
                        text = 'Game Over!'
                    elif self.game_space[a][b] == 0:
                        show_list[a][b] = self.game_space[a][b]
                        self.look_zero(a, b, show_list)
                    else:
                        show_list[a][b] = self.game_space[a][b]
                else:
                    text = 'Error! No Click'
            elif c == 2:
                if show_list[a][b] == '■':
                    show_list[a][b] = '?'
                elif show_list[a][b] == '?':
                    show_list[a][b] = '■'
                else:
                    text = 'Error! Open'

    def look_zero(self, a: int, b: int, show_list):
        for i in range(a - 1, a + 2):
            for j in range(b - 1, b + 2):
                if 0 <= i < self.m and 0 <= j < self.n:
                    if show_list[i][j] == '■':
                        if self.game_space[i][j] == 0:
                            show_list[i][j] = 0
                            self.look_zero(i, j, show_list)
                        else:
                            show_list[i][j] = self.game_space[i][j]

    def input_set(self):
        a = int(input("输入行："))
        b = int(input("输入列："))
        c = int(input("操作（0：插旗； 1：点击； 2：标记）："))
        if not (0 < a <= self.m and 0 < b <= self.n and c in (0, 1, 2)):
            a, b, c = self.input_set()
            a += 1
            b += 1
        return a - 1, b - 1, c

if __name__ == '__main__':

    root = Tk()
    root.title = '我的第一个GUI'
    root.geometry('500x400+500+500')
    app = SaoLei(root,8,8,10,0)


    root.mainloop()