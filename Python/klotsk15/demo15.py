import random
import time
from os import system as sys
print('已调用demo15')
class Lst_Error(Exception):
    def __init__(self):
        Exception.__init__(self)
    def __str__(self):
        return 'lst错误，无法被还原！'
# class
l,m=0,0
lst1 = []
lst2 = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
lstxy = []
dic1 = {'up':[-1,0],'down':[1,0],'right':[0,1],'left':[0,-1]}
lst_direction = []
def index_num(x):
    for i in range(4):
        for j in range(4):
            if x == lst1[i][j]:
                return [i,j]
def index_num2(x):
    for i in range(4):
        for j in range(4):
            if x == lst2[i][j]:
                return [i,j]
def move(j,k,my,mx):
        lst1[j+my][k+mx],lst1[j][k]=lst1[j][k],lst1[j+my][k+mx]
        if my==1:
            st = '下'
        if my==-1:
            st = '上'
        if mx==1:
            st = '右'
        if mx==-1:
            st = '左'
        for i in lst1:
            print(i)
        print()
        lst_direction.append(st)
        p,o = k+mx,j+my
        return [j+my,k+mx]
def move_16(y,x,l,m):
    mj, mk = l - y, m - x  # 移动到正确位置需要的距离右-上-
    for movex in range(abs(mk)):
        if mk < 0:
            y, x = move(y, x, 0, -1)  # 往左
        else:
            y, x = move(y, x, 0, 1)  # 往右
    for movey in range(abs(mj)):
        if mj > 0:
            y, x = move(y, x, 1, 0)  # 往
        else:
            y, x = move(y, x, -1, 0)  # 往下

    return [y,x]
def move2(j,k,ud,rl):
    y, x = index_num(16)  # 空的位置
    my=y-j-1
    mx=x-k-1
    if my > 0:
        for n in range(abs(my)):
            y, x = move(y, x, -1, 0)
            # print('空->上')
    if my < 0:
        for m in range(abs(my)):
            y, x = move(y, x, 1,0)
            # print('空->下')
    if mx < 0:
        for n in range(abs(mx)):
            y, x = move(y, x, 0, 1)
            # print('空->下')
    if mx > 0:
        for m in range(abs(mx)):
            y, x = move(y, x, 0, -1)
    if ud==1:#b下
        y,x= move(y,x,0,-1)
        y,x=move(y,x,-1,0)
    if ud==-1:#上
        y,x = move(y,x,-1,0)
        y, x = move(y, x, -1, 0)
        y, x = move(y, x, 0, -1)
        y, x = move(y, x, 1, 0)
    if rl==-1:#左
        y,x = move(y,x,0,-1)
        y, x = move(y, x, 0, -1)
        y, x = move(y, x, -1, 0)
        y, x = move(y, x, 0,1)
    if rl==1:#右
        y,x = move(y,x,-1,0)
        y, x = move(y, x, 0, -1)
    return [j+ud,k+rl]
def move_num_up(j,k):
    y, x = index_num(16)
    mj, mk = j-1-y, k - x  # 移动16到正确位置需要的距离右-上-
    for movey in range(abs(mj)):
        if mj < 0:
            y, x = move(y, x, -1, 0)  # 往
        else:
            y, x = move(y, x, 1, 0)  # 往下
    for movex in range(abs(mk)):
        if mk < 0:
            y, x = move(y, x, 0, -1)  # 往左
        else:
            y, x = move(y, x, 0, 1)  # 往右
    move(y,x,dic1['down'][0],dic1['down'][1])
    return [2,k]
def move_num_left(j,k):
    y, x = index_num(16)
    if y==j and x>k:
        y,x = move(y,x,dic1['down'][0],dic1['down'][1])
        y, x = move(y, x, dic1['left'][0], dic1['left'][1])
        y, x = move(y, x, dic1['left'][0], dic1['left'][1])
    mj, mk = j - y, k-1 - x  # 移动16到正确位置需要的距离右-上-
    for movex in range(abs(mk)):
        if mk < 0:
            y, x = move(y, x, 0, -1)  # 往左
        else:
            y, x = move(y, x, 0, 1)  # 往右
    for movey in range(abs(mj)):
        if mj < 0:
            y, x = move(y, x, -1, 0)  # 往
        else:
            y, x = move(y, x, 1, 0)  # 往下
    move(y, x, dic1['right'][0], dic1['right'][1])
    return [j,2]
