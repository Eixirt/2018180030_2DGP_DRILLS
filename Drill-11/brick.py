import random
from pico2d import *
import game_world
import game_framework


class Brick:
    image = None

    def __init__(self):
        if Brick.image is None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y, self.velocity = random.randint(200, 1300-1), 200, 300
        self.dir = 1
        self.moving_interval = 0

    def get_bb(self):
        # fill here
        return self.x - Brick.image.w / 2, self.y - Brick.image.h / 2,\
               self.x + Brick.image.w / 2, self.y + Brick.image.h / 2

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        self.moving_interval = self.dir * self.velocity * game_framework.frame_time
        if (self.x - self.moving_interval) > 1300 - 1 or (self.x - self.moving_interval) < 200:
            self.dir = -self.dir
            self.x -= self.moving_interval
        else:
            self.x -= self.moving_interval

    # fill here for def stop
    def stop(self):
        self.velocity = 0

    pass


