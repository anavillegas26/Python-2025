class Gato:
    def __init__(self, nombre, color, edad, energia, hambre, medicamentos):
        self.nombre = nombre
        self.color = color
        self.edad = int(edad)
        self.energia = int(energia)
        self.hambre = int(hambre)
        self.__medicamentos = medicamentos # atributo privado para los medicamentos del gatito

    def jugar(self):           # Método para simular que el gatito juega y si aumenta o diminuye su energia  o hambre)
        if self.energia > 30:  # si la energia es mayor a 30
            self.energia -= 10 # resta 10 de energia
            self.hambre += 10  # aumenta el hambre
            print(f"El gatito {self.nombre} ha jugado mucho y ahora tiene {self.energia} de energía.")
        else:
            print(f"{self.nombre} está demasiado cansado para jugar.")

    def comer(self):       # Método simula que el gatito come y si aumenta o dismunuye la enegia y el hambre
        self.energia += 30  # si come aumenta 30 de enegia 
        self.hambre = max(0, self.hambre - 10) # disminuye el hambre ( sin llegar a 0)
        print(f"{self.nombre} ha sido alimentado y ahora tiene {self.energia} de energía.")

    def gatito_enfermo(self): # Método para simular al gatito enfermo 
        if self.energia <= 0 or self.hambre >= 80: #si disminuye  la energia y el hambre mayor 100
            print(f"El gatito {self.nombre} se encuentra enfermo y debe tomar sus medicamentos: {self.__medicamentos}")

    def agregar_medicamento(self, medicamento, dosis): # Método para agregar el medicamento y la dosis
        self.__medicamentos.append((medicamento, dosis)) # se agregara a la lista vacia
        print(f"Medicamento {medicamento} agregado con dosis {dosis} para {self.nombre}")

    def listar_medicamentos(self): # muestra los medicamentos que hay disponible
        return self.__medicamentos

    def __str__(self): # muestra las caracteristicas del gatito
        return f"Gatito: {self.nombre} | Edad: {self.edad} años | Energía: {self.energia} | Hambre: {self.hambre}"

    def __del__(self): # borra gatito
        print(f"El Gatito: {self.nombre} salió a la terraza")

class Espacio:
    def __init__(self, sofa, terraza):
        self.sofa = sofa
        self.terraza = terraza
        self.total_gatitos = []  # lista vacia para poder agregar a los gatitos

    def agregar_gatito(self, gatito): # agrega gatitos a al Espacio
        self.total_gatitos.append(gatito) # cuenta los gatitos que hay en el espacio
        print(f"Gatito {gatito.nombre} agregado al café.")

# Crear objetos
gatito1 = Gato("Juanito", "negro", 2, 50, 70, []) # nombre, color, edad, energia, hambre, lista vacias para los medicamentos
gatito2 = Gato("Rayita", "blanco", 3, 40, 30, [])
gatito3 = Gato("Pedro", "romano", 2, 0, 80, [])  

cafe_gatitos = Espacio(sofa=3, terraza=2)
cafe_gatitos.agregar_gatito(gatito1)
cafe_gatitos.agregar_gatito(gatito2)
cafe_gatitos.agregar_gatito(gatito3)

gatito1.jugar()
gatito2.comer()
gatito3.gatito_enfermo()
gatito3.agregar_medicamento("Antibiotico","5mg")
gatito3.listar_medicamentos()

gatito1.__str__()
gatito2.__str__()
gatito3.__str__()