# import pynput.keyboard as pk
import pyglet
import playsound
import warnings
warnings.filterwarnings('ignore')
import pynput.mouse as pm
import threading,time
# def on_press(key):
#     # 监听按键
#     key=str(key)[1]
#     print("按键为",key)
#     # s.send(key.encode())
# # 连接事件以及释放
# with pk.Listener(on_press=on_press) as pklistener:
#     pklistener.join()
import pyglet
# sound = pyglet.media.load('pop.wav')
def sound_play():
    sound = pyglet.media.load('pop.wav')
    sound.play()
    pyglet.app.run()
# def play_sound():
#     global play_thread
#     play_thread = threading.Thread(target=sound_play())
#     play_thread.start()
def on_click(x, y, button, pressed):
    # 监听鼠标点击
    if pressed:
        print("按下鼠标")
        sound_play()
        # play_sound()
    if not pressed:#     # Stop listener
        return False
def ls_k_thread():
    while(1):
        with pm.Listener(on_click=on_click) as pmlistener:
            pmlistener.join()
ls_k_thread()


# def analyse_pic_thread():
#     r = threading.Thread(target=ls_k_thread)
#     r.start()
# try:
#     analyse_pic_thread()
#     while(1):
#         pass
#
# except:
#     pass

