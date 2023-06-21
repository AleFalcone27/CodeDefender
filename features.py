import pygame
from pygame.locals import *
import sys

from Puntuacion import crear_registro,obtener_tabla_de_puntuaciones

pygame.init()

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
            
def end_game(screen,elapsed_time,score):
        flag = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            
            if flag == False: 
                intro = pygame.image.load("Images\Lose.png")
                screen.blit(intro, (0,0))
                pygame.display.flip()
                nombre = input("INGRESA TU NOMBRE: ")
                nombre = nombre.capitalize()
                nombre = nombre.strip(" ")
                crear_registro(nombre,score,elapsed_time)
                obtener_tabla_de_puntuaciones(screen)
                flag = True


