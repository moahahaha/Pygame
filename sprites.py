import pygame as pg
from random import randint
vec = pg.math.Vector2


player_img = pg.image.load("Player.PNG")
player_img = pg.transform.scale(player_img,(70,70))

player_left_img = pg.transform.flip(player_img, True, False)


RUNNING1 = pg.image.load("Run1.png")
RUNNING1 = pg.transform.scale(RUNNING1,(70,70))
RUNNING2 = pg.image.load("Run2.png")
RUNNING2 = pg.transform.scale(RUNNING2,(70,70))
RUNNING3 = pg.image.load("Run3.png")
RUNNING3 = pg.transform.scale(RUNNING3,(70,70))
RUNNING4 = pg.image.load("Run4.png")
RUNNING4 = pg.transform.scale(RUNNING4,(70,70))
RUNNING5 = pg.image.load("Run5.png")
RUNNING5 = pg.transform.scale(RUNNING5,(70,70))
RUNNING6 = pg.image.load("Run6.png")
RUNNING6 = pg.transform.scale(RUNNING6,(70,70))

running_frames = [RUNNING1, RUNNING2, RUNNING3, RUNNING4, RUNNING5, RUNNING6]

HURT1 = pg.image.load("Hurt1.png")
HURT1 = pg.transform.scale(HURT1,(70,70))
HURT2 = pg.image.load("Hurt2.png")
HURT2 = pg.transform.scale(HURT2,(70,70))
HURT3 = pg.image.load("Hurt3.png")
HURT3 = pg.transform.scale(HURT3,(70,70))
HURT4 = pg.image.load("Hurt4.png")
HURT4 = pg.transform.scale(HURT4,(70,70))

hurting_frames = [HURT1, HURT2, HURT3, HURT4]

'''
for frame in running_frames:
    frame = pg.transform.scale(frame, (500,500))
'''

enemy_img = pg.image.load("Enemy.png")
enemy_img = pg.transform.scale(enemy_img,(100,100))

food_img = pg.image.load("hotdog.png")
food_img = pg.transform.scale(food_img,(60,60))

heart_img = pg.image.load("heart.png")
heart_img = pg.transform.scale(heart_img,(50,50))



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.current_frame = 0
        self.last_update = 0
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 4
        self.life = 5
        
        self.hurting = False
        self.running = False
        self.left = False
        
        self.running_frames = running_frames
        self.hurting_frames = hurting_frames

        self.image_left = player_left_img
       

    def update(self):
        
    
        
        '''
        self.move_to =vec(pg.mouse.get_pos())
        self.move_vector = self.move_to - self.pos
        self.pos += self.move_vector.normalize() * self.speed
        self.rect.center = self.pos
        '''
        keys =pg.key.get_pressed()
        
        if keys[pg.K_w]:
            self.pos.y -= self.speed
            self.running = True
        if keys[pg.K_s]:
            self.pos.y += self.speed
            self.running = True
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.running = True
            self.left = False
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.running = True
            self.left = True

        if self.pos.x < 40:
            self.pos.x = 40
        if self.pos.x > 960:
            self.pos.x = 960
        if self.pos.y < 40:
            self.pos.y = 40
        if self.pos.y > 940:
            self.pos.y = 940
      
        self.animate()
        self.rect.center = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        
        if self.running:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_frames)
                self.image = self.running_frames[self.current_frame]
                self.rect = self.image.get_rect()
        
                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)
        
        if self.hurting:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.hurting_frames)
                self.image = self.hurting_frames[self.current_frame]
                self.rect = self.image.get_rect()
        

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(1000,2000),randint(10,950))
        self.rect.center = self.pos
        self.speed = 5

        
    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

            
class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = food_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(1000,2000),randint(10,950))
        self.rect.center = self.pos
        self.speed = 5
    
    def update(self):
        self.rect.center = self.pos
        
        self.pos.x -= self.speed
        
        
class Heart(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = heart_img
        self.rect = self.image.get_rect()
        self.pos = vec(randint(2000,3000),randint(10,950))
        self.rect.center = self.pos
        self.speed = 5
        
    def update(self):
        self.rect.center = self.pos
        
        self.pos.x -= self.speed