import pygame 

from rectangulo_pequeño import RectanguloPequeño
from rectangulo_grande import RectanguloGrande

pygame.init()

ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Colisión Rectangular en Pygame")

background = (0,0,0,)
color_colision = (234,63,63) # rojo

# instacias de los rectangulos
rectangulo_pequeño = RectanguloPequeño(200,200,100,50)
rectangulo_grande = RectanguloGrande(400,300,150,100)

runnig = True
while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False

    teclas = pygame.key.get_pressed ()

    # almacena la posicion actual de los rectangulos antes de moverlos
    pos_anterior_pequeño = rectangulo_pequeño.obtener_posicion()
    pos_anterior_grande = rectangulo_grande.obtener_posicion()

    # movimientos los rectangulos
    rectangulo_pequeño.mover(teclas)
    rectangulo_grande.mover(teclas)

       #verificar colision rectagular
    if rectangulo_pequeño.rect.colliderect(rectangulo_grande.rect):
        #si existe colision, se reestableceran las posiciones anteriores
       rectangulo_pequeño.restablecer_posicion(*pos_anterior_pequeño)    
       rectangulo_grande.restablecer_posicion(*pos_anterior_grande)   
       rectangulo_pequeño.cambiar_color(color_colision)   
       rectangulo_grande.cambiar_color(color_colision) 
    else:
        #restablecer colores normales
        rectangulo_pequeño.cambiar_color((63,232,234))  
        rectangulo_grande.cambiar_color((63,234,76))  

    ventana.fill(background)  
    rectangulo_pequeño.dibujar(ventana)  
    rectangulo_grande.dibujar(ventana) 

    pygame.display.update() 
pygame.quit()       