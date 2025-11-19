class Vehiculo_Terrestre:
   def __init__(self,año=int,marca=str, color=str,bencina=int):
      self.año = año
      self.marca = marca 
      self.color = color
      self.bencina = bencina

   def mover(self):
      print(f"Los vehiculos terrestres estan recorriendo la carretera")


class Vehiculo_Acuatico: 
   def __init__(self,año=int,marca=str, color=str,petróleo=int):
      self.año = año
      self.marca = marca 
      self.color = color
      self.petróleo = petróleo

   def mover(self):
      print(f"Los vehiculos del agua estan navegando")

class Vehiculo_Aereo: 
   def __init__(self,año=int,marca=str, color=str,gas=int):
      self.año = año
      self.marca = marca
      self.color = color
      self.gas = gas

   def mover(self):
      print(f"Los vehiculos aereos estan volando")


class Auto(Vehiculo_Terrestre):
    def __init__(self,año=int,marca=str,color=str,bencina=int,asiento_cuero=True):
       super().__init__(año,marca,color,bencina)
       self.asiento_cuero = asiento_cuero

    

class Camioneta(Vehiculo_Terrestre):
     def __init__(self, año=int, marca=str, color=str,bencina=int,pickup=bool):
        super().__init__(año, marca, color,bencina)
        self.pickup = pickup


class Lancha(Vehiculo_Acuatico):
    def __init__ (self,año=int,marca=str,color=str, petróleo =int,nombre=str):
       super().__init__(año,marca,color,petróleo)
       self.nombre = nombre

class Velero(Vehiculo_Acuatico):
    def __init__(self, año=int, marca=str, color=str,petróleo=int,velas=int):
       super().__init__(año, marca, color,petróleo)
       self.velas = velas

   
   
class Avioneta(Vehiculo_Aereo):
    def __init__(self, año= int, marca=str, color=str,gas=int,hélices=bool):
       super().__init__(año, marca, color,gas)
       self.hélices = hélices

class Helicoptero(Vehiculo_Aereo):
    def __init__(self, año=int, marca=str, color=str,gas=int,tren_aterrizaje=bool ):
       super().__init__(año, marca, color,gas)
       self.tren_aterrizaje = tren_aterrizaje
   
    

class Hidroavion(Vehiculo_Acuatico,Vehiculo_Aereo):
    def __init__(self,año=int,marca=str,color=str,petróleo=int,gas=int, turbinas=bool):
       super().__init__(año,marca,color,petróleo,gas)
       self.turbinas = turbinas
    

class Vehiculo_anfibio(Vehiculo_Acuatico,Vehiculo_Terrestre):
    def __init__ (self,año,marca,color,petróleo,gas, snorkel=bool):
       super().__init__(año,marca,color,petróleo,gas)
       self.snorkel = snorkel
   


   #instanciar los vehiculos 

carrera =[
   Hidroavion(2005,"SAPITO","verde", 2000,3000,True),
   Auto( 2016,"PEUGEOT","blanco",2500,True),
   Helicoptero(2026,"Alitas", "Amarillo",4000,True)
]
      
for vehiculo in carrera:
    print(vehiculo)
    vehiculo.mover()

