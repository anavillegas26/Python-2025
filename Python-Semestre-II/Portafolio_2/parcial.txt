class Jugador:
       
       JUGADORES_CREADOS = 0  # contador global

       def __init__(self, nombre:str,edad :int,posicion,club:str, goles, club,energia= [0,100], ):
         self.__nombre = nombre
         self.__edad = edad >= 0
         self.__posicion = posicion ["DEL","VOL","DEF","ARQ"]
         self.goles = 0 
         self.club = club 
         self.energia = energia 

         self.posicion = posicion_valida = True
     
         
        
         assert = 
         
         JUGADORES_CREADOS += 1


       def entrenar(self):       
        self.energia += 30  
        self.entrenar = max(0, self - 10) 
        print(f"{self.nombre} ha entrenado" )

        def listar_goles(self.goles)
        return self.__goles
        # getter y setter
        
        @property
        def setnombre(self):
          return self.__nombre
    

        @property
        def setedad(self):
           return self.__edad
        
        @property

        def  posicion(self):
            return self.__posicion

 
       def anotar(self):
           
       # metodo magico

        def __str__(self)-> str:
         return f"El jugador {self.nombre}, esta jugando para el Club{self.club} y juega en la posición {self.__posicion},y tiene enegía {self.energia} por anotar {self.goles}  goles"

       # variables de clase
        @classmethod
        def  creados(csl) :
           return   creados
       


jugador1 = Jugador("Juan Martine", 18, "DEL", "Deportes Castro", 30)
jugador2 = Jugador("Leonardo",20,"DEF"," Deportes Castro"40)

                   




