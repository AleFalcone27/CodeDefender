import pygame
from pygame.locals import *
import sys

def draw_score(score,screen):
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    score_text = font.render("Score: " + str(score), True, "BLACK")
    screen.blit(score_text, (10, 10))

def start_game():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                else:
                    return False
            
def end_game(screen):
        
        for event in pygame.event.get(): ##SACAR ESTE WHILE TRUE 
            if event.type == QUIT:
                 sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    nombre = input("INGRESA TU NOMBRE: ") 



        font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 40)
        end_text = font.render("YOU LOSE", True, "BLACK")
        screen.blit(end_text, (450, 270))
        pygame.display.flip()



        # intro = pygame.image.load("Images\intro.png")
        # screen.blit(intro, (0,0))