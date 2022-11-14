import pygame as pg
from random import randint
vec = pg.math.Vector2


player_img = pg.image.load("Player.PNG")
player_img = pg.transform.scale(player_img,(100,100))

enemy_img = pg.image.load("Enemy.png")
enemy_img = pg.transform.scale(enemy_img,(100,100))



player_left_img = pg.transform.flip(player_img, True, False)

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 3

        self.image_left = player_left_img
       

    def update(self):
        self.rect.center = self.pos

        self.move_to =vec(pg.mouse.get_pos())
        self.move_vector = self.move_to - self.pos
        self.pos += self.move_vector.normalize() * self.speed
        self.rect.center = self.pos

        keys =pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        if keys[pg.K_s]:
            self.pos.y += self.speed
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = player_img
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = player_left_img

        if self.pos.x < 40:
            self.pos.x = 40
        if self.pos.x > 960:
            self.pos.x = 960
        if self.pos.y < 40:
            self.pos.y = 40
        if self.pos.y > 940:
            self.pos.y = 940
        


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.pos = vec(1100,randint(0,950))
        self.rect.center = self.pos
        self.speed = 3

        
    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 1000
            self.pos.y = randint(0,1000)

