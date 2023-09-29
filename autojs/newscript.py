#coding=utf-8
import os
import time
x=0
while(x<100):
    print(x)
    os.system('./adb shell input tap 1160 840')
    time.sleep(20)
    a=0
    while(a<6):
        os.system('./adb shell input swipe 380 800 530 680 10000')
        os.system('./adb shell input tap 2000 900')
        time.sleep(15)
        a+=1
    os.system('./adb shell input tap 2240 70')#设置
    print('设置')
    time.sleep(1)
    os.system('./adb shell input tap 1400 940')#发起投降
    print('发起投降')
    time.sleep(20)
    os.system('./adb shell input tap 1400 950')#点击屏幕继续
    print('点击屏幕继续')
    time.sleep(10)
    os.system('./adb shell input tap 1160 980')#继续
    print('继续')
    time.sleep(1)
    x+=1
    os.system('./adb shell input tap 1300 970')#再来一局
    print('再来一局')
    time.sleep(20)