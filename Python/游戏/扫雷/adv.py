import random
import time


class SaoLei:
    m: int
    n: int
    k: int
    mode: int
    coordinate_list = []
    # game_space: list[list[int or str]]

    def __init__(self, m: int, n: int, k: int, mode: int):
        """
        初始化游戏
        :param m: m行, m >= 8
        :param n: n列, n >= 8
        :param k: k个雷, 10 <= k <= m*n*0.3
        :param mode: 0：手动模式，1：全自动模式 2：半自动模式
        """
        if m >= 8:
            self.m = m
        else:
            print("row Error!")
            exit(0)
        if n >= 8:
            self.n = n
        else:
            print("col Error!")
            exit(0)
        if 10 <= k <= m * n * 0.3:
            self.k = k
            self.flag = self.k
        else:
            print("k Error!")
            exit(0)
        if mode in (0, 1, 2):
            self.mode = mode
        else:
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
        text = ''
        while True:
            # 输出画面
            for i in range(10):
                print()
            print(text)
            print("+++" * self.n, end='+\n')
            print(' │ ', end='')
            for k in range(1, self.n + 1):
                print('%d' % (k % 10), end='  ')
            print('\n─┼─', end='')
            print('───' * (self.n - 1), end='─\n')
            k = 1
            for i in range(self.m):
                print(k, end='│ ')
                for j in range(self.n):
                    print(show_list[i][j], end='  ')
                print()
                k = (k + 1) % 10
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





    # def automatic_input(self, show_list: list[list]
    #
    #                     ):
    #     """
    #     自动化方法
    #     :param show_list:
    #     :return:a,b,c
    #     """
    #     if self.coordinate_list:
    #         a = self.coordinate_list.pop()
    #         print("选定位置【%d, %d】, 操作为：%d" % (a[0] + 1, a[1] + 1, a[2]))
    #         # time.sleep(0.5)
    #         return a[0], a[1], a[2]
    #
    #     for i in range(self.m):
    #         for j in range(self.n):
    #             if type(show_list[i][j]) is not str and show_list[i][j] > 0:
    #                 z = show_list[i][j]
    #                 for x in range(i - 1, i + 2):
    #                     for y in range(j - 1, j + 2):
    #                         if 0 <= x < self.m and 0 <= y < self.n:
    #                             if show_list[x][y] == '□':
    #                                 z -= 1
    #                             elif show_list[x][y] == '■':
    #                                 self.coordinate_list.append([x, y])
    #                 if z == 0:
    #                     for p in range(len(self.coordinate_list)):
    #                         self.coordinate_list[p].append(1)
    #                 elif z == len(self.coordinate_list):
    #                     for p in range(len(self.coordinate_list)):
    #                         self.coordinate_list[p].append(0)
    #                 else:
    #                     self.coordinate_list.clear()
    #
    #                 if self.coordinate_list:
    #                     a = self.coordinate_list.pop()
    #                     print("选定位置【%d, %d】, 操作为：%d" % (a[0] + 1, a[1] + 1, a[2]))
    #                     # time.sleep(0.5)
    #                     return a[0], a[1], a[2]
    #
    #     # 进入高级计算
    #     print("调用高级计算处理，请等候...")
    #     self.advanced_automatic_input(show_list)
    #     if self.coordinate_list:
    #         print("计算完成!生成操作:")
    #         for mmm in self.coordinate_list:
    #             print("\t坐标【%d，%d】，操作：%d" % (mmm[0] + 1, mmm[1] + 1, mmm[2]))
    #         print("========================")
    #         a = self.coordinate_list.pop()
    #         print("选定位置【%d, %d】, 操作为：%d" % (a[0] + 1, a[1] + 1, a[2]))
    #         # time.sleep(0.5)
    #         return a[0], a[1], a[2]
    #
    #     # 无法确定，随机选择位置
    #     elif self.mode == 1:
    #         a = random.randint(0, self.m - 1)
    #         b = random.randint(0, self.n - 1)
    #         while show_list[a][b] != '■':
    #             a = random.randint(0, self.m - 1)
    #             b = random.randint(0, self.n - 1)
    #         else:
    #             print("无法确定位置，随机选择【%d, %d】点开" % (a + 1, b + 1))
    #             # time.sleep(2)
    #             return a, b, 1
    #     else:
    #         print("无法确定位置，请手动输入。 提示：还有【%d】个" % self.flag)
    #         return self.input_set()
    #
    # def advanced_automatic_input(self, show_list: list[list]
    #
    #                              ):
    #     processed_list = []
    #     set_dic = dict()
    #     for i in show_list:
    #         processed_list.append(i.copy())
    #
    #     # 初步处理
    #     for i in range(self.m):
    #         for j in range(self.n):
    #             if type(processed_list[i][j]) is int and processed_list[i][j] > 0:
    #                 c = set()
    #                 for p in range(i - 1, i + 2):
    #                     for q in range(j - 1, j + 2):
    #                         if 0 <= p < self.m and 0 <= q < self.n:
    #                             if processed_list[p][q] == '□':
    #                                 processed_list[i][j] -= 1
    #                             elif processed_list[p][q] == '■':
    #                                 c.add((p, q))
    #                 if c:
    #                     set_dic[tuple(c)] = processed_list[i][j]
    #
    #     # 寻找子集
    #     key_list = list(set_dic.keys())
    #     for i in range(len(key_list)):
    #         for j in range(i + 1, len(key_list)):
    #             if len(key_list[i]) < len(key_list[j]):
    #                 p = i
    #                 q = j
    #             elif len(key_list[i]) > len(key_list[j]):
    #                 p = j
    #                 q = i
    #             else:
    #                 continue
    #
    #             if set(key_list[p]).issubset(set(key_list[q])):
    #                 d = list(set(key_list[q]) - set(key_list[p]))
    #                 if set_dic[key_list[q]] - set_dic[key_list[p]] == 0:
    #                     for k in d:
    #                         e = list(k)
    #                         e.append(1)
    #                         self.coordinate_list.append(e)
    #                 elif set_dic[key_list[q]] - set_dic[key_list[p]] == len(d):
    #                     for k in d:
    #                         e = list(k)
    #                         e.append(0)
    #                         self.coordinate_list.append(e)
    #

# 传参【 m行，n列， k个雷， mode：0、手动； 1、全自动; 2、半自动】，可自定义
# 简单 8 8 10
# 一般 16 16 40
# 困难 16 32 99
game = SaoLei(16, 32, 99, 0)

