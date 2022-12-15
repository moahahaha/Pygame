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

THROW1 = pg.image.load("Throw1.png")
THROW1 = pg.transform.scale(THROW1,(70,70))
THROW2 = pg.image.load("Throw2.png")
THROW2 = pg.transform.scale(THROW2,(70,70))
THROW3 = pg.image.load("Throw3.png")
THROW3 = pg.transform.scale(THROW3,(70,70))
THROW4 = pg.image.load("Throw4.png")
THROW4 = pg.transform.scale(THROW4,(70,70))

throwing_frames = [THROW1, THROW2, THROW3, THROW4]

HURT1 = pg.image.load("Hurt1.png")
HURT1 = pg.transform.scale(HURT1,(70,70))
HURT2 = pg.image.load("Hurt2.png")
HURT2 = pg.transform.scale(HURT2,(70,70))
HURT3 = pg.image.load("Hurt3.png")
HURT3 = pg.transform.scale(HURT3,(70,70))
HURT4 = pg.image.load("Hurt4.png")
HURT4 = pg.transform.scale(HURT4,(70,70))

hurting_frames = [HURT1, HURT2, HURT3, HURT4]

STANDING1 = pg.image.load("Stand1.png")
STANDING1 = pg.transform.scale(STANDING1,(70,70))
STANDING2 = pg.image.load("Stand1.png")
STANDING2 = pg.transform.scale(STANDING2,(70,70))

standing_frames = [STANDING1, STANDING2]

'''
for frame in running_frames:
    frame = pg.transform.scale(frame, (500,500))
'''


enemy_img = pg.image.load("Enemy.png")
enemy_img = pg.transform.scale(enemy_img,(100,100))

BUNNYRUN1 = pg.image.load("Bunnyrun1.png")
BUNNYRUN1 = pg.transform.scale(BUNNYRUN1,(90,90))
BUNNYRUN2 = pg.image.load("Bunnyrun2.png")
BUNNYRUN2 = pg.transform.scale(BUNNYRUN2,(90,90))
BUNNYRUN3 = pg.image.load("Bunnyrun3.png")
BUNNYRUN3 = pg.transform.scale(BUNNYRUN3,(90,90))
BUNNYRUN4 = pg.image.load("Bunnyrun4.png")
BUNNYRUN4 = pg.transform.scale(BUNNYRUN4,(90,90))
BUNNYRUN5 = pg.image.load("Bunnyrun5.png")
BUNNYRUN5 = pg.transform.scale(BUNNYRUN5,(90,90))
BUNNYRUN6 = pg.image.load("Bunnyrun6.png")
BUNNYRUN6 = pg.transform.scale(BUNNYRUN6,(90,90))
BUNNYRUN7 = pg.image.load("Bunnyrun7.png")
BUNNYRUN7 = pg.transform.scale(BUNNYRUN7,(90,90))

Bunnyrun_frames = [BUNNYRUN1,BUNNYRUN2,BUNNYRUN3,BUNNYRUN4,BUNNYRUN5,BUNNYRUN6,BUNNYRUN7]

food_img = pg.image.load("hotdog.png")
food_img = pg.transform.scale(food_img,(60,60))

heart_img = pg.image.load("heart.png")
heart_img = pg.transform.scale(heart_img,(50,50))

