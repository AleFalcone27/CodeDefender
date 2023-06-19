import pygame

def draw_score(score,screen):
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    score_text = font.render("Score: " + str(score), True, "BLACK")
    screen.blit(score_text, (10, 10))