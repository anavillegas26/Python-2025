import pygame as pg
pg.init()


#color de fondo (variable, globales)
OUTBACK_GROUND= (210,180,140,) # negro
yellow =(255,255,0)# amarillo
light_blue =( 0,179,255) # azul claro
light_blue = (14,255,0) # verde claro

#seteo de la ventana
windows = pg.display.set_mode((800,600)) # tamaño de la ventana
pg.display.set_caption("conseptos basicos")# titulo de la ventana


running = True
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running = False
    windows.fill(background)

    #dibujando Figura

    pg.draw.circle(windows,yellow, (400,300),60)
    pg.draw.rect(windows,(196,138,230),(100,200,200,100))             
    pg.display.update()

pg.quit()