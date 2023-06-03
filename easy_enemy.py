import random
import pygame

class easyEnemy():
    tipo = "Enemy"
    def __init__(self) -> None:
        self.id = id
        self.image_1 = pygame.image.load("easy_enemy.png")
        self.posx = random.randint(0,1280)
        self.posy = random.randint(0,720)
        self.width = 40
        self.height = 40
        

    def easy_enemy_create_list(cant):
        easy_enemy_list = []
        for easy_enemy in range(cant):
            easy_enemy_list.append(easyEnemy())
        return easy_enemy_list
        
    def easy_enemy_create(self,screen):
        return pygame.draw.rect(screen,(0,0,250),(self.posx, self.posy, self.width, self.height))
    
    


    
    
    
    ## AGREGARLE MOVIMIENTO A LOS ENEMIGOS
    
    
    

