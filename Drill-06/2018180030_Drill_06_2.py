import random
import pico2d

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT)

background = pico2d.load_image('KPU_GROUND.png')
character = pico2d.load_image('animation_sheet.png')
pin_point = pico2d.load_image('pin_point.png')

running = True

goto_points = []

player_point = []
frame_point = [0, 1]
cnt = 0
cnt_idx = 0


def init_points():
    global goto_points
    global player_point

    for i in range(0, 9 + 1):
        goto_points = goto_points + [[random.randint(200, 1000), random.randint(200, 800)]]

    player_point = player_point + goto_points[0]


def draw_points():
    global goto_points
    for [x, y] in goto_points:
        pin_point.draw(x, y + 34, 50, 68)


def handle_events():
    global running

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False


def moving_character():
    global player_point
    global frame_point
    global goto_points
    global cnt_idx
    global cnt

    t = cnt / 100

    if t <= 1:
        player_point[0] = ((-t**3 + 2*t**2 - t)*goto_points[(cnt_idx - 1) % 10][0] +
                           (3*t**3 - 5*t**2 + 2)*goto_points[cnt_idx % 10][0] +
                           (-3*t**3 + 4*t**2 + t)*goto_points[(cnt_idx + 1) % 10][0] +
                           (t**3 - t**2)*goto_points[(cnt_idx + 2) % 10][0])/2

        player_point[1] = ((-t**3 + 2*t**2 - t)*goto_points[(cnt_idx - 1) % 10][1] +
                           (3*t**3 - 5*t**2 + 2)*goto_points[cnt_idx % 10][1] +
                           (-3*t**3 + 4*t**2 + t)*goto_points[(cnt_idx + 1) % 10][1] +
                           (t**3 - t**2)*goto_points[(cnt_idx + 2) % 10][1])/2
        cnt += 4
        if cnt > 100:
            cnt_idx = (cnt_idx + 1) % 10
            cnt = 0


# 메인문
init_points()
while running:
    pico2d.clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)


    # 300, 300 에 점 찍기
    # pin_point.draw(300, 300 + 34, 50, 68)

    draw_points()

    character.clip_draw(frame_point[0] * 100, frame_point[1] * 100, 100, 100, player_point[0], player_point[1])
    frame_point[0] = (frame_point[0] + 1) % 8
    moving_character()

    pico2d.update_canvas()
    pico2d.delay(0.02)
    handle_events()

pico2d.close_canvas()