import pygame
import random
from player import MainChar
from rock_element import Rocks
from pygame.locals import *
from bullets import move_bullet,remove_bullet_off_screen,remove_bullet_when_hit_enemy,bullet_colision
from features import draw_score,start_game,end_game
from Levels.LVL1 import *

# INICIALIZAMOS PYGAME
pygame.init()

# PANTALLA
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Code Defenderdd")

# CREAMOS UNA INSTACIA DE LA CLASE MAINCHAR
player = MainChar(SCREEN_WIDTH / 2 - 50 / 2, SCREEN_HEIGHT / 2 - 100 / 2, 50, 100, "Images\programador.png", 5)


# BULLET
bullet_size = 10
bullet_vel = 10
bullets = []

# ENEMY
easy_enemy_height = 30
easy_enemy_width = 74
enemies = []
enemy_vel = 1

# SOUNDS
shot_sound = pygame.mixer.Sound("Sounds\shootSound.wav")
lose_sound = pygame.mixer.Sound("Sounds\loseSound.wav")
main_theme = pygame.mixer.Sound("Sounds\main_theme.mp3")
shot_sound.set_volume(0.1)  # Establece el volumen del sonido de disparo al 50%
main_theme.play()
main_theme.set_volume(0.05)

# PAUSA
pause = False
flag_pause = True
pause_start_time = 0
paused_time = 0
total_paused_time = 0
flag2 = False

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

# SCORE
score = 0

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

flag_start = False

# GAME LOOP
running = True
clock = pygame.time.Clock()
while running:
    while flag_start == False:
        intro = pygame.image.load("Images\intro.png")
        screen.blit(intro, (0,0))
        pygame.display.flip()
        flag_start = start_game()

    current_time = pygame.time.get_ticks() /1000
    current_time = int(current_time)        
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if not pause:
                shot_sound.play()
                bullet_x = player.pos_x + player.width / 2 - bullet_size / 2
                bullet_y = player.pos_y + player.height / 2 - bullet_size / 2
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

    if pause:
        if flag_pause == True:
            pause_start_time = pygame.time.get_ticks() /1000 # ME QUEDOa CON EL TICK EN EL CUAL SE INGRESA A LA PAUSA
            pause_start_time = int(pause_start_time)
            flag_pause = False
        paused_time = pygame.time.get_ticks() /1000  # ME QUEDO CON EL TICK EN EL CUAL SE SALE DE LA PAUSA
        paused_time = int(paused_time)
        flag2 = True

        font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 60)
        pause_text = font.render("PAUSE"  , True, "BLACK")
        screen.blit(pause_text, (450, 270))     

        pygame.display.flip()
        
    # VERIFICAMOS LA PAUSA
    if not pause:
        if flag2 == True:
            pause_time = pygame.time.get_ticks() / 1000 # ME QUEDO CON EL PRIMER SEGUNDO 
            pause_time = int(pause_time)
            total_paused_time_actual = paused_time - pause_start_time  # RESTAMOS EL TICK EN EL CUAL SE SALIO DE LA PAUSA AL TICK EN EL CUAL SE INGRESO
            total_paused_time = total_paused_time + total_paused_time_actual # ACUMULAMOS EL TIEMPO TOTAL DE PAUSA PARA RESTARSELO AL CRONOMETRO MAIN
            elapsed_time = pause_time - total_paused_time # RESTAMOS EL TOTAL DEL TIEMPO DE PAUSA AL RELOJ MAIN
            flag2 = False
        
        # MOVIMIENTO DEL JUGADOR
        keys = pygame.key.get_pressed()
        if keys[K_a] and player.pos_x > 0:
            player.pos_x = player.caminar("left", player.pos_x)
        if keys[K_d] and player.pos_x < SCREEN_WIDTH - player.width:
            player.pos_x = player.caminar("rigth", player.pos_x)
        if keys[K_w] and player.pos_y > 0:
            player.pos_y = player.caminar("up", player.pos_y)
        if keys[K_s] and player.pos_y < SCREEN_HEIGHT - player.height:
            player.pos_y = player.caminar("down", player.pos_y)
        # Creamos el reactangulo del jugador
        player_rect = player.get_rect(player.pos_x,player.pos_y)


        # ------ LOGICA DE LAS BALAS -----
        # eliminamos las balas que se sale de la pantalla 
        bullets_to_remove =  move_bullet(bullets,bullet_vel)
        remove_bullet_off_screen(bullets_to_remove,bullets)
        # Verifica la colision de las balas con los enemigos y elimina a ambos en caso de colision
        if(bullet_colision(bullets_to_remove,bullets,enemies,bullet_size)):
            remove_bullet_when_hit_enemy(bullets_to_remove,bullets)
            score = score + 1


        # Move the enemies
        for enemy in enemies:
            if enemy.x < player.pos_x:
                enemy.x += enemy_vel
            elif enemy.x > player.pos_x:
                enemy.x -= enemy_vel
            if enemy.y < player.pos_y:
                enemy.y += enemy_vel
            elif enemy.y > player.pos_y:
                enemy.y -= enemy_vel
        
        
        # ----- NIVELES ------
        if score == 0:
            tutorial(enemies,create_enemy)
            
        if score >= 1 and score < 15: # Se generan 15 enemigos
            lvl_1(enemies,create_enemy,list_rocks,screen)
            enemy_vel = 1.2

        if score >= 19 and score < 25: # se generan 20 enemigos
            lvl_2(enemies,create_enemy,list_rocks)
            enemy_vel = 1.2
            
        if score >= 34 and score < 44:
            lvl_3(enemies,create_enemy,list_rocks)
            enemy_vel = 1.5
            
        if score >= 58 and score < 68:
            lvl_4(enemies,create_enemy,list)
            enemi_vel = 1.7
            
        
    # DIBUJAMOS FONDO
        fondo = pygame.image.load("Images\\floor.png")
        screen.blit(fondo, (0, 0))
        
        #DIBUJAMOS EL SCORE
        round(score,screen)
        
        
        # DIBUJAMOS LAS PIEDRAS
        for rock in list_rocks:
            rock_rect = rock.draw_rocks(list_rocks,screen)
            
            # VEIRICAMOS COLISION CON EL JUGADOR
            if player_rect.colliderect(rock_rect):
                if player.pos_y > rock.pos_y:
                    player.pos_y += player.vel
                if player.pos_y < rock.pos_y:
                    player.pos_y -= player.vel
                if player.pos_x < rock.pos_x:
                    player.pos_x -= player.vel
                if player.pos_x > rock.pos_x:
                    player.pos_x += player.vel


         # ----- ENEMIGOS ------
        for enemy in enemies:
            if player_rect.colliderect(enemy):
                while True:
                    running = end_game(screen)  # Game over if player collides with an enemy

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
        draw_score(score,screen)

        # DIBUJAMOS CRONOMETRO
        elapsed_time = current_time - total_paused_time
        font = pygame.font.SysFont("microsoftjhengheimicrosoftjhengheiui", 30)
        elapsed_time = int(elapsed_time)
        elapsed_time_text = font.render("Time: " + str(elapsed_time ) , True, "BLACK")
        flag_pause = True
        
        screen.blit(elapsed_time_text, (10, 40))        
        
        pygame.font.get_fonts()
        pygame.display.flip()
        # Control the frame rate

        clock.tick(60)
        
# Qit the game
pygame.quit()


# Reloj 10
#