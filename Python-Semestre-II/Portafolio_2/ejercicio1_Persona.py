# GUIA RÁPIDA DE CLASES EN PYTHON
# Docente: Victor Saldivia Vera - Institución: Universidad de Los Lagos

class Persona():
    
    # Constructor de Clase
    def __init__(self, nombre, apellido, edad, altura,peso,nota1,nota2,nota3): # este método se ejecuta automáticamente al crear un nuevo objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)
        self.nota1 = float(nota1)
        self.nota2 = float(nota2)
        self.nota3 = float(nota3)
    # Atributos (Características compartidas por todos los objetos de la clase)
    # nombre = "Cristina"
    # apellido = "Torres"
    # edad = 23
    
    # Métodos (Comportamientos)
    
    def hablar(self):
        print(f"{self.nombre} esta hablando")
        
    def caminar(self):
        print(f"{self.nombre} esta caminando")

    
        
    def calcular_imc(self): 
        imc = (self.peso / (self.altura**2))
    
        if imc < 18:
            print(f" Según su imc se encuentra muy flaquito.")
        elif imc >= 18 and imc < 25:
            print(f" Según su imc se encuentra con un peso normal y dentro del rango saludable.")    
        elif imc >=25 and imc <29:
            print(f"Según su imc esta comiemdo mucho y esta muy gordito")
        else:
            print("Según su imc usted se  encuentra como bolita")

    def promedio_asignatura(self):
        promedio = (self.nota1 + self.nota2 +self.nota3) /3

        if promedio >=40:
            print(f"{self.nombre} tiene{promedio}, por lo tanto aprueba la asignatura")
        else:
            print(f"{self.nombre}: tiene {promedio} por lo tanto NO aprueba la asignatura")
        

persona1 = Persona("Cristina","Torres",23,1.70, 40.5,4.0,5.0,6.0) # instancia de la clase Persona -> crear un objeto de la clase Personapersona2 = Persona("Benjamin", "Gomez", 20,1.80, 100 )
persona2 = Persona("Benjamín","Gomez",20,1.80, 100,4.5,3.0,2.0 )

print(f"{persona1.nombre}")
print(f"{persona1.apellido}")
print(f"{persona1.edad}")

print(f"{persona2.nombre}")
print(f"{persona2.apellido}")
print(f"{persona2.edad}")

persona1.hablar() # equivalente a Persona.hablar(persona1)
persona2.caminar() # se puede crear múltiples objetos de la misma clase

persona1.calcular_imc()
persona2.calcular_imc()
persona1.promedio_asignatura()
