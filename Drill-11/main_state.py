import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball, BigBall
from brick import Brick

name = "MainState"

boy = None
grass = None
brick = None
balls = []
big_balls = []
collided_rect = [0, 0, 0, 0]


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    # 충돌 영역 구하기
    collided_rect[0] = max(left_a, left_b)
    collided_rect[2] = min(right_a, right_b)

    collided_rect[1] = max(bottom_a, bottom_b)
    collided_rect[3] = min(top_a, top_b)

    return True


def collide_block(block, obj):
    block_bb = {'left': block.get_bb()[0], 'bottom': block.get_bb()[1],
                'right': block.get_bb()[2], 'top': block.get_bb()[3]}
    obj_bb = {'left': obj.get_bb()[0], 'bottom': obj.get_bb()[1],
              'right': obj.get_bb()[2], 'top': obj.get_bb()[3]}

    if block_bb['top'] - 5 < obj_bb['bottom'] < block_bb['top'] and \
            obj_bb['left'] < block_bb['right'] and obj_bb['right'] > block_bb['left']:
        obj.y = block_bb['top'] + 19
        return True
        pass
    return False
    pass


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls
    global balls
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]
    game_world.add_objects(balls, 1)

    global brick
    brick = Brick()
    game_world.add_object(brick, 1)
    pass


def exit():
    game_world.clear()


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
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # fill here for collision check
    for ball in balls:
        if collide(boy, ball):
            balls.remove(ball)
            game_world.remove_object(ball)

    for ball in balls:
        if collide(grass, ball):
            ball.stop()

        if collide(brick, ball):
            if abs(collided_rect[0] - collided_rect[2]) > abs(collided_rect[1] - collided_rect[3]) \
                    and (brick.y < ball.y):
                # ball.stop()
                ball.y = brick.get_bb()[3] + ball.image.h / 2 - 3
                ball.x -= brick.moving_interval
                pass
            elif ball.get_bb()[0] < brick.get_bb()[0]:
                ball.x = brick.get_bb()[0] - ball.image.w / 2 - 15
                pass
            elif ball.get_bb()[2] > brick.get_bb()[2]:
                ball.x = brick.get_bb()[2] + ball.image.w / 2 + 15
                pass
        pass
    # 플레이어와 벽돌 충돌체크
    if collide(brick, boy):
        if (collided_rect[1] + collided_rect[3]) / 2 < (brick.get_bb()[1] + brick.get_bb()[3]) / 2:
            boy.jumping_power = 0
            pass
        elif boy.starting_pos_y == brick.get_bb()[3] + 100 / 2 - 3 and boy.jumping_height >= 0:
            boy.init_jump()
            boy.y += 4 
            boy.starting_pos_y = 90
            boy.jump()
            pass
        else:
            boy.is_jumping = False
            boy.y = brick.get_bb()[3] + 100 / 2 - 3
            if boy.cur_state == boy.init_state:
                boy.x -= brick.moving_interval
        pass

    if not collide(grass, boy):
        if not collide(brick, boy) and boy.is_jumping is False:
            boy.init_jump()
            boy.jumping_power = 0
            boy.starting_pos_y = 90
            pass
    pass


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






