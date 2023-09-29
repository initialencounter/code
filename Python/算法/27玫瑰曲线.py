from turtle import *
from math import *
def draw(a,n,end):
    t=0
    while t<=end:
        x=a*sin(n*t)*cos(t)
        y=a*sin(n*t)*sin(t)
        goto(x,y)
        t+=0.01
# draw(100,3/2,12.56)

def draw_heart():
    up()
    t=0
    a=100
    while t<2 * pi:
        x=a*(1-sin(t))*cos(t)
        y=a*(1-sin(t))*sin(t)
        goto(x,y)
        down()
        t+=0.01
# draw_heart()

def draw_peach():
    a,t=10,0
    up()
    while t<=2*pi:
        x=a*15*sin(t)**3
        y=a*(15*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))
        goto(x,y)
        down()
        t+=0.01
# draw_peach()
def draw_butterfly():
    a,t=60,0
    b=24*pi
    while t<=b:
        print(t)
        begin_fill();
        col = str(hex(int((t * 256 / b) * 65535))[2:])
        col = '#' + (6 - len(col)) * '0' + col
        color(col)
        p=e**cos(t)-2*cos(4*t)+sin(t/12)**5
        x=a*sin(t)*p
        y=a*cos(t)*p
        goto(x, y)
        end_fill()
        down()
        t += 0.1

draw_butterfly()