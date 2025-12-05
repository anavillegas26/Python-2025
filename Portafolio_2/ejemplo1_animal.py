class Animal():
    #constructor de la clase animal (def__init__)
    #atributos de la clase animal
    def __init__(self, nombre, especie,edad): #  self(parametro especial) hace referencia a si mismo, todos los def van con un tabular dentro de la clase
       self.nombre = nombre     # identar (self permite meterme en la funcines)
       self.especie = especie
       self.edad = edad

#Metodo  de la clase animal(comportamiento)
    def correr(self):
        print(f"{self.nombre} esta corriendo") 

    def dormir(self):
         print(f"{self.nombre} esta durmiendo")

#creando un objeto de la clase animal
gatito = Animal("Michi","Gato",4)
perrito = Animal("Firulais", "Perro",2)
loro =  Animal("Loro Pepito", "Ave",1)

#Impresion de los atributosde los objetos
print(f"El nombre del animal es:{gatito.nombre}")
print(f"La especie del animal es:{gatito.especie}")
print(f"La edad del animal es:{gatito.edad}")

print(f"El nombre del animal es:{perrito.nombre}")
print(f"La especie del animal es:{perrito.especie}")
print(f"La edad del animal es:{perrito.edad}")

#llamada a los métodos de los objetos
gatito.dormir()
perrito.correr()
loro.dormir()