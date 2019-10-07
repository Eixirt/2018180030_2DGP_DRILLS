import pico2d

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT)

background = pico2d.load_image('KPU_GROUND.png')
mouse = pico2d.load_image('hand_arrow.png')
character = pico2d.load_image('animation_sheet.png')

running = True
frame_x = 0
frame_y = 1

mouse_x = 320
mouse_y = 350


def handle_events():
    global running
    global mouse_x, mouse_y

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False
        elif event.type == pico2d.SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y


pico2d.hide_cursor()

while running:
    pico2d.clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    mouse.draw(mouse_x, mouse_y)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, 100 + 240, 290)
    frame_x = (frame_x + 1) % 8

    pico2d.update_canvas()
    pico2d.delay(0.05)
    handle_events()

pico2d.close_canvas()