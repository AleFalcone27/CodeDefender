import pygame
from main_char import *

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
    
    
    main_char = MainCharacter("main","programador.png")
    
    # Creamos la superficie cargando la imagen 
    main_char_surface = pygame.image.load(main_char.image_1)
    
    # Reescalamos la imagen
    # main_char_scaled = pygame.transform.scale(main_char_surface,main_char.scale)
    
    # Le damos las medidas a la hitbow
    rectangulo = pygame.Rect((main_pos), (50, 100))
    
    # Creamos el rectangulo
    rect_main = main_char_surface.get_rect()
    pygame.draw.rect(screen,(255, 0, 0), rectangulo)
    
    # Lo printeamos en la pantalla
    screen.blit(main_char_surface,(main_pos))
    
    
    #Tengo que crear el movimiento por el objeto lo que no se como carajos hacer
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        main_pos.x += 5
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