from turtle import *
from time import *


def draw(b):
    left(120)
    fd(b)


def new_list(b, c):
    list1 = []
    list2 = []
    while b > c:
        list1.append(b)
        b = b / 2
    list1.reverse()
    for i in list1:
        list2.append(i)
        list2.append(i)
        list2.append(i)
    c = 3
    n = 0
    for i in range(len(list1)):
        if i < len(list1) - 1:
            list5 = list2[0:c + n]
            list2.insert(c + 1 + n, list5)
            list2.insert(c + 3 + n, list5)
            c += 4
            n += 1
    list2 = str(list2).replace('],', ',').replace(',[', ',').replace('[', '').replace(']', '').replace(' ', '').split(
        ',')
    print(list2)
    return list2


def main():
    speed(0)
    for i in new_list(240, 10):
        draw(int(float(i)))
    sleep(3)


if __name__ == '__main__':
    main()
