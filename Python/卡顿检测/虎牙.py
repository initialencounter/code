
from PIL import Image,ImageGrab
import time,pyautogui
initcolor=(255,255,255,255)
time.sleep(5)
while 1:
    time.sleep(2)
    box = (200,500,300,600)
    img = ImageGrab.grab(box)
    img = img.load()
    color  =img[50,50]

    if color==initcolor:
        print('kadun',time.time())
        pyautogui.click(58, 703, 1, button='left')
        time.sleep(1)
        pyautogui.click(67,777,1, button='left')
    else:
        initcolor = color