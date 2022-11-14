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
herolife = 5


screen = pg.display.set_mode((HEIGHT,WIDTH))


all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()


blueguy = Player()
bunny = Enemy()
all_sprites.add(blueguy, bunny)
enemy_group.add(bunny)



FPS = 120
clock = pg.time.Clock()

    
comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
print(herolife)

playing = True
while playing: 
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 


    text_player_hp = comic_sans30.render(str(herolife), False, (BLACK))
    screen.blit(text_player_hp,(10,10))

    screen.fill(GRØNN_BLÅ)

    all_sprites.update()
    

    hits = pg.sprite.spritecollide(blueguy, enemy_group, True)
    if hits:
        herolife -= 1

        

    if len(enemy_group) < 10:
        bunny = Enemy()
        all_sprites.add(bunny)
        enemy_group.add(bunny)

    all_sprites.draw(screen)


    pg.display.update()
    