import random
from pico2d import *
import game_world
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball41x41.png')
        self.x = random.randint(0 + 50, main_state.background.w - 50)
        self.y = random.randint(0 + 50, main_state.background.h - 50)

    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        cx, cy = self.x - main_state.boy.bg.window_left, self.y - main_state.boy.bg.window_bottom
        self.image.draw(cx, cy)
        # fill here for draw

    def update(self):
        pass

