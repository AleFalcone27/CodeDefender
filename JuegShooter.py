import pygame
import random
from player import MainChar
from rock_element import Rocks

from pygame.locals import *

# Inicializamos Pygame
pygame.init()

# PANTALLA
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Shooter")

# Creamos una instancia de la clase mainChar
player = MainChar(SCREEN_WIDTH / 2 - 50 / 2, SCREEN_HEIGHT / 2 - 100 / 2, 50, 100, "Images\programador.png", 5)

# Obtenemos los atributos del obj player para utilizarlos en nuestro juego
PLAYER_WIDTH = player.width
PLAYER_HEIGHT = player.height
player_vel = player.vel

# Bullet properties
bullet_size = 10
bullet_vel = 10
bullets = []

# Enemy properties
easy_enemy_height = 30
easy_enemy_width = 74
enemies = []

# Puntaje
score = 0


# SOUNDS
shot_sound = pygame.mixer.Sound("Sounds\shootSound.wav")
enemy_killed_sound = pygame.mixer.Sound("Sounds\enemyKilled.wav")
lose_sound = pygame.mixer.Sound("Sounds\loseSound.wav")
shot_sound.set_volume(0.1)  # Establece el volumen del sonido de disparo al 50%
enemy_killed_sound.set_volume(0.2)  # Establece el volumen del sonido de enemigo muerto al 30%

# PAUSA
pause = False


# CREMOS LA LISTA DE PIEDRAS
list_rocks = [
    Rocks('Images\\rock.png', 40, 0, 0),
    Rocks("Images\\rock.png", 40, 50, 350),
    Rocks("Images\\rock.png", 40, 900, 250),
    Rocks("Images\\rock.png", 40, 300, 425),
    Rocks("Images\\rock.png", 40, 800, 125),
    Rocks("Images\\rock.png", 40, 400, 425),
    Rocks("Images\\rock.png", 40, 800, 125)
]


# FUNCION PARA CREAR NUEVOS ENEMIGOS
def create_enemy():
    side = random.randint(1, 4)
    if side == 1:  # Top
        x = random.randint(0, SCREEN_WIDTH - easy_enemy_width)
        y = -easy_enemy_height
    elif side == 2:  # Right
        x = SCREEN_WIDTH
        y = random.randint(0, SCREEN_HEIGHT - easy_enemy_height)
    elif side == 3:  # Bottom
        x = random.randint(0, SCREEN_WIDTH - easy_enemy_width)
        y = SCREEN_HEIGHT
    else:  # Left
        x = -easy_enemy_height
        y = random.randint(0, SCREEN_HEIGHT - easy_enemy_width)
    enemy = pygame.Rect(x, y, easy_enemy_width, easy_enemy_height)
    enemies.append(enemy)


# GAME LOOP
running = True
clock = pygame.time.Clock()

