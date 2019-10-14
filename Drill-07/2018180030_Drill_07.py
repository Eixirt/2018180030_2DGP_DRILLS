from pico2d import *
from random import *


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = randint(100, 700), 90
        self.frame = randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = randint(100, 700), 599
        self.size = randint(0, 1)  # 0 = 21x21 / 1 = 41x41
        self.fall_speed = randint(5, 50)
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        if self.y > 30:
            self.y = self.y - self.fall_speed
            if self.y <= 30:
                self.y = 30

    def draw(self):
        if self.size == 0:
            self.image.draw(self.x, self.y + 35)
        else:
            self.image.draw(self.x, self.y + 45)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
open_canvas()
boy = Boy()
grass = Grass()

balls = [Ball() for i in range(20)]
team = [Boy() for i in range(11)]

running = True

# game main loop code
while running:
    # player 역할
    handle_events()

    for boy in team:
        boy.update()

    for ball in balls:
        ball.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()

    for ball in balls:
        ball.draw()

    update_canvas()

    delay(0.05)

# finalization code
close_canvas()