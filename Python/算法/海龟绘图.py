import time
from turtle import *
from time import *


def main():
    ht()
    speed('normal')
    pensize(50);
    pencolor('LightGreen')
    up();
    goto(-400, -200);
    down();
    goto(400, -200)
    # 栅栏
    pensize(20);
    pencolor('GoldEnrod')
    up();
    goto(-400, -150);
    down();
    goto(400, -150)
    up();
    goto(-250, -200);
    down();
    goto(-250, -100)
    up();
    goto(-100, -200);
    down();
    goto(-100, -100)
    up();
    goto(30, -200);
    down();
    goto(30, -100)
    up();
    goto(300, -200);
    down();
    goto(300, -100)
    # 树
    pensize(30);
    pencolor('OLive')
    up();
    goto(-150, -200);
    down();
    goto(-150, -120)
    pensize(1);
    color('ForestGreen')
    up();
    goto(-80, -120);
    down()
    begin_fill();
    seth(60);
    circle(80, steps=3);
    end_fill()
    up();
    goto(-95, -50);
    down()
    begin_fill();
    seth(60);
    circle(60, steps=3);
    end_fill()
    up();
    goto(-110, 0);
    down()
    begin_fill();
    seth(60);
    circle(40, steps=3);
    end_fill()
    # 墙体
    pensize(1);
    color('RoyalBlue')
    up();
    home();
    fd(70);
    right(90);
    down()
    begin_fill();
    fd(200);
    left(90);
    fd(200);
    left(90);
    fd(200);
    end_fill()
    # 烟囱
    pensize(30);
    pencolor('DimGray')
    up();
    goto(230, 30);
    down();
    goto(230, 120)
    # 房顶
    pensize(1);
    color('DeepPink');
    up();
    home();
    down()
    begin_fill();
    left(30);
    fd(200);
    right(60);
    fd(200);
    home();
    end_fill()
    # 窗户
    color('Violet');
    up();
    goto(160, -90);
    down()
    begin_fill();
    seth(45);
    circle(50, steps=4);
    end_fill()
    # 门
    color('Chocolate');
    up();
    goto(250, -200);
    down();
    seth(90)
    begin_fill()
    fd(120);
    left(90);
    fd(60);
    left(90);
    fd(120);
    left(90);
    fd(60)
    end_fill()
    # 炊烟
    up();
    goto(250, 160);
    dot(30, 'AliceBlue')
    goto(270, 200);
    dot(20, 'AliceBlue')
    goto(300, 220);
    dot(10, 'AliceBlue')
    # 太阳
    goto(-260, 250);
    dot(80, 'Gold')


# main()
def pentagram():
    pensize(1);
    speed('normal')
    color('Red')
    begin_fill()
    fd(100);
    right(180 - 36);
    fd(100);
    left(180 - 108)
    fd(100);
    right(180 - 36);
    fd(100);
    left(180 - 108)
    fd(100);
    right(180 - 36);
    fd(100);
    left(180 - 108)
    fd(100);
    right(180 - 36);
    fd(100);
    left(180 - 108)
    fd(100);
    right(180 - 36);
    fd(100);
    left(180 - 108)
    end_fill()
    sleep(2)


# pentagram()
def taiqi():
    ht()
    pensize(1);
    speed(20)
    color('Black')
    begin_fill()
    circle(200, 180, 1000)
    circle(100, 180, 1000)
    circle(-100, 180, 1000)
    end_fill()
    circle(-200, 180, 1000)
    up(), goto(0, 250), down()
    color('White')
    begin_fill()
    circle(50, 360, 1000)
    end_fill()

    up(), goto(0, 50), down()
    color('Black')
    begin_fill();
    circle(50, 360, 1000)
    end_fill()
    sleep(5)

# taiqi()