# INICIALIZAMOS EL RELOJ
start_time = pygame.time.get_ticks()
elapsed_time = 0

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == MOUSEBUTTONDOWN:
            
            shot_sound.play()
            
            bullet_x = player.pos_x + PLAYER_WIDTH / 2 - bullet_size / 2
            bullet_y = player.pos_y + PLAYER_HEIGHT / 2 - bullet_size / 2

            # Obtenemos la posicion del cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # bullet_dir_x y bullet_dir_y son la direccion en la que va la bala
            bullet_dir_x = mouse_x - bullet_x
            bullet_dir_y = mouse_y - bullet_y

            bullet_dir_length = max(abs(bullet_dir_x), abs(bullet_dir_y))
            bullet_dir_x /= bullet_dir_length
            bullet_dir_y /= bullet_dir_length
            bullets.append((bullet_x, bullet_y, bullet_dir_x, bullet_dir_y))

    # Movimientos del jugador
    keys = pygame.key.get_pressed()
    if keys[K_a] and player.pos_x > 0:
        player.pos_x = player.caminar("left", player.pos_x)
    if keys[K_d] and player.pos_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player.pos_x = player.caminar("rigth", player.pos_x)
    if keys[K_w] and player.pos_y > 0:
        player.pos_y = player.caminar("up", player.pos_y)
    if keys[K_s] and player.pos_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player.pos_y = player.caminar("down", player.pos_y)


    # Move the bullets
    bullets_to_remove = []
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y, bullet_dir_x, bullet_dir_y = bullet
        bullet_x += bullet_dir_x * bullet_vel
        bullet_y += bullet_dir_y * bullet_vel
        if bullet_x < 0 or bullet_x > SCREEN_WIDTH or bullet_y < 0 or bullet_y > SCREEN_HEIGHT:
            bullets_to_remove.append(i)
        else:
            bullets[i] = (bullet_x, bullet_y, bullet_dir_x, bullet_dir_y)


    # Remove bullets that have gone off-screen
    for i in reversed(bullets_to_remove):
        bullets.pop(i)

    # Move the enemies
    for enemy in enemies:
        if enemy.x < player.pos_x:
            enemy.x += player.vel - 4
        elif enemy.x > player.pos_x:
            enemy.x -= player.vel - 4
        if enemy.y < player.pos_y:
            enemy.y += player.vel - 4
        elif enemy.y > player.pos_y:
            enemy.y -= player.vel - 4


    # Check collision between bullets and enemies
    bullets_to_remove = []
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y, _, _ = bullet
        bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size)
        for j, enemy in enumerate(enemies):
            if bullet_rect.colliderect(enemy):
                enemy_killed_sound.play()
                bullets_to_remove.append(i)
                enemies.pop(j)
                score += 1  # Incrementar el puntaje por cada enemigo alcanzado

    # Remove bullets and enemies that have collided
    for i in reversed(bullets_to_remove):
        bullets.pop(i)

    # Check collision between player and enemies
    player_rect = pygame.Rect(player.pos_x, player.pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False  # Game over if player collides with an enemy

    # Generate new enemies
    if len(enemies) < 5:
        create_enemy()

    # Draw the game
    screen.fill("WHITE")
    fondo = pygame.image.load("Images\\floor.png")
    screen.blit(fondo, (0, 0))

    # DIBUJAMOS LAS PIEDRAS
    for rock in list_rocks:
        rock_surface = rock.image
        rock_surface = pygame.transform.scale(rock_surface, (rock.rescale, rock.rescale))
        rock_rect = pygame.Rect(rock.pos_x, rock.pos_y, rock.rescale, rock.rescale)
        screen.blit(rock_surface, (rock_rect))
        
        # Verificar si el lado derecho de rect1 choca con el lado izquierdo de rect2
        if player_rect.colliderect(rock_rect):
            if player.pos_y > rock.pos_y:
                player.pos_y += player.vel
            if player.pos_y < rock.pos_y:
                player.pos_y -= player.vel
            if player.pos_x < rock.pos_x:
                player.pos_x -= player.vel
            if player.pos_x > rock.pos_x:
                player.pos_x += player.vel
            

    # DIBUJAMOS AL PERSONAJE PRINCIPAL
    image = player.image  # Accedemos al atributo imagen
    image_rect = image.get_rect()  # Obtener el rectángulo de la imagen
    image_rect.center = (player.pos_x + 50 // 2, player.pos_y + 100 // 2)  # Centramos el rectangulo con la posicion de nuestro personaje
    screen.blit(image, image_rect)

    # DIBUJAMOS LAS BALAS
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet[:2] + (bullet_size, bullet_size))

    # DIBUJAMOS LOS ENEMIGOS
    for enemy in enemies:
        easy_enemy_image = pygame.image.load("Images\\sintaxError_image.png")
        screen.blit(easy_enemy_image, enemy)

    # DIBUJAMOS EL SCORE
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    score_text = font.render("Score: " + str(score), True, "BLACK")
    screen.blit(score_text, (10, 10))

    # DIBUJAMOS EL CRONOMETRO
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
    elapsed_time_text = font.render("Time: " + str(elapsed_time // 1000) , True, "BLACK")
    screen.blit(elapsed_time_text, (10, 40))
    pygame.font.get_fonts()

    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
