import pico2d
KPU_WIDTH, KPU_HEIGHT = 1280, 1024
pico2d.open_canvas(KPU_WIDTH, KPU_HEIGHT)

background = pico2d.load_image('KPU_GROUND.png')
mouse = pico2d.load_image('hand_arrow.png')
character = pico2d.load_image('animation_sheet.png')

running = True

while running:
    pico2d.clear_canvas()
    background.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    pico2d.update_canvas()
    pico2d.delay(0.1)

pico2d.close_canvas()