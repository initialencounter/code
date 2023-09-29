from pynput import keyboard
import os, pyautogui, time
time.sleep(3)
num = 1
fe = 1
def on_press1(key):
    key = str(key)
    global num
    global fe
    if "'z'" in key:
        pyautogui.click(164,946,1,button = 'left')
    elif "'x'" in key:
        pyautogui.click(1800, 950, 1, button='left')
    elif "'s'" in key:
        pyautogui.click(1800, 750, 1, button='left')
    elif "'w'" in key:
        pyautogui.click(1830, 610, 1, button='left')
    elif "'r'" in key:#数据
        pyautogui.click(1830, 215, 1, button='left')
    elif "'1'" in key:
        pyautogui.click(460, 384, 1, button='left')
    elif "'2'" in key:
        pyautogui.click(750, 370, button='left')
    elif "'3'" in key:
        pyautogui.click(1070, 384, 1, button='left')
    elif "'4'" in key:
        pyautogui.click(1388, 377, 1, button='left')
    elif "'5'" in key:
        pyautogui.click(1700, 380, 1, button='left')
    elif "'q'" in key:
        num +=1
        pyautogui.click(1800, 290+num*73, 1, button='left')
    elif "'e'" in key:
        num =num-1
        pyautogui.click(1800, 290+num*73, 1, button='left')
    elif "'a'" in key:
        pyautogui.click(1626, 849, 1, button='left')
    elif "Key.esc" in key:
        os._exit(0)
while fe == 1:
    with keyboard.Listener(on_press=on_press1) as listener:
        listener.join()
