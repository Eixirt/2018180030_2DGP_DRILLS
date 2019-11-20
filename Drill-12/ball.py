import random
from pico2d import *
import game_world


class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(200, 1000), random.randint(200, 1000)

    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

