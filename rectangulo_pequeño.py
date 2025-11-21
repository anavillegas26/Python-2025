import pygame as pg

class RectanguloPequeño:
    def __init__(self, x,y ,ancho,alto):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = (39,245,224) # color normal
        self.velocidad = 1
        self.rect = pg.Rect(self.x,self.y,self.ancho,self.alto)
    
    def dibujar (self,ventana):
        pg.draw.rect(ventana,self.color, self.rect)


    
    def mover(self,teclas):
        mov_x = 0
        mov_y = 0

        if teclas [pg.K_DOWN]:
            mov_x = -1
        if teclas[pg.K_UP]:
            mov_x = 1
        if teclas[pg.K_LEFT]:
            mov_y = -1
        if teclas[pg.K_RIGHT]:
            mov_y = 1
 
        self.rect.x += mov_x * self.velocidad
        self.rect.y += mov_y * self.velocidad
    
    def restablecer_posicion(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def cambiar_color(self,color):
        self.color = color

    def obtener_posicion(self):
        return (self.rect.x, self.rect.y)

    
