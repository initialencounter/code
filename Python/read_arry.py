from PIL import Image
from os import system as sys
lst = [[[240,800],[500,800],[770,800],[1030,800]],[[240,1080],[500,1080],[770,1080],[1030,1080]]
           ,[[240,1340],[500,1340],[770,1340],[1030,1340]],[[240,1600],[500,1600],[770,1600],[1030,1600]]]

def read_arry():
    sys('adb shell /system/bin/screencap -p /sdcard/脚本/scr.png')
    sys('adb pull /sdcard/脚本/scr.png /Users/mac/PycharmProjects/pythonProject1')
    # time.sleep(5)
    img = Image.open('./scr.png').load()
    lst1 = []
    for i in lst:
        lst_ = []
        for j in i:
            print(img[j[0],j[1]][1])
            x = img[j[0],j[1]][1]
            lst_.append(int(x/15))
        lst1.append(lst_)
    for i in range(4):
        for j in range(4):
            if 17 == lst1[i][j]:
                lst1[i][j]=16
                l,m=i,j
    for i in lst1:
        print(i)
    return lst1