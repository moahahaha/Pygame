import pygame as pg

from sprites import*




class Game():
    
    def __init__(self):
        pg.init()
        
        #rgb
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.GRØNN_BLÅ = (100,200,150)

        self.WIDTH = 1000
        self.HEIGHT = 1000
        
        self.screen = pg.display.set_mode((self.HEIGHT,self.WIDTH))
        self.bg = pg.image.load("background.jpg")
        self.bg = pg.transform.scale(self.bg, (self.HEIGHT, self.WIDTH))

        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
  
        self.FPS = 120
        self.clock = pg.time.Clock()
        
        self.new()

    
    
    
    def new(self):
        
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.food_group = pg.sprite.Group()
        self.heart_group = pg.sprite.Group()

        self.blueguy = Player()
        
        self.all_sprites.add(self.blueguy)
    
        
        
        self.score = 0
        self.text_player_hp = self.comic_sans30.render(str(self.blueguy.life), False, self.WHITE)  
        self.text_score_hp = self.comic_sans30.render(str(self.score), False,  self.WHITE) 
    
        
        self.run()  
    
    
    
    def run(self):
        i = 0
        playing = True
        while playing:
            self.clock.tick(self.FPS)                                     
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False 
                    
                
            self.screen.blit(self.bg,(i,0))
            self.screen.blit(self.bg,(self.WIDTH+1,0))
            if (i == -self.WIDTH):
                self.screen.blit(self.bg,(self.WIDTH+i,0))
                i = 0
            i-=1
        
            
            self.all_sprites.update()
            
            

            hits = pg.sprite.spritecollide(self.blueguy, self.enemy_group, True)
            if hits:
                self.blueguy.hurting = True
                self.blueguy.last_hurt = pg.time.get_ticks()
                self.score -= 50
                self.blueguy.life -= 1
                if self.blueguy.life <= 0:
                    self.blueguy.kill()
                    self.blueguy = Player()
                    self.all_sprites.add(self.blueguy)
                    self.score = 0
                    
            hits = pg.sprite.spritecollide(self.blueguy, self.food_group, True)
            if hits:
                self.score += 100

            hits = pg.sprite.spritecollide(self.blueguy, self.heart_group, True)
            if hits:
                self.blueguy.life += 1
                if self.blueguy.life >=  5:
                    self.blueguy.life = 5
                




            for enemy in self.enemy_group:
                if enemy.pos.x < -100:
                    enemy.kill()
                  
            if len(self.enemy_group) < 7:
                bunny = Enemy()
                self.all_sprites.add(bunny)
                self.enemy_group.add(bunny)
                
            
        
        
            for food in self.food_group:
                if food.pos.x < -100:
                    food.kill()        
            
            if len(self.food_group) < 2:
                hotdog = Food()
                self.all_sprites.add(hotdog)
                self.food_group.add(hotdog)



            for heart in self.heart_group:
                if heart.pos.x < -100:
                    heart.kill()
                    
            if len(self.heart_group) < 1:
                heart = Heart()
                self.all_sprites.add(heart)
                self.heart_group.add(heart)



            self.all_sprites.draw(self.screen)


            self.screen.blit(self.text_player_hp,(10,10))
            self.screen.blit(self.text_score_hp,(900,10))
            
            self.text_player_hp = self.comic_sans30.render(str(self.blueguy.life), False, self.WHITE)  
            self.text_score_hp = self.comic_sans30.render(str(self.score), False,  self.WHITE) 
        

            pg.display.update()

g = Game()     