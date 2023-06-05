import pygame
import random
from player import MainChar


from pygame.locals import *



# Inicializamos  Pygame
pygame.init()

# Set up the display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


player = MainChar(SCREEN_WIDTH / 2 - 50 / 2, SCREEN_HEIGHT / 2 - 100 / 2, 50 , 100 ,"programador.png", 5)



# Obtenemos los atributos del obj player para utilizalos en nuestro juego
PLAYER_WIDTH = player.width
PLAYER_HEIGHT = player.height
player_vel = player.vel
player_x = player.pos_x
player_y = player.pos_y


# Bullet properties
bullet_size = 10
bullet_vel = 10
bullets = []


# Enemy propertiess
easy_enemy_height = 30
easy_enemy_width = 74
enemy_vel = 3
enemies = []


# Function to create a new enemy
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

# Game loop
running = True
clock = pygame.time.Clock()

# Cronometro
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
            bullet_x = player_x + PLAYER_WIDTH / 2 - bullet_size / 2
            bullet_y = player_y + PLAYER_HEIGHT / 2 - bullet_size / 2
            # Obtenemos la posicion del cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet_dir_x = mouse_x - bullet_x
            bullet_dir_y = mouse_y - bullet_y
            # Aca no se que carajos pasa INVESTIGAR
            bullet_dir_length = max(abs(bullet_dir_x), abs(bullet_dir_y))
            bullet_dir_x /= bullet_dir_length
            bullet_dir_y /= bullet_dir_length
            bullets.append((bullet_x, bullet_y, bullet_dir_x, bullet_dir_y))


    ## Hacemos el cronometro para guardar el tiempo transcurrido 
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    font = pygame.font.Font(None, 36)
    timer_text = font.render("Time: " + str(elapsed_time / 1000), True, "BLACK")
    screen.blit(timer_text, (10, 500))

    pygame.display.flip()
    
    # Movimientos del jugador
    keys = pygame.key.get_pressed()
    if keys[K_a] and player_x > 0:
        player_x = player.caminar("left",player_x)
    if keys[K_d] and player_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player_x = player.caminar("rigth",player_x)
    if keys[K_w] and player_y > 0:
        player_y = player.caminar("up",player_y)
    if keys[K_s] and player_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y = player.caminar("down",player_y)


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
        if enemy.x < player_x:
            enemy.x += enemy_vel -2
        elif enemy.x > player_x:
            enemy.x -= enemy_vel -2
        if enemy.y < player_y:
            enemy.y += enemy_vel -2
        elif enemy.y > player_y:
            enemy.y -= enemy_vel -2



    # Check collision between bullets and enemies
    bullets_to_remove = []
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y, _, _ = bullet
        bullet_rect = pygame.Rect(bullet_x, bullet_y, bullet_size, bullet_size)
        for j, enemy in enumerate(enemies):
            if bullet_rect.colliderect(enemy):
                bullets_to_remove.append(i)
                enemies.pop(j)
                break


    # Remove bullets and enemies that have collided
    for i in reversed(bullets_to_remove):
        bullets.pop(i)

    # Check collision between player and enemies
    player_rect = pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False  # Game over if player collides with an enemy

    # Generate new enemies
    if len(enemies) < 5:
        create_enemy()

    # Draw the game
    screen.fill(WHITE)


    # Accedemos al atributo image 
    image =  pygame.image.load(player.image)  
    # Obtener el rectángulo de la imagen 
    image_rect = image.get_rect()   
    # Centramos el rectangulo con la posicion de nuestro personaje
    image_rect.center = (player_x + 50 // 2, player_y + 100 // 2)
    screen.blit(image, image_rect)  

    for bullet in bullets:
        pygame.draw.rect(screen, (0,255,0), bullet[:2] + (bullet_size, bullet_size))

    for enemy in enemies:
        easy_enemy_image = pygame.image.load("sintaxError_image.png")
        pygame.draw.rect(screen, (255,255,0), enemy)
        screen.blit(easy_enemy_image, enemy)


    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
