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
        print(f" Los datos ingresados en la ficha son los siguientes\n nombre:{self.nombre}\n, edad:{self.edad}\n, peso:{self.peso}\n, genero{self.genero}")


class Perro (Animal):
     def __init__(self,nombre, edad, peso, genero,raza):
        super().__init__(nombre, edad,peso, genero)
        self.raza = raza

     def ladrar(self):
        print(f"{self.nombre} esta ladrando")

     def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes \n nombre:{self.nombre}\n, edad:{self.edad}\n, peso:{self.peso}\n, genero{self.genero}, raza:{self.raza}")


class Gato (Animal):
     def __init__(self, nombre, edad,peso,genero ,color_pelaje):
        super().__init__(nombre,edad,peso,genero)
        self.color_pelaje =color_pelaje

     def maullar(self):
        print(f" El gato {self.nombre} esta maullando")

     def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes\n nombre:{self.nombre}\n, edad:{self.edad}\n, peso:{self.peso}\n, genero{self.genero}, color del pelaje{self.color_pelaje}")

class Pajaro(Animal):
    def __init__(self, nombre,edad,peso,genero, color_plumaje):
       super().__init__(nombre,edad,peso,genero)
       self.color_plumaje = color_plumaje

    def volar(self):
       print(f"El {self.nombre} esta volando alto")

    def mostrar_ficha(self):
        print(f" Los datos ingresados en la ficha son los siguientes\n nombre:{self.nombre}\n edad:{self.edad}\n peso:{self.peso}\n genero {self.genero}\n color del pelaje {self.color_plumaje}")   


# crear los objetos


pajaro1 = Pajaro("Pepito", 2, 0.3, "Hembra", "Gris")
print(f"✅ Objeto creado: {pajaro1}")
pajaro1.mostrar_ficha()
pajaro1.volar()
pajaro1.comer()
pajaro1.dormir()