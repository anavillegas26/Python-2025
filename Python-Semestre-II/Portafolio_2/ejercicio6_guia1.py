class Cancion:
    #constructor
    def __init__(self, titulo,artista,duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = int(duracion_segundos)

#metodos de class
    #convertir la duracion a formato minutos a segundos
    def min_seg(self):
        m, s = divmod(max(self.duracion_segundos,0),60) #divmod, divide y obtiene 
       # el resto en formato tupla
        return f"{m}:{s:02d}"
    
    #Metodo magico que muestra la cancion utilizando un print
    def __str__(self):
        return f"{self.titulo} - {self.artista}( {self.min_seg()})"
    
class Playlist:
    #constructor de clase
    def __init__(self,nombre):
        self.nombre = nombre
        self.canciones =[]

    #metodos de  clase
    def agregar(self,cancion): # agregar cacnciones
        self.canciones.append(cancion)

    #duracion total de la playlist
    def duracion_total(self):  
        #iterador for en una linea
        return sum(elemento.duracion_segundos for elemento in self.canciones)
    
    #Muestra la duracion total en mm:ss
    def min_seg_total(self):
        total = self.duracion_total()
        m, s = divmod(max(total,0),60)
        return f"{m}:{s:02d}"
    
    #contar el numero de canciones
    def __len__(self):
        return len(self.canciones)
    
    # Método magico que combina 2 playslist en una nueva playlist
    def __add__(self,otra):
        nueva_playlist= Playlist(f"{self.nombre} + {otra.nombre}")
 
    # guardar las canciones en la playlist combinadas
        nueva_playlist = self.canciones + otra.canciones
        return nueva_playlist
    

    def __str__(self):
        #encabezado a mostrar  de l Playlist
        encabezado_playlist = f"Playlist:{self.nombre}| {len(self.canciones)}| Total :{self.min_seg_total()}"
        # Lanzar mensaje si la lista esta vacia
        if not self.canciones:
            return encabezado_playlist + " \n (vacia)"
        
    # mostar la creacion de formato de impresion de la playlist
        lineas = [encabezado_playlist]

    #creacion de ciclo para mostar el listado de canciones 
        for i, c in enumerate(self.canciones, start=1): # star(recorre las canciones en numerandolas en 1 en lugar de 0
            lineas.append (f"  {i}. {c}")
            return "\n". join(lineas) #convina salto de linea
        
    # instanciar clase creacion de objetos
 #Crear canciones (duración en segundos)
cancion1 = Cancion("The Real Slim Shady", "Eminem", 284)  # 284 seg = 4:44
cancion2 = Cancion("Not Like Us", "Kendrick Lamar", 274)
cancion3 = Cancion("Houdini", "Eminem", 227)
cancion4 = Cancion("Black Summer", "Red Hot Chili Peppers", 232)

# Crear playlist de Hip Hop y agregar canciones
playlist1 = Playlist("Hip Hop")
playlist1.agregar(cancion1)
playlist1.agregar(cancion2)
playlist1.agregar(cancion3)

# Crear playlist de Rock y agregar canción
playlist2 = Playlist("Rockcito")
playlist2.agregar(cancion4)

# Mostrar ambas playlists - con salto de lineas al final para que sea mas bonito :) 
print(playlist1)
print("\n")
print(playlist2)
print("\n")

# Combinar playlists con el operador + (__add__)
playlist3 = playlist1 + playlist2
print("Playlist Combinada:\n", playlist3) 

# Mostrar cantidad de canciones de la playlist combinada
print("\nCantidad de canciones en Playlist Combinada:", len(playlist3))


 
