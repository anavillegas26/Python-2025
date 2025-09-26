class Vehiculo:
    def __init__(self, marca, modelo, año,color):
        self.marca = marca
        self.modelo = modelo
        self.año =int(año)
        self.color = color
        
#metodo de la clase Vehiculo
    def arrancar(self):
        print(f"El  {self.marca}  {self.color}  esta  encendido y a punto arrancar")

    def frenado(self):
        print(f" El {self.marca} {self.color} esta frenando")

    def acelerando(self):
        print(f"El {self.marca} esta comenzando a acelerar") 
#Creando objetos de la clase vehiculo
auto1 = Vehiculo("Toyota", "Corolla", 2020,"Verde")
auto2 = Vehiculo("Ford","Mustang", 2021,"Azul")
auto3 = Vehiculo("Honda","Civic", 2019,"Negro")
auto4 = Vehiculo("Peugeot", 5008,2020,"Blanco")

print(f"El Vehiculo numero uno es un {auto1.marca}  {auto1.modelo} del año {auto1.año} y su color es  {auto1.color}")

auto1.arrancar()
auto2.frenado()
auto3.acelerando()

