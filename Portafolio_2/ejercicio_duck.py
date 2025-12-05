import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2   # calcula pi por 2 para el area
    

class Rectangulo:
    def __init__(self, altura, base):
        self.altura =altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura
    
class Triangulo:
    def __init__(self, altura,base):
        self.altura =altura
        self.base = base

    def calcular_area(self):
        return (self.base * self.altura) / 2
    
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor= base_menor
        self.altura =altura

    def calcular_area(self):
        return((self.base_mayor + self.base_menor)+ self.altura) /2
        