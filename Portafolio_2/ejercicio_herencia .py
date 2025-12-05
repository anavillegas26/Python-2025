class Animal:
     def __init__(self,nombre,edad,peso, genero):
       self.nombre = nombre
       self.edad = edad
       self.peso = peso
       self.genero = genero

     def comer(self):
      print (f"{self.nombre} esta comiendo")

     def dormir(self):
        print(f"{self.nombre} esta durmiendo")

     def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes:\n nombre:{self.nombre}\n edad:{self.edad}\n peso:{self.peso}\n genero{self.genero}")


class Perro (Animal):
     def __init__(self,nombre, edad, peso, genero,raza):
        super().__init__(nombre, edad,peso, genero)
        self.raza = raza

     def hacer_sonido(self):
        print(f"{self.nombre} esta ladrando")

     def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes \n nombre:{self.nombre}\n edad:{self.edad}\n peso:{self.peso}\n genero{self.genero} raza:{self.raza}")


class Gato (Animal):
     def __init__(self, nombre, edad,peso,genero ,color_pelaje):
        super().__init__(nombre,edad,peso,genero)
        self.color_pelaje =color_pelaje

     def hacer_sonido(self):
        print(f" El gato {self.nombre} esta maullando")

     def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes\n nombre:{self.nombre}\n edad:{self.edad} años\n peso:{self.peso} Kg\n genero{self.genero} color del pelaje{self.color_pelaje}")

class Pajaro(Animal):
    def __init__(self, nombre,edad,peso,genero, color_plumaje):
       super().__init__(nombre,edad,peso,genero)
       self.color_plumaje = color_plumaje

    def hacer_sonido(self):
       print(f"El {self.nombre} esta volando alto")

    def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes\n nombre:{self.nombre}\n edad:{self.edad} años\n peso:{self.peso} Kg\n genero {self.genero}\n color del pelaje {self.color_plumaje}")   

class Puma(Animal):
    def __init__(self,nombre,edad,peso,genero,estado_natural):
       super().__init__(nombre,edad,peso,genero)
       self.estado_natural = estado_natural

    def hacer_sonido(self):
       print(f"El Puma {self.nombre} esta gruñendo")

    def mostrar_ficha(self):
        print(f"Los datos ingresados son los siguientes:")
        print(f"nombre:{self.nombre}")
        print(f"edad:{self.edad} años")
        print(f"peso: {self.peso} Kg")
        print(f"genero: {self.genero}")
        print(f"Estado Natural: {self.estado_natural}")
   

# crear los objetos en una lista

zoologico =[
  Perro("Cholito",5 ,12,"Macho","Labrador"),
  Gato("Bikini",8,3, "Macho","Naranja"),
  Pajaro("Pepito",2,2,"Macho","Verde"),
  Puma("Julieta",2,30,"Hembra","Café")
]

#Bucle polimorfico
for animal in zoologico:
   print(f"\n Ficha de {animal.nombre}")
   animal.mostrar_ficha()
   animal.hacer_sonido()
   