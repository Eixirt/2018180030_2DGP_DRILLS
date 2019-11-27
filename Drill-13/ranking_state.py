import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state


name = "RankingState"

ranking_list = []


def enter():
    global ranking_list
    hide_cursor()
    hide_lattice()
    pass


def exit():
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass


def draw():
    clear_canvas()



    update_canvas()
    pass





