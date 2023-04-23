# ping-pong
from pygame import *
init()
width,height = 500,700
FPS = 200
x1 = 0
y1 = 680
x2 = 0
y2 = 0
x3 = 250
y3 = 350
ert = 150
ert2 = 150
window = display.set_mode((width,height))
Black = (0,0,0)
Blue = (0,0,255)
White = (255,255,255)
Green = (0,255,0)
speed = 3
speed_x = 2
speed_y = 2
display.set_caption('Game of Sanchir')
clock = time.Clock()
game_over = False
a = 0
s = 0
d = 1
color = White
color2 = White
while not game_over:
    window.fill(Black)
    draw.rect(window,White,(0,340,500,10))
    draw.rect(window,color,(x1,y1,ert,20))
    draw.rect(window,color,(x2,y2,ert2,20))
    draw.circle(window,White,(x3,y3,),25)
    x3 += speed_x
    y3 += speed_y
    if d < 0:
        if draw.rect(window,White,(0,340,500,10)).colliderect(draw.circle(window,White,(x3,y3,),25)):
            speed_y *= -1
    if y3 < 25:
        a += 1
        print('Player1:',a,'|','Player2:',s)
        x1 = 0
        y1 = 680
        x2 = 0
        y2 = 0
        x3 = 250
        y3 = 350
        speed_y *= -1
    if x3 > 475 or x3 < 25:
        speed_x *= -1
    if y3 > 700:
        s += 1
        print('Player1:',a,'|','Player2:',s)
        x1 = 0
        y1 = 680
        x2 = 0
        y2 = 0
        x3 = 250
        y3 = 350
        speed_y = 2
    for i in event.get():
        if i.type == QUIT:
            game_over = True
        if i.type == KEYDOWN:
            if i.key == K_2:
                ert += 10
        if i.type == KEYDOWN:
            if i.key == K_3:
                ert -= 10
        if i.type == KEYDOWN:
            if i.key == K_1:
                speed_y *= -1
        if i.type == KEYDOWN:
            if i.key == K_b:
                color = Blue
        if i.type == KEYDOWN:
            if i.key == K_n:
                color = White
        if i.type == KEYDOWN:
            if i.key == K_g:
                color = Green
        if i.type == KEYDOWN:
            if i.key == K_4:
                d *= -1
        if i.type == KEYDOWN:
            if i.key == K_5:
                x1 = 0
                ert = 500
    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < width - ert:
        x1 += speed
    if keys_pressed[K_d] and x2 < width - ert2:
        x2 += speed
    if keys_pressed[K_a] and x2 > 0:
        x2 -= speed
    if draw.rect(window,color,(x1,y1,ert,20)).colliderect(draw.circle(window,White,(x3,y3,),25,)):
        speed_y *= -1
    if draw.rect(window,color2,(x2,y2,ert2,20)).colliderect(draw.circle(window,White,(x3,y3,),25,)):
        speed_y *= -1
    display.flip()
    clock.tick(FPS)
