import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

pygame.init()
pygame.mixer.init()

score = 1

enemy_killed_sound = pygame.mixer.Sound("Sounds\enemyKilled.wav")
enemy_killed_sound.set_volume(0.2)  # Establece el volumen del sonido de enemigo muerto al 30%


def move_bullet (bullets,bullet_vel):
    bullets_to_remove = []
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y, bullet_dir_x, bullet_dir_y = bullet
        bullet_x += bullet_dir_x * bullet_vel
        bullet_y += bullet_dir_y * bullet_vel
        if bullet_x < 0 or bullet_x > SCREEN_WIDTH or bullet_y < 0 or bullet_y > SCREEN_HEIGHT:
            bullets_to_remove.append(i)
        else:
            bullets[i] = (bullet_x, bullet_y, bullet_dir_x, bullet_dir_y)
    return bullets_to_remove


def remove_bullet_off_screen(bullets_to_remove,bullets): #COMO FUNCIONA ESTA? 
    for i in reversed(bullets_to_remove):
        bullets.pop(i)
    return bullets
            
            
def remove_bullet_when_hit_enemy(bullets_to_remove,bullets):
    for i in reversed(bullets_to_remove):
        try:
            bullets.pop(i)
        except IndexError:
            pass
    return bullets
    
def bullet_colision(bullets_to_remove,bullets,enemies,bullet_size):
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y, _, _ = bullet
        bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size)
        for j, enemy in enumerate(enemies):
            if bullet_rect.colliderect(enemy):
                enemy_killed_sound.play()
                bullets_to_remove.append(i)
                enemies.pop(j)
                bullet_hit  = True # Incrementar el puntaje por cada enemigo alcanzado
                return bullet_hit
            
            
