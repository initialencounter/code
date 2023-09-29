from falling_object import *
from pyglet.window import key
from pyglet import clock

game_state = 0

game_win = pyglet.window.Window(width=800, height=600)
game_win.set_caption('公主迎圣诞')

princess = pyglet.sprite.Sprite(princess_img, 400, 150)
falling_obj = falling_object()
heart = pyglet.sprite.Sprite(heart1_img, 50, 500)
score_label = pyglet.text.Label('0', color=(0, 0, 0, 255), x=300, y=570)
timer_label = pyglet.text.Label('00:00', color=(0, 0, 0, 255), x=430, y=570)

player = pyglet.media.Player()
player.volume = 0.5

@game_win.event
def on_draw():
    global game_state, heart_num
    game_win.clear()
    if game_state == 0:
        welcome_img.blit(0, 0)
    elif game_state == 1:
        bg_img.blit(0, 0)
        princess.draw()
        score_label.draw()
        falling_obj.draw()
        if 1 <= heart_num <= 3:
            heart.draw()
        timer_label.draw()
    else:
        end_img.blit(0, 0)
        score_label.draw()
        timer_label.draw()

@game_win.event
def on_key_press(symbol, modifiers):
    global game_state, score, heart_num, timer_value
    if symbol == key.ENTER:
        if game_state != 1:
            game_state = 1
            falling_obj.change()
            score = 0
            heart_num = 3
            timer_value = 300


def princess_control(dt):
    global game_state
    if game_state != 1:
        return

    if keys[key.LEFT]:
        princess.x -= 400 * dt
        if princess.x < princess.width / 2:
            princess.x = princess.width / 2
    elif keys[key.RIGHT]:
        princess.x += 400 * dt
        if princess.x > 800 - princess.width / 2:
            princess.x = 800 - princess.width / 2


def falling_control(dt):
    global heart_num, score, game_state
    if game_state != 1:
        return
    falling_obj.rotation += 60 * dt
    falling_obj.y -= 200 * dt
    if falling_obj.y < 0:
        falling_obj.change()

    if falling_obj.touching(princess.position, princess.height / 2):
        if falling_obj.type == 1:
            score += 10
        elif falling_obj.type == 2:
            score += 50
        elif falling_obj.type == 3:
            heart_num -= 1
        # 音效
        pop_sound.play()
        # 切换下落物体造型
        falling_obj.change()

    score_label.text = str(score)

    # 更新生命爱心
    if heart_num < 0:
        game_state = 2
    elif heart_num == 1:
        heart.image = heart1_img
    elif heart_num == 2:
        heart.image = heart2_img
    elif heart_num == 3:
        heart.image = heart3_img


def others_control(dt):
    '''其他控制：倒计时、循环播放背景音乐'''
    global game_state, timer_value

    # 倒计时
    if game_state == 1:
        timer_value -= 1 * dt
        if timer_value <= 0:
            timer_value = 0
            game_state = 2
        timer_label.text = '%02d:%02d' % (timer_value // 60, timer_value % 60)

    # 循环播放背景音乐
    if game_state == 1:
        if not player.playing:
            player.queue(music)
            player.play()
    else:
        player.next_source()


if __name__ == '__main__':
    keys = key.KeyStateHandler()
    game_win.push_handlers(keys)
    clock.schedule_interval(princess_control, 1 / 60)
    clock.schedule_interval(falling_control, 1 / 60)
    clock.schedule_interval(others_control, 1 / 60)
    pyglet.app.run()
