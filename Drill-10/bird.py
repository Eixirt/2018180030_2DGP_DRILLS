import pico2d
import game_framework
import game_world

PIXEL_PER_METER = (10.0 / 0.2)  # 10 pixel = 20 cm
RUN_SPEED_KMPH = 32.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    BIRD_PIXEL_WIDTH = 180
    BIRD_PIXEL_HEIGHT = 160

    def __init__(self):
        self.image = pico2d.load_image('bird_animation.png')
        self.dir = 1
        self.frame = 0
        self.x, self.y = 400, 300
        self.velocity = RUN_SPEED_PPS
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        if self.x >= 910:
            self.velocity = -RUN_SPEED_PPS

        elif self.x <= 90:
            self.velocity = RUN_SPEED_PPS

        self.dir = pico2d.clamp(-1, self.velocity, 1)
        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame % 5) * 183,
                                           self.image.h - 168 * (1 + int(self.frame // 5)),
                                           180, 160, 0, '', self.x, self.y,
                                           Bird.BIRD_PIXEL_WIDTH, Bird.BIRD_PIXEL_HEIGHT)
        elif self.dir == -1:
            self.image.clip_composite_draw(int(self.frame % 5) * 183,
                                           self.image.h - 168 * (1 + int(self.frame // 5)),
                                           180, 160, 0, 'h', self.x, self.y,
                                           Bird.BIRD_PIXEL_WIDTH, Bird.BIRD_PIXEL_HEIGHT)
        pass

    pass
