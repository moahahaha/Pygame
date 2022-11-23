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


all_sprites = pg.sprite.Group()
enemy_group = pg.sprite.Group()


blueguy = Player()
bunny = Enemy()
all_sprites.add(blueguy, bunny)
enemy_group.add(bunny)




screen = pg.display.set_mode((HEIGHT,WIDTH))
bg = pg.image.load("Background forest.jpg")
bg = pg.transform.scale(bg, (1000, 1000))

comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
  
score = 0

FPS = 120
clock = pg.time.Clock()






playing = True
while playing: 
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False 
            
            

    screen.blit(bg,(0,0))
  
    
    all_sprites.update()
    
    text_player_hp = comic_sans30.render(str(blueguy.life), False, WHITE)  
    text_score_hp = comic_sans30.render(str(score), False, WHITE) 
    
    

    hits = pg.sprite.spritecollide(blueguy, enemy_group, True)
    if hits:
        blueguy.life -= 1
        print(blueguy.life)
        if blueguy.life <= 0:
            blueguy.kill()
            blueguy = Player()
            all_sprites.add(blueguy)
            score = 0





    for enemy in enemy_group:
        if enemy.pos.x < -100:
            enemy.kill()
            score += 100



    if len(enemy_group) < 7:
        bunny = Enemy()
        all_sprites.add(bunny)
        enemy_group.add(bunny)

    all_sprites.draw(screen)


    screen.blit(text_player_hp,(10,10))
    screen.blit(text_score_hp,(900,10))
    
        

    pg.display.update()
    