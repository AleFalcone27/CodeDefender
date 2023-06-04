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
        self.rect = 20 
        

    def easy_enemy_update(self,screen,easy_enemy_list):
        for i in easy_enemy_list:
            i = pygame.Rect(self.posy,self.posx , self.width, self.height)
            pygame.draw.rect(screen,(250,0,0),i)

    def easy_enemy_create_list(cant):
        easy_enemy_list = []
        for easy_enemy in range(cant):
            easy_enemy_list.append(easyEnemy())
        return easy_enemy_list
    
    ## CHEKEAR LA LINEA 18 
    ## AHI TENEMOS QEU GENERAR UN RECTANGULO 
    ## VIDEO DE CLASS MIN 45.32 