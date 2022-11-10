import pygame as pg
from random import randint
from sprites import *

pg.init()


#rgb
WHITE = (255,255,255)
BLACK = (0,0,0)
GRØNN_BLÅ = (100,200,150)
WIDTH = 1000
HEIGHT = 1000


screen = pg.display.set_mode((HEIGHT,WIDTH))


all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()


blueguy = Player()
bunny = Enemy()
all_sprites.add(blueguy, bunny)
enemy_group.add(bunny)



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

    hits = pg.sprite.spritecollide(blueguy, enemy_group, True)
    if hits:
        print("collided")

    if len(enemy_group) < 10:
        bunny = Enemy()
        all_sprites.add(bunny)
        enemy_group.add(bunny)

    all_sprites.draw(screen)


    pg.display.update()
    