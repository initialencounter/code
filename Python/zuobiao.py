import pyautogui
import time
# 获取鼠标位置
def get_mouse_positon():
    # time.sleep(1)  # 准备时间
    print('开始获取鼠标位置')
    try:
        for i in range(1):
            # Get and print the mouse coordinates.
            x, y = pyautogui.position()
            print(x, y)
            time.sleep(0.5)  # 停顿时间
    except:
        print('获取鼠标位置失败')
def on_press(key):
    key = str(key)
    print(key)
    if "'f'" in key:
        os.system('./adb shell input tap 270 960')
    elif "'d'" in key:
        os.system('./adb shell input tap 2200 730')
    elif "'1'" in key:
        os.system('./adb shell input tap 600 300')
    elif "'2'" in key:
        os.system('./adb shell input tap 970 300')
    elif "'3'" in key:
        os.system('./adb shell input tap 1330 300')
    elif "'4'" in key:
        os.system('./adb shell input tap 1730 300')
    elif "'5'" in key:
        os.system('./adb shell input tap 2100 300')
    elif "'l'" in key:
        os.system('./adb shell input tap 2222 555')
if __name__ == "__main__":
    get_mouse_positon()