stone_img = pg.image.load("Rock.png")
stone_img = pg.transform.scale(stone_img,(20,20))


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.projectile_speed = 5

        self.current_frame = 0
        self.last_update = 0
        self.image = player_img
        self.rect = self.image.get_rect()
        self.pos = vec(100,100)
        self.rect.center = self.pos
        self.speed = 4
        self.life = 5
        
        self.standing = True
        self.hurting = False
        self.running = False
        self.left = False
        self.throwing = False
        
        self.last_hurt = 0
        self.last_throw = 0
        
        self.attack_direction_x = 0
        
        self.running_frames = running_frames
        self.hurting_frames = hurting_frames
        self.standing_frames = standing_frames
        self.throwing_frames = throwing_frames 

        self.image_left = player_left_img
       

    def update(self):
        
    
        
        '''
        self.move_to =vec(pg.mouse.get_pos())
        self.move_vector = self.move_to - self.pos
        self.pos += self.move_vector.normalize() * self.speed
        self.rect.center = self.pos
        '''
        keys =pg.key.get_pressed()
        
        self.standing = True
        self.running = False 
        self.throwing = False
        '''
        self.pos.y += 2 !!!      
        '''
        if keys[pg.K_w]:
            self.pos.y -= self.speed
            self.running = True
            self.standing = False
            
        if keys[pg.K_s]:
            self.pos.y += self.speed
            self.running = True
            self.standing = False
        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.running = True
            self.left = False
            self.standing = False
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.running = True
            self.left = True
            self.standing = False
            
        #self.attack_direction_x = 0
        if keys[pg.K_LEFT]:
            self.attack_direction_x = -self.projectile_speed
            self.throwing = True
        if keys[pg.K_RIGHT]:
            self.attack_direction_x = self.projectile_speed
            self.throwing = True
            
        if not self.attack_direction_x == 0:
            if keys[pg.K_SPACE]:
                self.attack()
                self.throwing = True
                
        
         

        if self.pos.x < 40:
            self.pos.x = 40
        if self.pos.x > 750:
            self.pos.x = 950
        if self.pos.y < 40:
            self.pos.y = 40
        if self.pos.y > 800:
            self.pos.y = 800
      
        self.animate()
        self.rect.center = self.pos
        
        

    def animate(self):
        now = pg.time.get_ticks()
        
        
        if self.hurting:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.hurting_frames)
                self.image = self.hurting_frames[self.current_frame]
                self.rect = self.image.get_rect()
                
            if self.last_hurt + 1000 < now:
                self.hurting = False
                
            
        elif self.throwing:
            if now - self.last_update > 100:
                self.last_update = now 
                self.current_frame = (self.current_frame + 1) % len(self.throwing_frames)
                self.image = self.throwing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                
            if self.last_throw + 1000 < now:
                self.throwing = False
                
                
                
                
                
        elif self.running:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.running_frames)
                self.image = self.running_frames[self.current_frame]
                self.rect = self.image.get_rect()
        
                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)
        
    
        elif self.standing:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                self.image = self.standing_frames[self.current_frame]
                self.rect = self.image.get_rect()
                
                if self.left:
                    self.image = pg.transform.flip(self.image, True, False)
        
                
    def attack(self):
        Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x, 0)  
                



class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
       self.groups = game.all_sprites, game.projectiles_grp 
       pg.sprite.Sprite.__init__(self, self.groups)
       self.game = game
       self.image = stone_img
       self.image.fill((255,0,0))
       self.rect = self.image.get_rect()
       self.pos = vec(x, y) 
       self.direction_x = direction_x
       self.direction_y = direction_y
       self.rect.center = self.pos   
       
    def update(self):
        self.rect.center = self.pos
        self.pos.x += self.direction_x     
        self.pos.y += self.direction_y


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.last_update = 0
        self.current_frame = 0
        self.pos = vec(randint(1000,2000),randint(10,950))
        self.rect.center = self.pos
        self.speed = 5
        
        self.bunnyrun = True
        
        self.bunnyrun_frames = Bunnyrun_frames
        
    def update(self):
        self.rect.center = self.pos
        
        self.pos.x -= self.speed
        
    
        self.animate()
        self.rect.center = self.pos


    def animate(self):      
        now = pg.time.get_ticks()
        
        if self.bunnyrun:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.bunnyrun_frames)
                self.image = self.bunnyrun_frames[self.current_frame]
                self.rect = self.image.get_rect()
                
                
                
                            
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
        self.pos = vec(randint(5000,6000),randint(10,950))
        self.rect.center = self.pos
        self.speed = 5
        
    def update(self):
        self.rect.center = self.pos
        
        self.pos.x -= self.speed