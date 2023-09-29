#coding=utf-8
import os
import time
x=time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime())
#键盘命令
def jianpan(x):
    os.system('./adb shell input keyevent '+x)

# 安装与卸载

# os.system('./adb install apk')
def xiezai(package):
    os.system('./adb shell pm uninstall --user 0 '+package)
 
#打开微信
 
# os.system('./adb shell am start com.tencent.mm/.ui.LauncherUI')
# os.system('./adb shell am force-stop com.example.app')

# 熄萍时间(1-2147483647)
def xipingshijian(x):
    os.system('./adb shell settings put system screen_off_timeout '+x)
# os.system('adb shell settings get system screen_off_timeout')

# 录屏
def luping():
    os.system('./adb shell screenrecord  --time-limit 10 --size 2340*1080 /storage/emulated/0/Quark/Download/demo.mp4')

# 截屏
def jieping():
    os.system('./adb shell screencap /storage/emulated/0/Quark/Download/screen-%s.png'%x)
 
# 将截屏导出到电脑

# os.system('./adb pull /storage/emulated/0/Quark/Download/screen-%s.png /Users/mac/Pictures/screen-%s.png'%(x,x))
 
# 屏幕分辨率
def fenlianlv(x,y):
    if x != 'reset':
        os.system('./adb shell wm size '+x+'x'+y)
    else:
        os.system('./adb shell wm size reset ')

# 屏幕像素
def xiangsu(x):
    os.system('./adb shell wm density '+x)

# 电池电量
def dianliang(x):
    if x != 'reset':
        os.system('./adb shell dumpsys battery set level '+x)
    else:
        os.system('./adb shell dumpsys battery reset')

# 隐藏状态栏
def zhuangtai():
    os.system('./adb shell settings put global policy_control immersive.status=*')

# 恢复 ./adb shell settings put global policy_control null

# 键盘
# jianpan('26')
# 卸载
# xiezai('com.huawei.android.pushagent')
# 熄屏时间
# xipingshijian('3600000')
# 录屏
# luping()
# 截屏
# jieping()
# 屏幕分辨率
# fenbianlv()
# 像素
# xiangsu()
# 电池电量
# dianliang('reset')
# str='''4k极致23_fhd.mp4 [崩坏3]幽魅夜魔–芽衣32_fhd.mp4 《原神》 甘雨 - 要和甘雨一起加班么34_fhd.mp4 【原神】芭芭拉26_fhd.mp4 【崩坏3】希儿36_fhd.mp4 【崩坏3】雷电芽衣20_fhd.mp4 二次元59_fhd.mp4 八重樱614_hd.mp4 原神348_hd.mp4 原神99_fhd.mp4 原神甘雨 这是我老婆，拔刀吧诸君76_fhd.mp4 围裙刻晴17_fhd.mp4 德丽莎观星【稚忻】54_fhd.mp4 梦里韶光87_fhd.mp4 椰羊甘雨853_hd.mp4 樱50_fhd.mp4 爱宕20_fhd.mp4 甘雨39_fhd.mp4 甘雨（原神）96_fhd.mp4 白裙泥岩，博士，你有信心帮我穿好高跟鞋吗？13_fhd.mp4 皇女20_fhd.mp4 碧蓝航线 光辉 4k加v49_fhd.mp4 碧蓝航线90_fhd.mp4 礼服黑贞 原图地址 7422410722_fhd.mp4 花嫁尼禄26_fhd.mp4 花嫁甘雨06_fhd.mp4 诺艾尔72_fhd.mp4 雷电芽衣54_fhd.mp4'''
# list=str.split('.mp4 ')
# for list1 in list:
#     os.system('./adb -s 192.168.1.105 pull /storage/emulated/0/Pictures/壁纸/'+list1 +'.mp4 /Users/mac/Pictures/火荧壁纸/' + list1)
# os.system('./adb shell settings put global policy_control null')
# zhuangtai()
# os.system('./adb shell wm size 1158x2510')
os.system('./adb shell wm size 1158x2500')