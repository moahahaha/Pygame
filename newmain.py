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
        self.bg = pg.image.load("Background forest.jpg")
        self.bg = pg.transform.scale(self.bg, (self.HEIGHT, self.WIDTH))

        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
  
        self.FPS = 120
        self.clock = pg.time.Clock()
        
        self.new()

    
    
    
    def new(self):
        
        self.all_sprites = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()

        self.blueguy = Player()
        self.bunny = Enemy()
        
        self.all_sprites.add(self.blueguy, self.bunny)
        self.enemy_group.add(self.bunny)
        
        
        self.score = 0
        self.text_player_hp = self.comic_sans30.render(str(self.blueguy.life), False, self.WHITE)  
        self.text_score_hp = self.comic_sans30.render(str(self.score), False,  self.WHITE) 
    
        
        self.run()  
    
    
    
    def run(self):
        playing = True
        while playing:
            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing = False 
                    
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        self.new 
                    

            self.screen.blit(self.bg,(0,0))
        
            
            self.all_sprites.update()
            
            
            

            hits = pg.sprite.spritecollide(self.blueguy, self.enemy_group, True)
            if hits:
                blueguy.life -= 1
                print(blueguy.life)
                if blueguy.life <= 0:
                    blueguy.kill()
                    blueguy = Player()
                    self.all_sprites.add(blueguy)
                    score = 0



            for enemy in self.enemy_group:
                if enemy.pos.x < -100:
                    enemy.kill()
                    score += 100



            if len(self.enemy_group) < 7:
                bunny = Enemy()
                self.all_sprites.add(bunny)
                self.enemy_group.add(bunny)

            self.all_sprites.draw(self.screen)


            self.screen.blit(self.text_player_hp,(10,10))
            self.screen.blit(self.text_score_hp,(900,10))
            
                

            pg.display.update()

g = Game()