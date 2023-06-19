import pygame
from rock_element import Rocks

# font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
# score_text = font.render("Score: " + str(score), True, "BLACK")
# screen.blit(score_text, (10, 10))
def draw_round(screen,level_text):
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    level_text = font.render(level_text , True, "BLACK")
    screen.blit(level_text, (500, 10))  
    
def round(score,screen):    
    if score == 0:
        draw_round(screen,"TUTORIAL")
    if score >= 1 and score < 19: 
        draw_round(screen,"ROUND 1")  
    if score > 18 and score < 34:
        draw_round(screen,"ROUND 2")
    if score > 33 and score < 58:
        draw_round(screen,"ROUND 3")
    if score > 33 and score < 58:
        draw_round(screen,"ROUND 3")


def tutorial(enemies,create_enemy):
        if len(enemies) < 1:
            create_enemy()

def lvl_1 (enemies,create_enemy,list_rocks,screen):
    if len(list_rocks) < 8:
        list_rocks.append(Rocks("Images\\rock.png", 40, 200,250))
    if len(enemies) < 5:
        create_enemy()

def lvl_2(enemies,create_enemy,list_rocks):
    if len(list_rocks) < 9:
        list_rocks.append(Rocks("Images\\rock.png", 40, 350,100))
    if len(enemies) < 10:
        create_enemy()
        
def lvl_3(enemies,create_enemy,list_rocks):
    if len(list_rocks) < 10:
        list_rocks.append(Rocks("Images\\rock.png", 40, 500,700))
    if len(enemies) < 15:
        create_enemy()
        
        
def lvl_4(enemies,create_enemy,list_rocks):
    if len(list_rocks) <= 11:
        list_rocks.append(Rocks("Images\\rock.png", 40, 250,300))
    if len(enemies) < 20:
        create_enemy()
        


