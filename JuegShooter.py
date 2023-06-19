import pygame
import random
from player import MainChar
from rock_element import Rocks

from pygame.locals import *

from bullets import move_bullet,remove_bullet_off_screen,remove_bullet_when_hit_enemy,bullet_colision

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


score = 0

# SOUNDS
shot_sound = pygame.mixer.Sound("Sounds\shootSound.wav")
lose_sound = pygame.mixer.Sound("Sounds\loseSound.wav")
shot_sound.set_volume(0.1)  # Establece el volumen del sonido de disparo al 50%


# PAUSA
pause = False
flag_pause = True
pause_start_time = 0
paused_time = 0

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


flag2 = False

# GAME LOOP
running = True
clock = pygame.time.Clock()

total_paused_time = 0

# CUANDO APRETE LA PAUSA EL PERSONAJE NO SE PUEDA NI MOVER NI APRETAR EL BOTON
# CUANDOE STOY EN PAUSA NO SE LEAN LOS INPUTS DEL USUARIO
# cUANDO ESTOY EN PAUSA NO SE LEAN LOS EVENTOS QUE NO SEAN CERRAR EL JUEGO

while running:
    current_time = pygame.time.get_ticks() /1000
    current_time = int(current_time)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if not pause:
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
                
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pause = not pause




# EL TIEMPO DE PAUSA SE SUMA EN LA PROXIMA 

    if pause:
        
        if flag_pause == True:
            pause_start_time = pygame.time.get_ticks() /1000 # Guardo el el segundo en el cual el juego se pone en pausa
            pause_start_time = int(pause_start_time)
            print("PRIMER SEGUNDO DE PAUSA: ",pause_start_time)
            flag_pause = False
        paused_time = pygame.time.get_ticks() /1000  # Me quedo con el segundo en el cual el juego sale de la pausa
        paused_time = int(paused_time)
        flag2 = True
        
        print(paused_time)
        
        
    # VERIFICAMOS LA PAUSA
    if not pause:
    
        # DIBUJAMOS EL CRONOMETRO
    
        if flag2 == True:
            
            primertikbandera = pygame.time.get_ticks() /1000
            primertikbandera = int(primertikbandera)
            total_paused_time_actual = paused_time - pause_start_time  # 5
            total_paused_time =  total_paused_time + total_paused_time_actual # 0 + 5
            elapsed_time =  primertikbandera - total_paused_time # 10 - 5
            flag2 = False
        
        
        elapsed_time = current_time - total_paused_time
        font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
        elapsed_time = int(elapsed_time)
        elapsed_time_text = font.render("Time: " + str(elapsed_time ) , True, "BLACK")
        
        
        print("A",total_paused_time)
        flag_pause = True
        
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


        # LOGICA DE LAS BALAS 
        # Remove bullets that have gone off-screen
        bullets_to_remove =  move_bullet(bullets,bullet_vel)
        remove_bullet_off_screen(bullets_to_remove,bullets)
        # Verifica la colision de las balas con los enemigos y elimina a ambos en caso de colision
        if(bullet_colision(bullets_to_remove,bullets,enemies,bullet_size)):
            remove_bullet_when_hit_enemy(bullets_to_remove,bullets)
            score = score + 1



        # PLAYER
        # Creamos el reactangulo del jugador
        player_rect = player.get_rect(player.pos_x,player.pos_y)


        for enemy in enemies:
            if player_rect.colliderect(enemy):
                running = False  # Game over if player collides with an enemy
        
        
        # ENEMY
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
        
        # Generate new enemies
        # if len(enemies) < 5:
            # create_enemy()
            
            
        # DRAW STUFF
            
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
        
        screen.blit(elapsed_time_text, (10, 40))
    

        
        
        pygame.font.get_fonts()
        pygame.display.flip()
        # Control the frame rate

        clock.tick(60)
        
# Qit the game
pygame.quit()


# Reloj 10
#