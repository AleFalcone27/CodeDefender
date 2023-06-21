import pygame

class Rocks():
    def __init__(self,image,rescale,pos_x,pos_y) -> None:
        self.pos_x = pos_x 
        self.pos_y = pos_y
        self.rescale = rescale
        self.image = pygame.image.load(image)
        

    # DIBUJAMOS LAS PIEDRAS
    def draw_rocks(self,list_rocks,screen):
        for rock in list_rocks:
            rock_surface = self.image
            rock_surface = pygame.transform.scale(rock_surface, (rock.rescale, rock.rescale))
            rock_rect = pygame.Rect(self.pos_x, self.pos_y, self.rescale, self.rescale)
            screen.blit(rock_surface, (rock_rect))
        return rock_rect


# VEr si puedo agregar la colision como atributo