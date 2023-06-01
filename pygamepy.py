import pygame
import random
from main_char import *
from enemy_1 import *

# pygame setup
pygame.init() # iniciamos 

screen = pygame.display.set_mode((1280, 720)) # se crea la ventana y sus dimensiones

clock = pygame.time.Clock()

running = True

main_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


while running:
    
    screen.fill("white")# fill the screen with a color to wipe away anything from last frame
    
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False
    
    
    
    # PERSONAJE PRINCIPAL #
    
    main_char = MainCharacter("main","programador.png",(50, 100))
    
    # Creamos la superficie cargando la imagen 
    main_char_surface = pygame.image.load(main_char.image_1)
    
    # Le damos las medidas a la hitbox
    rect_main_char = pygame.Rect((main_pos), main_char.hit_box)
    
    # Creamos el rectangulo
    pygame.draw.rect(screen,(255, 0, 0), rect_main_char)
    
    # Lo printeamos en la pantalla
    screen.blit(main_char_surface,(main_pos))
    
    # ENEMIGO #
    ## ES POR ACA ->
    easy_enemy = enemy_1("enemy_1","easy_enemy.png",(33, 50),((random.randint(0,1280),random.randint(0,720))))
    
    # Creamos la superficie cargando la imagen 
    easy_enemy_surface = pygame.image.load(easy_enemy.image_1)
    
    # le damos las medidas a la hit box
    rect_easy_enemy = pygame.Rect(easy_enemy.spawn_cor, easy_enemy.hit_box)
    
    # dibujamos la hitbox
    pygame.draw.rect(screen,(255, 0, 0), rect_easy_enemy)
    # rectangulo = pygame.Rect((main_pos), (50, 100))
    
    
    ## Aca tengo el colisionador 
    if rect_main_char.colliderect(rect_easy_enemy):
        print("El jugador colisiona con el enemigo")
    
    
    
    
    screen.blit(easy_enemy_surface,(easy_enemy.spawn_cor))
    
    
    #Tengo que crear el movimiento por el objeto lo que no se como carajos hacer
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        main_pos.x += 5
        
        #easy_enemy__pos.x = main_pos.x IDEA PARA SEGUIR AL MAIN CHAR
        
        
        
        # main_char.move("rigth")

    if keys[pygame.K_LEFT]:
        main_pos.x -= 5
        # main_char.move("left")
        
    if keys[pygame.K_DOWN]:
        main_pos.y += 5
        # main_char.move("down")
        
    if keys[pygame.K_UP]:
        main_pos.y -= 5
        # main_char.move("up")

    # print(main_pos.x)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(80) / 1000

        
    
    
pygame.quit()



"""
    
# if evento.type == pygame.MOUSSEMOTION:

#     posicion_circulo = evento.pos


para poder fijar eventos que ocurran por tiempo

tick = pygame.USEREVENT + 0



"""


"""
Hacer archivos diferentes por cada uno de los elementos de nuestro juego 

crear constantes para el ancho y largo de la pantalla

-- caida de las doonas --
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,1000)

def crear_lista_donas(cantidad)
for i in range(cantidad):
    y = random,randrange(randogo,rango)
    x = random,randrange(randogo,rango)
    lista_donas.append(crear(x,y,60,60))
    
return lita_donas

Tenemos que crear constructores para todos 
- Personaje
- enemigos 
power ups y cada uno va a tener sus atributos y metodos

Tenemos que crear una rectangulo para el personaje y para los enemigos y power ups
"""