import pygame as pg

pg.init()

screen = pg.display.set_mode((1000,1000))

player_img = pg.image.load("Player.PNG")
player_img = pg.transform.scale(player_img,(100,100))

#rgb
WHITE = (255,255,255)
BLACK = (0,0,0)
GRØNN_BLÅ = (100,200,150)


x = 350
y = 250
direction_x = 1
direction_y = 1

speed = 5
FPS = 120
clock = pg.time.Clock()





playing = True
while playing: #game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 

    # move box
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= speed

    if keys[pg.K_s]:
        y += speed

    if keys[pg.K_a]:
        x -= speed

    if keys[pg.K_d]:
        x += speed
       

    screen.fill(GRØNN_BLÅ)


    if x > 900:
        x = 900
    if x < 0:
        x = 0
    if y > 900:
        y = 900
    if y < 0:
        y = 0
        

    screen.blit(player_img, (x,y))

    pg.display.update()
    