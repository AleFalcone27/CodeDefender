# Importamos las bibliotecas 
import pygame

# Importamos modulos propios
from main_char import *
from easy_enemy import easyEnemy

# Creamos las "Constantes" de nuestro programa
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

# JUEGO #
pygame.init() # iniciamos 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # se crea la ventana y sus dimensiones

clock = pygame.time.Clock()

running = True

main_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


while running:
    
    screen.fill("white")# fill the screen with a color to wipe away anything from last frame
    
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT:
            running = False
    
    # PERSONAJE PRINCIPAL #
    
    main_char = MainCharacter("main","programador.png","programadorUP.png",(50, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        main_char.caminar("rigth", main_pos, 8)
        main_char_surface = pygame.image.load(main_char.image)
        
    if keys[pygame.K_LEFT]:
        main_char.caminar("left", main_pos, 8)
        
    if keys[pygame.K_DOWN]:
        main_char.caminar("down", main_pos, 8)
        
    if keys[pygame.K_UP]:
        main_char.caminar("up", main_pos, 8)
        main_char_surface = pygame.image.load(main_char.image_up)
        screen.blit(main_char_surface,(main_pos))
    
    # Creamos la superficie cargando la imagen 
    main_char_surface = pygame.image.load(main_char.image)
    
    # Le damos las medidas a la hitbox
    rect_main_char = pygame.Rect((main_pos), main_char.hit_box)
    
    # Creamos el rectangulo
    pygame.draw.rect(screen,(0, 0, 0), rect_main_char)
    
    # Lo printeamos en la pantalla
    screen.blit(main_char_surface,(main_pos))
    
    # Limitamos el movimiento del personaje principal a las medidas de nuestra screen
    if rect_main_char.bottom > 720:
        main_pos.y = 618
    if rect_main_char.top < 0:
        main_pos.y = 1
    if rect_main_char.right > 1280:
        main_pos.x = 1230
    if rect_main_char.left < 0:
        main_pos.x = 1
    
    

    
    
    
    
    
    
    
    # ENEMIGO #
    
    
    easy_enemy_list = easyEnemy.easy_enemy_create_list(10)
    
    a = easyEnemy()
    
    a.easy_enemy_update(screen,easy_enemy_list)


    # if rect_main_char.colliderect():
    #     print("El jugador colisiona con el enemigo")

            
    # Creamos la superficie cargando la imagen 
    # easy_enemy_surface = pygame.image.load(easy_enemy.image_1)
    
    # le damos las medidas a la hit box
    # rect_easy_enemy = pygame.Rect((100,100),easy_enemy.hit_box)

    # dibujamos la hitbox
    # pygame.draw.rect(screen,(255, 0, 0), rect_easy_enemy)
    
    ## Aca tengo el colisionador 
    
    
    
    # screen.blit(easy_enemy_surface,(easy_enemy.spawn_cor))

    #easy_enemy__pos.x = main_pos.x IDEA PARA SEGUIR AL MAIN CHAR


    
        
        # main_char.image = "programadorUP.png"
        # main_char_surface = pygame.image.load(main_char.image)
        # screen.blit(main_char_surface,(main_pos))
        
        # print(main_char.image)
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



Tenemos que crear constructores para todos 
- Personaje
- enemigos 
power ups y cada uno va a tener sus atributos y metodos

Tenemos que crear una rectangulo para el personaje y para los enemigos y power ups
"""