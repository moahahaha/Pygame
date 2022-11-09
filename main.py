import pygame as pg
from random import randint
from sprites import *

pg.init()

screen = pg.display.set_mode((1000,1000))



#rgb
WHITE = (255,255,255)
BLACK = (0,0,0)
GRØNN_BLÅ = (100,200,150)


all_sprites = pg.sprite.Group()


blueguy = Player()
all_sprites.add(blueguy)



FPS = 120
clock = pg.time.Clock()


playing = True
while playing: 
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 



    screen.fill(GRØNN_BLÅ)

    all_sprites.update()

    

    all_sprites.draw(screen)



    pg.display.update()
    