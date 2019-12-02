import random
from pico2d import *
import game_world
import main_state

class Ball:
    image = None

    def __init__(self):
        if Ball.image is None:
            Ball.image = load_image('ball41x41.png')
        self.x= random.randint(0 + 100, main_state.background.canvas_width - 100)

        self.y = random.randint(0 + 100, main_state.background.canvas_height - 100)

    def get_bb(self):
        # fill here
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw
        # draw_rectangle(*self.get_bb())

    def update(self):
        pass

