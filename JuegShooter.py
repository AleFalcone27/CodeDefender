import pygame
import random
from player import MainChar
from rock_element import Rocks


from pygame.locals import *

# Inicializamos  Pygame
pygame.init()

# PANTALLA
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Enemy Shooter")


# Creamos una instancia de la clase mainChar
player = MainChar(SCREEN_WIDTH / 2 - 50 / 2, SCREEN_HEIGHT / 2 - 100 / 2, 50 , 100 ,"programador.png", 5)


# Obtenemos los atributos del obj player para utilizalos en nuestro juego
PLAYER_WIDTH = player.width
PLAYER_HEIGHT = player.height
player_vel = player.vel

# Bullet properties
bullet_size = 10
bullet_vel = 10
bullets = []

# Enemy propertiess
easy_enemy_height = 30
easy_enemy_width = 74
enemies = []

#PROBAR APARECER EN ALGUN LUGAR RANDOM 
list_rocks = [
        Rocks("rock.png",40,200,100),
        Rocks("rock.png",40,50,350),
        Rocks("rock.png",40,800,250),
        Rocks("rock.png",40,300,425)]


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
            bullet_x = player.pos_x + PLAYER_WIDTH / 2 - bullet_size / 2
            bullet_y = player.pos_y + PLAYER_HEIGHT / 2 - bullet_size / 2
            
            # Obtenemos la posicion del cursor
            mouse_x, mouse_y = pygame.mouse.get_pos()

            """
            - bullet_x, bullet_Y son en principio la posicion de spawneo 
            - Restamos a la posicion de spawneo de la bala la posicion del mouse al momento del click
            CURSOR POS:  (496, 196)
            PLAYERPOS :  375.0 250.0
            BULLET DIR 101.0 -99.0
            """
            
            # bullet_dir_x y bullet_dir_y son la direccion en la que va la bala
            bullet_dir_x = mouse_x - bullet_x
            bullet_dir_y = mouse_y - bullet_y
            print("CURSOR",mouse_x,mouse_y)
            print("BULLET DIR", bullet_dir_x, bullet_dir_y)
            print("POSICION PLAYER = ", player.pos_x, player.pos_y)
            
            """
            La funcion abs verifica si el número es positivo o cero, entonces el valor absoluto es igual 
            al número original. Si el número es negativo, 
            el valor absoluto es igual al número multiplicado por -1, lo que elimina el signo negativo.
            """
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
    if keys[K_a] and player.pos_x > 0:
        player.pos_x = player.caminar("left",player.pos_x)
        print(player.pos_x)
    if keys[K_d] and player.pos_x < SCREEN_WIDTH - PLAYER_WIDTH:
        player.pos_x = player.caminar("rigth",player.pos_x)
    if keys[K_w] and player.pos_y > 0:
        player.pos_y = player.caminar("up",player.pos_y)
    if keys[K_s] and player.pos_y < SCREEN_HEIGHT - PLAYER_HEIGHT:
        player.pos_y = player.caminar("down",player.pos_y)


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
            enemy.x += player.vel -4
        elif enemy.x > player.pos_x:
            enemy.x -= player.vel -4
        if enemy.y < player.pos_y:
            enemy.y += player.vel -4
        elif enemy.y > player.pos_y:
            enemy.y -= player.vel -4


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
    player_rect = pygame.Rect(player.pos_x, player.pos_y, PLAYER_WIDTH, PLAYER_HEIGHT)
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            running = False  # Game over if player collides with an enemy

    # Generate new enemies
    if len(enemies) < 5:
        create_enemy()
        

    # Draw the game
    screen.fill("WHITE")
    fondo = pygame.image.load("floor.png")
    screen.blit(fondo, (0, 0))
    
    # DIBUJAMOS LAS PIEDRAS

    for rock in list_rocks:
        rock_surface = rock.image
        rock_surface = pygame.transform.scale(rock_surface, (rock.rescale,rock.rescale))
        screen.blit(rock_surface,(rock.pos_x,rock.pos_y))
    

    ## DIBUJAMOS AL PERSONAJE PRINCIPAL
    image =  player.image # Accedemos al atributo imagen 
    image_rect = image.get_rect()   # Obtener el rectángulo de la imagen 
    image_rect.center = (player.pos_x + 50 // 2, player.pos_y + 100 // 2) # Centramos el rectangulo con la posicion de nuestro personaje
    screen.blit(image, image_rect)  


    # DIBUJAMOS LAS BALAS
    for bullet in bullets:
        pygame.draw.rect(screen, (0,255,0), bullet[:2] + (bullet_size, bullet_size))

    # DIBUJAMOS LOS ENEMYGOS
    for enemy in enemies:
        easy_enemy_image = pygame.image.load("sintaxError_image.png")
        screen.blit(easy_enemy_image, enemy)
        


    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
