import pygame
from rock_element import Rocks

def draw_round(screen,level_text):
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    level_text = font.render(level_text , True, "BLACK")
    screen.blit(level_text, (500, 10))  
    
def round(score,screen):    
    if score >= 0 and score < 2:
        draw_round(screen,"TUTORIAL")
    if score >= 2 and score < 10: 
        draw_round(screen,"ROUND 1")  
    if score >=10  and score < 21:
        draw_round(screen,"ROUND 2")
    if score >= 21 and score < 43:
        draw_round(screen,"ROUND 3")
    if score >= 43 and score < 69:
        draw_round(screen,"ROUND 4")
    if score >= 69 :
        draw_round(screen,"FINAL ROUND")
    


def tutorial(enemies,create_enemy):
    if len(enemies) < 2:
        create_enemy()

def lvl_1 (enemies,create_enemy,list_rocks):
    if len(list_rocks) == 7:
        list_rocks.append(Rocks("Images\\rock.png", 40, 200,250))
        list_rocks.append(Rocks("Images\\rock.png", 40, 350,100))
    if len(enemies) < 5:
        create_enemy()

def lvl_2(enemies,create_enemy,list_rocks):
    if len(list_rocks) == 9:
        list_rocks.append(Rocks("Images\\rock.png", 40, 350,100))
        list_rocks.append(Rocks("Images\\rock.png", 40, 500,700))
    if len(enemies) < 7:
        create_enemy()
        
def lvl_3(enemies,create_enemy,list_rocks):
    if len(list_rocks) == 11:
        list_rocks.append(Rocks("Images\\rock.png", 40, 350,550))
        list_rocks.append(Rocks("Images\\rock.png", 40, 525,689))
    if len(enemies) < 10:
        create_enemy()
        
def lvl_4(enemies,create_enemy,list_rocks):
    if len(list_rocks) == 13:
        list_rocks.append(Rocks("Images\\rock.png", 40,  100,540))
        list_rocks.append(Rocks("Images\\rock.png", 40,  900,540))
    if len(enemies) < 20:
        create_enemy()
        
def lvl_5(enemies,create_enemy):
        if len(enemies) < 20:
            create_enemy()

