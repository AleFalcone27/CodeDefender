import pygame

class MainChar():
    def __init__(self, pos_x:int, pos_y:int, width:int, height:int, image:str, vel:int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self. height = height
        self.image = pygame.image.load(image)
        self.vel = vel

    def caminar(self,dir,player_pos,player_vel=5):
        match dir:
            # Nos guardamos el valor de la posicion menos o mas la velocidad segun corresponda y retornamos la misma 
            case "up":
                player_pos -= player_vel
                self.image = pygame.image.load("Images\programadorUp.png")
                return player_pos
            
            case "down":
                player_pos += player_vel
                self.image = pygame.image.load("Images\programador.png")
                return player_pos
            case "left":
                player_pos -= player_vel
                return player_pos
            case "rigth":
                player_pos += player_vel
                return player_pos
            
    
    def get_rect(self, posx, posy):
        return pygame.Rect(posx, posy, self.width, self.height)