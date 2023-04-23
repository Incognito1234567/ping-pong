import pygame as pg


background_color = (200, 255, 255)
RES = WIDTH, HEIGHT = 600, 500
window = pg.display.set_mode((RES))
window.fill(background_color)
FPS = 60


clock = pg.time.Clock()

game = True
finish = False
while game:
    pg.display.set_caption(str(clock.get_fps()))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    if finish != True:
        window.fill(background_color)

    pg.display.update()
    clock.tick(FPS)