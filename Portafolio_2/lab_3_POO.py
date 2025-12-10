
from abc import ABC, abstractmethod

class StreamPy(ABC):
    def __init__(self,titulo, año=int):
        self.titulo = titulo
        self.año = año
        
    @abstractmethod
    def mostrar_detalle(self):
        """Tienen diferente titulo y año"""
        pass 

class Reproducible(ABC):
    """ Se puede reproducir en minutos"""
    
    @abstractmethod
    def reproducir(self):
        """se puede reproducir"""
        

class Calificable(ABC):
    def __init__(self, rating=float):
        self.rating = rating


class Pelicula(StreamPy, Reproducible):
    def  __init__(self, titulo, año=int, duracion_minutos=int):
        self.duracion_minutos = duracion_minutos
        super().__init__(titulo, año)
    
     
    def reproducir_contenido(self):
        print (f"La pelicula : {self.nombre} se esta reproduciendo")

    def mostrar_detalle(self):
        print (f"La pelicula {self.nombre} tiene solo  1 hora de duracion")
    

class Documentales(StreamPy):
    def __init__(self, titulo, año=int, tema=str):
        self.tema = tema
        super().__init__(titulo, año)
    

    def reproducir_contenido(self):
        print(f" El documental:{self.nombre} se esta reproduciendo")

    def mostrar_detalle(self):
        print (f"El documental {self.nombre} tiene 2 horas  de duracion")
    
    

class MiniSerie(StreamPy,Reproducible,Calificable):
    def __init__(self, titulo, año=int, num_episodios=int):
        self.num_episodios = num_episodios
        super().__init__(titulo, año)

    def reproducir_contenido(self):
        print(f" La MiniSerie: {self.nombre} se esta reproduciendo")

    def mostrar_detalle(self):
        print (f"La Miniserie {self.nombre} tiene solo 5 capitulos ")


def lista_reproduccion (reproducir):
        return reproducir

series=[
         Pelicula ("El Rey Arturo", 2025,1.30),
         Documentales("La Vida en la Tierra",2000, "Medio Ambiente"),
         MiniSerie("It",2025,5)
        ]

lista_reproduccion.mostrar_detalle


    series.mostrar_detalle()