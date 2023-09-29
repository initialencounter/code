import pyglet
def center_image(image):
    '''设置图片的锚点为中心'''
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

pyglet.resource.path=['./res/images','./res/sounds']

welcome_img = pyglet.resource.image('game_welcome.png')
bg_img = pyglet.resource.image('game_play.png')
end_img = pyglet.resource.image('game_end.png')
heart1_img = pyglet.resource.image('heart1.png')
heart2_img = pyglet.resource.image('heart2.png')
heart3_img = pyglet.resource.image('heart3.png')
snow_flake_img = pyglet.resource.image('雪花.png')
clipper_img = pyglet.resource.image('剪刀.png')
gift_img = pyglet.resource.image('礼物.png')
princess_img = pyglet.resource.image('公主.png')

center_image(clipper_img)
center_image(snow_flake_img)
center_image(gift_img)
center_image(princess_img)

music = pyglet.resource.media('铃儿响叮当.m4a',streaming=False)
pop_sound = pyglet.resource.media('pop.wav',streaming=False)
