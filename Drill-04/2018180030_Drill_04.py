from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 20

# 여기를 채우세요.
frame_x = 0
frame_y = 1

is_right_moving = True

while x < 800:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x + 40, 90)
    update_canvas()
    frame_x = (frame_x + 1) % 8

    if x > 700:
        frame_y -= 1
        is_right_moving = False
    elif x < 20:
        frame_y += 1
        is_right_moving = True

    if is_right_moving:
        x += 20
    else:
        x -= 20

    delay(0.05)
    get_events()

close_canvas()

