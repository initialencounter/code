class Move_16:
    def __init__(self,other,my,mx):
        self.lst1 = other.lst1
        self.yx = other.yx
        self.my = my
        self.mx = mx
    def move__1(self):
        y,x = self.yx
        my = self.my
        mx = self.mx
        self.lst1[y][x],self.lst1[y+my][x+mx]=self.lst1[y+my][x+mx],self.lst1[y][x]
        # self.yx = [y+my,x+mx]
        print('\n\n\n')
        print(self.lst1)
class Lst:
    dic1 = {'u': [-1, 0], 'd': [1, 0], 'r': [0, 1], 'l': [0, -1]}
    lst2 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]
    def __init__(self,lst1,x):
        self.lst1 = lst1
        self.x = x
        for i in range(4):
            for j in range(4):
                if 16 == lst1[i][j]:
                    self.yx = [i, j]

        mj, mk = 3-self.yx[0],3-self.yx[1]
        for movey in range(abs(mj)):
            if mj > 0:
                self.move_16(1, 0)# 往
            else:
                self.move_16(-1, 0)  # 往下

        for movex in range(abs(mk)):
            if mk < 0:
                self.move_16(0, -1)  # 往左
            else:
                self.move_16(0, 1)  # 往右

        for i in range(4):
            for j in range(4):
                if x == lst1[i][j]:
                    self.jk = [i, j]
        for i in range(4):
            for j in range(4):
                if x == Lst.lst2[i][j]:
                    self.lm = [i, j]

    def move_16(self,my,mx):
        y, x = self.yx
        self.lst1[y][x], self.lst1[y + my][x + mx] = self.lst1[y + my][x + mx], self.lst1[y][x]
        self.yx = [y+my,x+mx]
        print(self.lst1)
        return self
class Alloction:
    def __init__(self,lst1):
        self.lst1 = lst1
    def allocation(self):
        x = self.lst1.x
        if x in [1,5,9]:
            Move159(self.lst1).do()
        elif x in [2,3,6,7]:
            Move2367(self.lst1).do()
        elif x in [4,8]:
            return Move48(self.lst1).do()
        elif x == 10:
            return Move10(self.lst1).do()
        elif x == 11:
            return Move10(self.lst1).do()
        elif x == 12:
            return Move10(self.lst1).do()
        else:
            return MoveFinl(self.lst1).do()

class Move159():
    def __init__(self,other):
        self.other = other
    def do(self):
        if self.other.lm == self.other.jk:
            print(self.other.yx,self.other.lm)
            print('{0}已还原'.format(self.other.x))
        else:
            ls = ['u','u','l']
            for i in ls:
                self.other.move_16(Lst.dic1[i][0],Lst.dic1[i][1])
        return 1
class Move2367():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))

class Move48():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))
class Move10():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))
class Move11():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))
class Move12():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))
class MoveFinl():
    def __init__(self, other):
        self.other = other

    def do(self):
        if self.other.lm == self.other.jk:
            print('{0}已还原'.format(self.other.x))

for i in range(1,14):
    ll = Lst([[16,1,3,4],[8,7,6,5],[12,11,10,9],[13,15,2,14]],i)
    llst = Alloction(ll)
    llst.allocation()
    break