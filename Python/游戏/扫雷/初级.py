from PIL import Image
from turtle import *
from PIL import ImageFilter
import time, os
from os import system as sys
cun=0
# while 1:
#     os.popen('adb shell input tap 158 824')
#     time.sleep(0.08)
#     os.popen('adb shell input tap 931 1600')
#     time.sleep(0.08)
#     os.popen('adb shell input tap 158 1600')
#     time.sleep(0.08)
#     os.popen('adb shell input tap 931 824')
#     time.sleep(0.5)
#     os.popen('adb shell input tap 970 2270')
#     time.sleep(0.5)
#     os.popen('adb shell input tap 778 1338')
#     time.sleep(0.5)
#     cun+=1
#     print(cun)
lst2=[[0,0],[6,5],[0,10],[5,4],[8,7],[7,1],[3,5],[7,8],[7,10],[8,12],
      [6,13],[1,3],[1,5],[0,8],[3,7],[4,9],[7,10],[1,12],[5,10]]
lst3 = [[6,13],[1,3],[1,5],[0,8],[3,7],[4,9],[7,10],[1,12],[5,10]]
for i in lst2:
    os.popen('adb shell input tap ' + str(55 + i[0] * 120) + ' ' + str(405 + i[1] * 120))
    # os.popen('adb shell input tap ' + str(i[0]) + ' ' + str(i[1]))
    time.sleep(0.08)
for i in lst3:
    os.popen('adb shell input tap ' + str(55 + i[0] * 120) + ' ' + str(405 + i[1] * 120))
    # os.popen('adb shell input tap ' + str(i[0]) + ' ' + str(i[1]))
    time.sleep(0.08)