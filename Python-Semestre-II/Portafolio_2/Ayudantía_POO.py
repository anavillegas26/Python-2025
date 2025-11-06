#crea una clase llamada Playlist
class Playlist:
    total_playlist = 0

    def __init__(self, usuario:str)-> str:
        self.usurario = usuario
        self.__canciones = []
        Playlist.total_playlist += 1
        
    def agregar_cancion(self,nombre:str) -> None:
        if nombre.strip() == "": #verifica no vacio
            return
    # verificar que no este repetida
        if nombre not in self.__canciones: # verifica no repetido
            self.__canciones.append(nombre) #  append agrega


    def eliminar_canciones(self, nombre:str) -> None:
        if nombre in self.__canciones:
            self.__canciones.remove(nombre)

    def __len__(self)-> int:
        return len(self.__canciones)
    
    def __str__(self)-> str:
        return f"Playlist de {self.usurario}:{len(self)} canciones"
    
    #instanciar objetos( crear las lista)

playlist1 = Playlist("Leo")
playlist2 = Playlist("Anita")

print(f"total de playlist:{Playlist.total_playlist}")

#agregar canciones
playlist1.agregar_cancion(" La mesa del rincón")
playlist1.agregar_cancion("Las flores de tu florero")
playlist1.agregar_cancion("")
playlist1.agregar_cancion("La mesa del rincón")

print(playlist1)
print(len(playlist1))

# eliminar cancion
playlist1.eliminar_canciones("La mesa del rincón")
print(playlist1)