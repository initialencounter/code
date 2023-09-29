#coding=utf-8
import os
a=0
while(a<10):
    os.system('./adb shell input tap 1900 420')#主动
    os.system('./adb shell input tap 130 450')#商店
    os.system('./adb shell input tap 1630 950')#最后一栏
    os.system('./adb shell input tap 1940 870')#出售
    # os.system('./adb shell input tap 330 340')#攻击
    # os.system('./adb shell input tap 1460 310')#名刀
    # os.system('./adb shell input tap 1940 960')#购买
    os.system('./adb shell input tap 2000 110')#关闭
    os.system('./adb shell input tap 280 440')#快捷
    a+=1
# os.system('./adb shell input tap ')
# os.system('./adb shell input tap ')
# os.system('./adb shell input tap ')
# os.system('./adb shell input tap ')