import pyglet
from math import sqrt
from pyglet import clock
from random import randint
from pyglet.window import key

pyglet.resource.path = ['./res']
bg_img = pyglet.resource.image('沙漠.png')
motor_animation = pyglet.resource.animation('motor-red.gif')
box_img = pyglet.resource.image('box.png')
motor_sound = pyglet.resource.media('motor.wav', streaming=False)
alter_sound = pyglet.resource.media('alter.mp3', streaming=False)

motor_x = 0
motor_y = 40
motor_speed = 0
mileages = 0

game_win = pyglet.window.Window(width=600, height=295, caption='疯狂摩托')
motor = pyglet.sprite.Sprite(img=motor_animation, x=50, y=40)
box = pyglet.sprite.Sprite(img=box_img, x=500, y=10)
speed_label = pyglet.text.Label('Speed:0', x=10, y=280)
mileages_label = pyglet.text.Label('Mileages:0', x=10, y=260)
motor_player = pyglet.media.Player()
alter_player = pyglet.media.Player()


@game_win.event
def on_draw():
    global motor_x
    bg_img.blit(0 - int(motor_x) % 600, 0)
    bg_img.blit(600 - int(motor_x) % 600, 0)

    if motor.y > box.y:
        motor.draw()
        box.draw()
    else:
        box.draw()
        motor.draw()

    speed_label.draw()
    mileages_label.draw()


def distance(a=(0, 0), b=(0, 0)):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def motor_move(up_max, down_min, speed, dt):
    global motor_speed, motor_y
    if keys[key.UP]:
        motor_y += 50 * dt
        if motor_y > up_max: motor_y = up_max
    if keys[key.DOWN]:
        motor_y -= 50 * dt
        if motor_y < down_min: motor_y = down_min
    if keys[key.LEFT]:
        motor_speed -= 324 * dt
        if motor_speed < 0: motor_speed = 0
    if keys[key.RIGHT]:
        motor_speed += speed * dt
        if motor_speed > 1620: motor_speed = 1620  # 摩托车最大速度


def motor_control(dt):
    global motor_speed, motor_x, motor_y, mileages

    if distance(motor.position, box.position) <= motor.width:
        if (box.y < motor.y < box.y + 12):
            motor_speed = 0
            motor_move(50, 0, 0, dt)
        elif motor.y >= box.y + 12:
            motor_move(50, box.y + 12, 162, dt)
        else:
            motor_move(box.y, 0, 162, dt)
    else:
        motor_move(50, 0, 162, dt)

    motor.y = motor_y
    motor_x += motor_speed * dt
    mileages = motor_x * 0.024
    speed_label.text = 'Motor:%.3f km/h' % (motor_speed * 0.024 * 3.6)
    mileages_label.text = 'Mileages: %.3f km' % (mileages / 1000)


    if motor_speed > 0:
        if not motor_player.playing:
            motor_player.queue(motor_sound)
            motor_player.play()
    elif motor_speed == 0:
        motor_player.next_source()


def box_control(dt):
    global mileages, motor_speed
    if mileages > 100 and int(mileages) % 300 == 0:
        if not motor_player.playing:
            alter_player.queue(alter_sound)
            alter_player.play()
        box.x = 3000
        box.y = motor.y - 6
    else:
        box.x -= motor_speed * dt


@game_win.event
def on_close():
    motor_player.next_source()


if __name__ == '__main__':
    keys = key.KeyStateHandler()
    game_win.push_handlers(keys)
    clock.schedule_interval(motor_control, 1 / 60)
    clock.schedule_interval(box_control, 1 / 60)
    pyglet.app.run()
