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

    comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

    all_sprites.update()
    

    hits = pg.sprite.spritecollide(blueguy, enemy_group, True)
    if hits:
        blueguy.life -= 1
        print(blueguy.life)
        if blueguy.life <= 0:
            blueguy.kill()

    

    if len(enemy_group) < 10:
        bunny = Enemy()
        all_sprites.add(bunny)
        enemy_group.add(bunny)

    all_sprites.draw(screen)

    text_hp = comic_sans30.render(str(blueguy.life), False, BLACK)
    screen.blit(text_hp(10,10))
        

    pg.display.update()
    