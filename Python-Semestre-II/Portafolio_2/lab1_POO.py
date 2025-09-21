class Gato:
    def __init__ (self ,nombre, color, edad, energia,hambre, medicamentos):
#crear contructor que tenga caracteristicas del gato
        self.nombre = nombre
        self.color = color
        self.edad =  int(edad)
        self.energia = int(energia)
        self.hambre = int (hambre)
        self.medicamentos = []

    #crear métodos (caracteristicas del gato)
    def  jugar(self):
       if self.nivel_energia > 30 :
          self.nivel_energia -=10
          self.nivel_hambre += 10
          print(f"el gatito{self.nombre} ha jugado mucho y ahora tiene{self.nivel_energia}")
       else:
           print(f"{self.nombre} esta demaciado cansado para jugar")
    
    
    def comer(self): 
        self.nivel_energia +=30
        self.nivel_hambre = max(0,self.nivel_hambre - 10)
        print(f"{self.nombre} ha sido alimentado y ahora tiene {self.nivel_energia}")

    def gatito_enfermo(self):
        if self.energia <= 0  or self.hambre >= 10:
            print(f" El Gatito {self.nombre} se encuentra enfermo y debe tomar {self.medicamento}")

    def agregar_medicamento(self,medicamento,dosis):
        self.__medicamento.append((medicamento,dosis))
        print(f"Medicamento {medicamento} agregado con dosis {dosis} para {self.nombre}")


    def listar_medicamentos(self):
        return self.__medicamentos

    def __str__(self):
     return f"Gatito: {self.nombre} | Edad:{self.edad} años | Energía: {self.nivel_energia} | Nivel de Hambre:{self.nivel_hambre} \n  "
    
    def __del__(self):
  
        print(f"El Gatito: {self.nombre} salio a la terraza")

class Espacio: #crea el segundo constructor
    def __init__(self, sofa,terraza, ):
        self.sofa = sofa
        self.terraza =terraza
        self.total_gatitos = [] #crea lista para guardar la cantidad de gatitos en el cafe


  # Mëtodos para el espacio del cafe
    def agregar_gatito(self,gatito):
        self.total_gatitos.append(gatito)
        print (f"Gatito {gatito.nombre} a entrado en el café")

#crear el objeto
gatito1 = Gato ("Juanito","negro", 2,10,10,["antibiotico"])
gatito2 = Gato ("Rayita", "blanco", 3,40,30,[])
gatito3 = Gato ("Pedro", "romano" ,2, 80,20,[] )
gatito4 = Gato ("Mañas","naranjo", 5, 50, 70,[])

cafe_gatitos = Espacio(sofa=3, terraza=2)
cafe_gatitos.agregar_gatito(gatito1)
cafe_gatitos.agregar_gatito(gatito2)
cafe_gatitos.agregar_gatito(gatito3)  
cafe_gatitos.agregar_gatito(gatito4)




