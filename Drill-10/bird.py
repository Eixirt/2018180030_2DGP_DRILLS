import pico2d
import time

frame_time = 0.0

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel = 10 cm

pico2d.open_canvas(800, 600)

running = True


class Bird:
    BIRD_PIXEL_WIDTH = 184
    BIRD_PIXEL_HEIGHT = 184
    def __init__(self):
        self.image = pico2d.load_image('bird_animation.png')
        self.dir = 1
        self.frame = 0
        pass

    def update(self):
        self.frame = (self.frame + 1) % 14
        pass

    def draw(self):
        print(self.frame)
        self.image.clip_composite_draw(int(self.frame % 5) * 181, self.image.h - 181 * (1 + int(self.frame // 5)),
                                       184, 184, 0, '', 400, 300)
        pass
    pass


def handle_events():
    global running
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            running = False
    pass


bird = Bird()


while running:
    pico2d.clear_canvas()

    handle_events()
    bird.update()
    bird.draw()
    pico2d.update_canvas()
    pico2d.delay(0.5)

pico2d.close_canvas()