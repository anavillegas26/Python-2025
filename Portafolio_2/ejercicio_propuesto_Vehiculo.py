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

class Cocesionaria: 

    def __init__(self):
        self.sala_ventas = {} #diccionario para guardar los autos

    def agregar_auto(self, vehiculo): # agrega un objeto (minuscula)vehiculo, que es de la clase Vehiculo
        clave = f"{vehiculo.marca}_{vehiculo.modelo}_{vehiculo.año}"
        self.sala_ventas[clave = vehiculo]
        print (f"Vehiculo agregado a la sala de ventas :{clave})
               

    def mostrar_autos(self):
        for clave, auto in self.sala_ventas.items():
            print(f"{clave}: {auto.marca}, {auto.modelo}, {auto.año}, {auto.color}")

   

    def buscar_libro(self,titulo):
        return self.libros.get(titulo,"libro no encontrado") #get(rerorre el dic{} y busca la claves(1985))
    
    def mostrar_libros(self): 
        for libro in self.libros.values(): #Para(for) buscar libro in (en)mi dic{} libros. values(muestra el
            # valor de mi dicionario)




#Creando objetos de la clase vehiculo
auto1 = Vehiculo("Toyota", "Corolla", 2020,"Verde")
auto2 = Vehiculo("Ford","Mustang", 2021,"Azul")
auto3 = Vehiculo("Honda","Civic", 2019,"Negro")
auto4 = Vehiculo("Peugeot", 5008,2020,"Blanco")

print(f"El Vehiculo numero uno es un {auto1.marca}  {auto1.modelo} del año {auto1.año} y su color es  {auto1.color}")

auto1.arrancar()
auto2.frenado()
auto3.acelerando()

