import pygame
import random

#engo que pasar esto a clases
"""
class EasyEnemy():
    def __init__(self,height:int, width:int, image:str):
        self.height = height
        self.width = width
        self.image = pygame.image.load(image)
        
    # Function to create a new enemy
    def create_enemy(self,SCREEN_WIDTH,SCREEN_HEIGHT)-> list:
        enemies_sintaxError = []
        side = random.randint(1, 4)
        if side == 1:  # Top
            x = random.randint(0, SCREEN_WIDTH - self.width)
            y = -self.height
        elif side == 2:  # Right
            x = SCREEN_WIDTH
            y = random.randint(0, SCREEN_HEIGHT - self.height)
        elif side == 3:  # Bottom
            x = random.randint(0, SCREEN_WIDTH - self.width)
            y = SCREEN_HEIGHT
        else:  # Left
            x = - self.height
            y = random.randint(0, SCREEN_HEIGHT - self.width)
        enemy = pygame.Rect(x, y, self.width, self.height)
        enemies_sintaxError.append(enemy)
        return enemies_sintaxError

    def caminar(self,player_pos_x,player_pos_y,player_vel,enemies_sintaxError): 
        for enemy in enemies_sintaxError:
            if enemy.x < player_pos_x:
                enemy.x += player_vel -4
                print(enemy.x)
            elif enemy.x > player_pos_x:
                enemy.x -= player_vel -4
            if enemy.y < player_pos_y:
                enemy.y += player_vel -4
            elif enemy.y > player_pos_y:
                enemy.y -= player_vel -4
                
"""