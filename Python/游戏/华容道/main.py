import random
import time
from p15 import main
from PIL import Image
from os import system as sys
l,m=0,0
lst = [[[150,800],[400,800],[670,800],[930,800]],
       [[150,1140],[400,1140],[670,1140],[930,1140]],
       [[150,1340],[400,1340],[670,1340],[930,1340]],
       [[150,1660],[400,1660],[670,1660],[930,1660]],]
def swpie(x,y,i):
    p = random.randint(1,5)
    t = random.randint(500, 700)
    if i=='上':
        xx=x+p
        yy=y+262+p
        sys('adb shell input swipe %s %s %s %s %s'%(x,y,xx,yy,t))
        # print('adb shell input swipe %s %s %s %s %s'%(x,y,xx,yy,y/10))
        y=yy
        x=xx
    if i=='下':
        xx=x+p
        yy=y-262+p
        sys('adb shell input swipe %s %s %s %s %s'%(x,y,xx,yy,t))
        y=yy
        x=xx
    if i=='左':
        xx=x-262+p
        yy=y+p
        sys('adb shell input swipe %s %s %s %s %s'%(x,y,xx,yy,t))
        y=yy
        x=xx
    if i=='右':
        xx=x+262+p
        yy=y+p
        sys('adb shell input swipe %s %s %s %s %s'%(x,y,xx,yy,t))
        y=yy
        x=xx
    return [x,y]
def tap(x,y):
    pp = 0
    t = random.randint(4, 5)
    p = random.randint(0, 3)
    p2 = random.randint(0, 3)
    xx = x+p
    yy = y+p+pp
    sys('adb shell input tap %s %s'%(xx,yy))
    time.sleep(t/10)

    return [x,y]

str_lst = main()

for i in str_lst:

    m,l = tap(lst[i[1]][i[0]][0],lst[i[1]][i[0]][1])
