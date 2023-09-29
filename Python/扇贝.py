# from pynput import keyboard
# import os, pyautogui, time
# fe = 1
# def on_press1(key):
#     key = str(key)
#     global num
#     global fe
#     if "'1'" in key:
#         os.system('adb shell input tap 522 2077')
#     elif "'2'" in key:
#         os.system('adb shell input tap 537 2247')
#     elif "Key.esc" in key:
#         os._exit(0)
# while fe == 1:
#     with keyboard.Listener(on_press=on_press1) as listener:
#         listener.join()
import os
print(os.listdir('/Users/mac/Desktop/video/'))