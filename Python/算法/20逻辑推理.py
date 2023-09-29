def leifeng():
    f = 1
    while 1:
        a = f != 3
        b = f == 2
        c = f == 4
        d = f != 4
        if a + b + c + d == 1:
            break
        else:
            f += 1
    print(f)


# leifeng()


import time


def map_o_w():  # 欧：1 美：2 亚：3 大：4 非：5
    key = 11111
    while 1:
        o = key // 10000
        m = key // 1000 % 10
        y = key // 100 % 10
        d = key // 10 % 10
        f = key % 10
        p6 = (o == m) + (o == y) + (o == d) + (o == f) \
             + (m == y) + (m == d) + (m == f) + (y == d) + (y == f) + (d == f)
        p1 = ((o == 3) + (m == 3) == 1)
        p2 = ((y == 4) + (d == 2) == 1)
        p3 = ((y == 1) + (f == 5) == 1)
        p4 = ((f == 4) + (d == 3) == 1)
        p5 = ((o == 2) + (m == 5) == 1)
        if (p1 + p2 + p3 + p4 + p5 == 5) and p6 == 0:
            print(o, m, y, d, f)
            break
        else:
            key += 1
    print('运行时间：{}'.format(time.process_time()))


# map_o_w()
def sp_meet():  # dog:o rabbit:m cat:y monkey:d fawn:f
    key = 0
    while 1:
        o = key // 10000
        m = key // 1000 % 10
        y = key // 100 % 10
        d = key // 10 % 10
        f = key % 10
        p6 = (o == m) + (o == y) + (o == d) + (o == f) \
             + (m == y) + (m == d) + (m == f) + (y == d) + (y == f) + (d == f)
        p1 = d > y
        p2 = f > o
        p3 = o > m > d
        if p1 + p2 + p3 == 3 and p6 == 0:
            print(o, m, y, d, f)
            break
        else:
            key += 1


# sp_meet()
def Murder():
    f = 1
    while 1:
        p1 = f != 1
        p2 = f == 3
        p3 = f == 4
        p4 = p3 == 0
        if (p1 + p2 + p3 + p4) == 3:
            print(f)
            break
        else:
            f += 1


# Murder()

def hotel():  # music:1 zhijia:2 msg:3 lay:4 read:5
    key = 12341
    while 1:
        a = key // 10000
        b = key // 1000 % 10
        c = key // 100 % 10
        d = key // 10 % 10
        e = key % 10
        p1 = a != 2 and a != 5
        p2 = b != 4 and b != 2
        p3 = c != 5 and c != 2
        p4 = d != 5 and d != 4
        p5 = a != 4 and d != 2
        if p1 + p2 + p3 + p4 + p5 == 5 and (a == b) + (a == c) + (a == d) + (a == e) \
                + (b == c) + (b == d) + (b == e) + (c == d) + (c == e) + (d == e) \
                + (a == 0) + (b == 0) + (c == 0) + (d == 0) + (e == 0) + (a > 5) + (b > 5) + (c > 5) + (d > 5) + (
                e > 5) == 0:
            print(a, b, c, d, e)
            break
        key += 1


# hotel()

def baizhi():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        p1 = a == (b + c + d + e == 3)
                        p2 = b == (a + c + d + e == 0)
                        p3 = c == (a + b + d + e == 1)
                        p4 = d == (a + b + c + e == 4)
                        if p1 + p2 + p3 + p4 == 4:
                            print(a, b, c, d, e)
                            break


# baizhi()
#
# listi = ['A', 'B', 'C', 'D', 'E', 'F']
# listc = ['美国', '德国', '英国', '法国', '俄罗斯', '意大利']  # 美国1 #德国2 #英国3 #法国4 #俄罗斯5 #意大利6
# listj = ['医生', '教师', '技师', '军人']
# listage = [1, 2, 3, 4, 5, 6]
# listm = ['杭州', '西安']




def country():
    for key in range(777777):
        a = key // 100000
        b = key // 10000 % 10
        c = key // 1000 % 10
        d = key // 100 % 10
        e = key // 10 % 10
        f = key % 10
        lgeal = ((a == b) + (a == c) + (a == d) + (a == e) + (a == f)
                 + (b == c) + (b == d) + (b == e) + (b == f)
                 + (c == d) + (c == e) + (c == f)
                 + (d == e) + (d == f)
                 + (e == f)
                 + (a == 0) + (b == 0) + (c == 0) + (d == 0) + (e == 0) + (f == 0)
                 + (a > 6) + (b > 6) + (c > 6) + (d > 6) + (f > 6) + (e > 6) == 0)
        p=((a==1)+(e==5)+(c==2)+(a==5)+(a==2)+(e==1)+(e==2)+(c==1)+(c==5)+(a==4)+(c==6)+(b==1)+(b==4)+(c==4))
        if lgeal and p==0:
            print(a, b, c, d, e, f)
            break
# country()




#
# print(eval(input('输入1：')))
# print(int(input('输入2：')))