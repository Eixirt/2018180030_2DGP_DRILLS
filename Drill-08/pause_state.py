from pico2d import *

import game_framework

name = "PauseState"
image = None
blink_time = 0
image_width = 0
image_height = 0

def enter():
    global image
    image = load_image('pause.png')
    pass


def exit():
    global image
    del image
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

    pass


def update():
    global blink_time
    global image
    global image_width, image_height

    if blink_time >= 0.25:
        blink_time = 0
        if image_width == 0:
            image_width = image.w
            image_height = image.h
        else:
            image_width = 0
            image_height = 0

    delay(0.01)
    blink_time += 0.01
    pass


def draw():
    clear_canvas()
    image.draw(400, 300, image_width / 4, image_height / 4)
    update_canvas()
    pass
