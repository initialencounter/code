from PIL import Image
from turtle import *
from PIL import ImageFilter
import time,os
from os import system as sys

lst2=[[0,0],[6,5],[0,11],[8,8],[6,13],[1,3],[1,5]]
# sys('adb shell /system/bin/screencap -p /sdcard/脚本/scr.png')
# sys('adb pull /sdcard/脚本/scr.png /Users/mac/PycharmProjects/pythonProject1/游戏/扫雷')
# time.sleep(2)
img = Image.open('./scr.png').load()
print(img[70,300])
lst_peak=[]
def readmin():
    x=0
    for i in range(0,540):
        for j in range(200,1170):
            if img[i,j][0]==193:
                lst_peak.append([i,j])
                x=1
            if x==1:
                break
def readmax():
    x=0
    for i in range(1000,540,-1):
        for j in range(2200,1170,-1):
            if img[i,j][0]==193:
                lst_peak.append([i,j])
                print(i,j)
                x = 1
            if x == 1:
                break


def draw(x,y):
    ht()
    pensize(1)
    speed(20)
    color('Black')
    begin_fill()
    circle(x, y, 10)
    end_fill()
# x,y=lst_peak[0][0],lst_peak[0][1]
lstpoint= []
print(len(lstpoint))
def main():
    readmin()
    readmax()
    # for i in range(lst_peak[0][0], lst_peak[1][0], 120):
    #     for j in range(lst_peak[0][1], lst_peak[1][1]+240, 120):
    for i in range(55, 1080, 135):
        for j in range(405, 2050, 135):
            if img[i,j][0]>230 and img[i,j][0]<255:  #193
                lstpoint.append([i, j])
    print(lstpoint)
    for i in lstpoint:
        os.popen('adb shell input tap '+str(i[0])+' '+str(i[1]))
        time.sleep(0.08)
    # time.sleep(0.4)
    # os.popen('adb shell input tap 540 2270')
    # lst2 = [[0, 0], [6, 5], [0, 10], [5, 4], [8, 7], [7, 1], [3, 5], [7, 8], [7, 10], [8, 12],
    #         [6, 13], [1, 3], [1, 5], [0, 8], [3, 7], [4, 9], [7, 10], [1, 12], [5, 10]]
    # lst3 = [[6, 13], [1, 3], [1, 5], [0, 8], [3, 7], [4, 9], [7, 10], [1, 12], [5, 10],[7,1]]
    # for i in lst2:
    #     os.popen('adb shell input tap ' + str(55 + i[0] * 120) + ' ' + str(405 + i[1] * 120))
    #     # os.popen('adb shell input tap ' + str(i[0]) + ' ' + str(i[1]))
    #     time.sleep(0.08)
    # for i in lst3:
    #     os.popen('adb shell input tap ' + str(55 + i[0] * 120) + ' ' + str(405 + i[1] * 120))
    #     # os.popen('adb shell input tap ' + str(i[0]) + ' ' + str(i[1]))
    #     time.sleep(0.08)
    # time.sleep(0.6)
    # os.popen('adb shell input tap 540 2270')
    # for i in range(55, 1080, 120):
    #     for j in range(405, 2050, 120):
    #         os.popen('adb shell input tap ' + str(i) + ' ' + str(j))
    #         time.sleep(0.01)
main()
def split(x,y):
    if x >1080 or  x<0 or y<0 or y>2340:
        pass
    if img[x+1,y][0]==193:
        split(x+1,y)
        draw(x+1,y)
    if img[x-1, y][0] == 193:
        split(x - 1, y)
        draw(x - 1, y)
    if img[x,y+1][0]==193:
        split(x,y+1)
        draw(x,y+1)
    if img[x,y-1][0]==193:
        split(x,y-1)
        draw(x,y-1)

# split(x,y)
