import time
from turtle import *
from time import *
from math import cos,radians
def square(b):
    begin_fill();
    print(b)
    col = str(hex(int(((200-b) * 256 / 200) * 65535))[2:])
    col = '#' + (6 - len(col)) * '0' + col
    color(col)
    for i in range(4):
        fd(b)
        right(90)
    end_fill()
def pythag_orean_number(b):
    if b<15:return

    square(b)

    fd(b)
    left(30)
    pythag_orean_number(b*cos(radians(30)))
    square(b*cos(radians(30)))

    right(90)
    fd(b*cos(radians(30)))
    pythag_orean_number(b * cos(radians(60)))
    square(b*cos(radians(60)))

    right(90)
    fd(b*cos(radians(60)))
    right(30)
    fd(b)
    right(90)
    fd(b)
    right(90)
# screensize(2800,1800,'#C1CDC1')
# speed(999999999999999)
# up()
# goto(50,-250)
# down()
# seth(90)
# sleep(3)
# pythag_orean_number(180)
# sleep(3)
def draw_triangle(b):
    if b<10:return
    for i in range(6):
        draw_triangle(b/2)
        left(120)
        fd(b)
        print(120,b)

speed(0)
draw_triangle(200)
def draw_snowflake(b):
    if b<4:
        return
    # down()
    for i in range(6):
        draw_snowflake(b/3)
        fd(b)
        left(60)
        fd(b)
        right(120)
    # up()

# draw_snowflake(100)
#
# sleep(1)

