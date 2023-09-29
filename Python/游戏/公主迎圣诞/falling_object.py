from random import randint
from math import sqrt
from game_res import *


class falling_object(pyglet.sprite.Sprite):
    def __init__(self):
        super().__init__(snow_flake_img)
        self.type = 1
        self.change()

    def change(self):
        x = randint(0, 10)
        if 0 <= x <= 1:
            self.type = 1
            self.image = snow_flake_img
        elif 2 <= x <= 3:
            self.type = 2
            self.image = gift_img
        else:
            self.type = 3
            self.image = clipper_img
        self.x, self.y = randint(100, 700), 900

    def touching(self, pos=(0, 0), distance=0):
        d = sqrt((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2)

        return d < distance
