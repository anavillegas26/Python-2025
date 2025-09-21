class Fraccion:
     # constructor de clase 
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

# Método 
    def __str__ (self):
        return f"La fraccion  tiene un numerador con valor: {self.numerador}, y el denominadorcon valor :{self.denominador}"

    def __add__ (self,other):
        nuevo_denomminador = self.denominador * other.denominador
        nuevo_numerador = self.numerador * other.denominador






fraccion1 = Fraccion (4,6)




print(fraccion1)