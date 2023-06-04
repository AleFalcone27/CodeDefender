import pygame

class MainCharacter():
    tipo = "MainCharacter"
    def __init__(self, id, image, image_up, hit_box) -> None:
        self.id = id
        self.image = image
        self.image_up = image_up
        self.hit_box = hit_box
        
        
    def caminar(self,dir,pos,vel):
        match dir:
            case "up":
                pos.y -= vel
            case "down":
                pos.y += 5
            case "left":
                pos.x -= 5
            case "rigth":
                pos.x += 5







