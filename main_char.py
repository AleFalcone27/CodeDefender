import pygame

class MainCharacter():
    tipo = "MainCharacter"
    def __init__(self, id, image, hit_box) -> None:
        self.id = id
        self.image_1 = image
        self.hit_box = hit_box
        
        
        # def move(self,direccion):
        #     if direccion == "left":
        #         main_pos.x -= 5
        #     if direccion == "rigth":
        #         main_pos.x += 5
        #     if direccion == "down":
        #         main_pos.y += 5
        #     if direccion == "up":
        #         main_pos.y -= 5
            
    # # Caminar
    # def walk(self, direccion):   
    #     pass
        
    # #Salto
    # def dash(self, distancia):
    #     pass





