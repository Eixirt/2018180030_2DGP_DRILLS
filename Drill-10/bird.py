import pico2d

pico2d.open_canvas(800, 600)

running = True


class Bird:
    def __init__(self):
        pass
    pass


def handle_events():
    global running
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False
    pass


while running:
    pico2d.clear_canvas()

    handle_events()
    pico2d.update_canvas()

pico2d.close_canvas()