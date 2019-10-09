import pico2d

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT)

background = pico2d.load_image('KPU_GROUND.png')
character = pico2d.load_image('animation_sheet.png')

running = True


def handle_events():
    global running

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False


def moving_charcter():
    global running


while running:
    pico2d.clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    pico2d.update_canvas()
    pico2d.delay(0.05)
    handle_events()

pico2d.close_canvas()