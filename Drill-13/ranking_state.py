import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import world_build_state


name = "RankingState"

curr_data = None
ranking_list = []
font = None


def enter():
    global ranking_list, font, curr_data

    with open('ranking_data.json', 'r') as f:
        ranking_list = json.load(f)

    ranking_list.append(curr_data)
    ranking_list.sort(reverse=True)

    hide_cursor()
    hide_lattice()
    font = load_font('ENCR10B.TTF', 20)

    with open('ranking_data.json', 'w') as f:
        json.dump(ranking_list, f)
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
            game_world.save()
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_world.save()
            game_framework.change_state(world_build_state)


def update():
    pass


def draw():
    clear_canvas()
    font.draw(600, 800, "Ranking Chart")

    for i in range(min(10, len(ranking_list))):
        font.draw(400, 700 - i * 20, "# " + str(i + 1))
        font.draw(500, 700 - i * 20, str(ranking_list[i]))

    update_canvas()
    pass





