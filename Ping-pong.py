import pygame as pg

pg.font.init()

background_color = (200, 255, 255)
RES = WIDTH, HEIGHT = 600, 500
window = pg.display.set_mode((RES))
window.fill(background_color)
FPS = 60
s_p1 = 0
s_p2 = 0

class GameSprite(pg.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, speed_x, speed_y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = speed_x
        self.speed_y = speed_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        global s_p1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= 450:
            self.speed_y *= -1
            s_p1 += 1
        if self.rect.y <= 0:
            self.speed_y *= -1
    def sds(self):
        return self.rect.x >= 600 or self.rect.x <= -20
    def pf(self):
        a = pg.key.get_pressed()
        if a[pg.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if a[pg.K_s] and self.rect.y <= (HEIGHT - 100):
            self.rect.y += self.speed
    def pd(self):     
        a = pg.key.get_pressed()   
        if a[pg.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if a[pg.K_DOWN] and self.rect.y <= (HEIGHT - 100):
            self.rect.y += self.speed
    def fr(self):
        self.speed_x *= -1
    def sd(self,r):
        return self.rect.colliderect(r)
    def remake(self):
        self.rect.x = 200
        self.rect.y = 200
x1,y1 = 200,200
x2,y2 = 0,150
x3,y3 = 560,150

ball = GameSprite('tenis_ball.png',x1,y1,50,50,4,4,4)
player1 = GameSprite('racket.png',x2,y2,40,100,6,4,4)
player2 = GameSprite('racket.png',x3,y3,40,100,6,4,4)


clock = pg.time.Clock()

game = True
finish = False
while game:
    pg.display.set_caption(str(clock.get_fps()//1))
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
    if finish != True:
        window.fill(background_color)
        ball.reset()
        player1.reset()
        player2.reset()
        ball.update()
        player1.pf()
        player2.pd()
        if ball.sds():
            ball.remake()
        if ball.sd(player1) or ball.sd(player2):
            ball.fr()
    pg.display.update()
    clock.tick(FPS)
