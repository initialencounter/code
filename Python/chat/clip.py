import os,time,pyperclip
cl = ''
while 1:
    os.system('adb pull /sdcard/脚本/clips.txt /Users/mac/PycharmProjects/pythonProject1/chat')
    time.sleep(1)
    # os.system('adb shell wm size')
    with open('./clips.txt','r') as f:
        ff = f.read()
        print(ff)
        if f!=cl:
            pyperclip.copy(ff)