def move_num_left2(j,k):
    y, x = index_num(16)
    mj, mk = j - y, k-1 - x  # 移动16到正确位置需要的距离右-上-
    for movex in range(abs(mk)):
        if mk < 0:
            y, x = move(y, x, 0, -1)  # 往左
        else:
            y, x = move(y, x, 0, 1)  # 往右
    for movey in range(abs(mj)):
        if mj < 0:
            y, x = move(y, x, -1, 0)  # 往
        else:
            y, x = move(y, x, 1, 0)  # 往下
def move_1(num):
    y, x = index_num(16)
    j, k = index_num(num)
    l, m = index_num2(num)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
        j, k = index_num(num)
        if j==3:
            j,k = move_num_up(j,k)
        if k==3:
            j,k = move_num_left(j,k)
        mj, mk = l - j, m - k  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                j, k = move2(j, k, 1, 0)  # 往
            else:
                j, k = move2(j, k, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                j, k = move2(j, k, 0, -1)  # 往左
            else:
                j, k = move2(j, k, 0, 1)  # 往右
        y,x = index_num(16)
        if y==j:
            y,x=move(y,x,dic1['right'][0],dic1['right'][1])
            y, x = move(y, x, dic1['right'][0], dic1['right'][1])
def move_23(num):
    y, x = index_num(16)
    j, k = index_num(num)
    l, m = index_num2(num)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
        j, k = index_num(num)
        if j==3:
            j,k = move_num_up(j,k)
        if k==3:
            j,k = move_num_left(j,k)
        j,k = index_num(num)
        if j>l:
            mj, mk = l+1 - j, m - k  # 移动到1，x需要的距离右-上
            for movey in range(abs(mj)):
                if mj > 0:
                    j, k = move2(j, k, 1, 0)  # 往
                else:
                    j, k = move2(j, k, -1, 0)  # 往下
            for movex in range(abs(mk)):
                if mk < 0:
                    j, k = move2(j, k, 0, -1)  # 往左
                else:
                    j, k = move2(j, k, 0, 1)  # 往右
            y,x = index_num(16)
            for i in range(3):
                if y != 3:
                    y,x=move(y,x,1,0)
            for i in range(3):
                if x>=k:
                    y,x=move(y,x,0,-1)
            y,x = move_16(y,x,j,k-1)
            j,k = index_num(num)
            lst = ['down', 'right', 'right', 'up', 'up', 'left', 'down']
            y, x = index_num(16)
            for i in lst:
                y, x = move(y, x, dic1[i][0], dic1[i][1])
        else:
            for i in range(abs(m-k)):
                j,k=move_num_left(j,k)
        y,x = index_num(16)
        if y==j:
            y,x=move(y,x,dic1['down'][0],dic1['down'][1])
def move_4(num):
    y, x = index_num(16)
    j, k = index_num(num)
    l, m = index_num2(num)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
        j, k = index_num(num)
        if j==3:
            j,k = move_num_up(j,k)
        if k==3:
            j,k = move_num_left(j,k)
        mj, mk = l+1 - j, m-1 - k  # 移动到1，x需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                j, k = move2(j, k, 1, 0)  # 往
            else:
                j, k = move2(j, k, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                j, k = move2(j, k, 0, -1)  # 往左
            else:
                j, k = move2(j, k, 0, 1)  # 往右
        y,x = index_num(16)
        for i in range(3):
            if y != 3:
                y, x = move(y, x, 1, 0)
        for i in range(3):
            if x >= k:
                y, x = move(y, x, 0, -1)
        if y!=j or x!=k:
            move_num_left2(j,k)
        lst = ['up','right','down','right','up','left','left','down']
        y, x = index_num(16)
        for i in lst:
            y,x = move(y,x,dic1[i][0],dic1[i][1])
        if y==j:
            y,x=move(y,x,dic1['down'][0],dic1['down'][1])
def move_12(num):
    j, k = index_num(num)  # 当前位置lst1
    l, m = index_num2(num)  # 正确位置
    y, x = index_num(16)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
    j,k = index_num(12)
    lst=['up', 'right', 'right', 'down', 'left', 'left', 'up', 'right', 'right', 'down', 'right', 'up',
                 'left', 'left', 'left',  'down', 'right', 'right', 'up', 'left', 'left', 'down']
    lst_2 = ['up', 'right', 'right', 'down', 'right', 'up', 'left', 'left', 'left', 'down']
    lst_3 = ['up','right','right','right','down','left','up','left','left','down']
    if j == 3 and k == 1:
        for i in lst:
            y, x = move(y, x, dic1[i][0], dic1[i][1])
    if j==3 and k==2:
        for i in lst_2:
            y, x = move(y, x, dic1[i][0], dic1[i][1])
    if j==3 and k==3:
        for i in lst_3:
            y, x = move(y, x, dic1[i][0], dic1[i][1])
def last():
    y,x = index_num(16)
    last_lst = ['left','left','down','right','right','right','up','left','left','left','down','right','right','right']
    for i in last_lst:
        y, x = move(y, x, dic1[i][0], dic1[i][1])
    return y

def route():

    y,x = index_num(16)
    y,x = move_16(y,x,3,0)
    route_lst = ['up', 'right', 'right', 'right','down', 'left','left', 'left', 'up', 'right', 'right']
    route_lst_2 = ['right','down','left','up']
    for i in route_lst:
        y, x = move(y, x, dic1[i][0], dic1[i][1])
    co=0
    while co<10:
        j, k = index_num(15)
        jj,kk =index_num(13)
        co+=1
        if j==2 and k==3 and jj==3 and kk==2:
            last()
            for i in range(1, len(lst_direction) + 1):
                if i % 10 == 0:
                    print()
                print([i, lst_direction[i - 1]], end='  ')

            print()
            print('已还原')
            print('步数：%s' % len(lst_direction))
            exit()
        for i in route_lst_2:
            y, x = move(y, x, dic1[i][0], dic1[i][1])
        if co>5:
            raise Lst_Error()


def finl_move():

    y, x = index_num(16)

    mj, mk = 3 - y, 3 - x  # 移动到正确位置需要的距离右-上-
    for movey in range(abs(mj)):
        if mj > 0:
            y, x = move(y, x, 1, 0)  # 往
        else:
            y, x = move(y, x, -1, 0)  # 往下
    for movex in range(abs(mk)):
        if mk < 0:
            y, x = move(y, x, 0, -1)  # 往左
        else:
            y, x = move(y, x, 0, 1)  # 往右

    route()
    return

def move_10():
    y,x  = index_num(16)
    j,k = index_num(10)
    l,m = index_num2(10)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
        j,k = index_num(10)
        lst10_31 = ['up','right','down','right','up','left','left','down','right','up','right']
        lst10_32 = ['left','left','up', 'left','down']
        lst10_33 = ['right','right','right','up','left','down','left','up','right']
        lst10_22 = ['right','up','right']
        lst10_23 = ['right','right','up','right','down','left','left','up','right']
        if j==3:
            if k==1:
                for i in lst10_31:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
            if k==2:
                for i in lst10_32:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
            if k==3:
                for i in lst10_33:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
        if j==2:
            if k==2:
                for i in lst10_22:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
            if k==3:
                for i in lst10_23:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
def move_11():
    y, x = index_num(16)
    j, k = index_num(11)
    l, m = index_num2(11)
    if j == l and k == m:
        pass
    else:
        mj, mk = 3 - y, 0 - x  # 移动到正确位置需要的距离右-上-
        for movey in range(abs(mj)):
            if mj > 0:
                y, x = move(y, x, 1, 0)  # 往
            else:
                y, x = move(y, x, -1, 0)  # 往下
        for movex in range(abs(mk)):
            if mk < 0:
                y, x = move(y, x, 0, -1)  # 往左
            else:
                y, x = move(y, x, 0, 1)  # 往右
        j, k = index_num(11)
        lst11_31 = ['up','right','down','right','up','left','left','down']  # 31 11
        lst11_32 = ['up','right','right','down','left','up','left','down']  # 32 11
        lst11_33 = ['right','right','right','up','left','down']
        lst11_23 = ['right','right','up','right']
        if j == 3:
            if k == 1:
                for i in lst11_31:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
            if k == 2:
                for i in lst11_32:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
            if k == 3:
                for i in lst11_33:
                    y, x = move(y, x, dic1[i][0], dic1[i][1])
        if j==2 and k==3:
            for i in lst11_23:
                y, x = move(y, x, dic1[i][0], dic1[i][1])


def main(lst):
    lst1 = lst
    for i in lst1:
        print(i)
    print('开始还原')
    move_1(1)
    move_23(2)
    move_23(3)
    move_4(4)
    move_1(5)
    move_23(6)
    move_23(7)
    move_4(8)
    move_1(9)
    move_10()
    move_11()
    move_12(12)
    finl_move()
    print(lst_direction)
# if __name__ == '__main__':
# lst1 = [[1,5,16,12],[10,4,14,8],[2,6,7,13],[9,3,11,15]]
# lst1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,15,14,16]]
# main(lst1)

