class FuncionTrigonometrica: # crear uno nuevo con matplotlib 
    def __init__(self, tipo, amplitud, periodo):
        self.tipo = tipo # seno, coseno o tangente
        self.amplitud = amplitud
        self.periodo = periodo


    def evaluar(self, x):
        # Solo usamos valores conocidos en radianes
        if self.tipo == 'seno': 
            if x == 0:
                return 0
            elif x == 1.57:  # π/2
                return self.amplitud * 1
            elif x == 3.14:  # π
                return 0
            
        elif self.tipo == 'coseno':
            if x == 0:
                return self.amplitud * 1
            elif x == 1.57:    # π/2
                return 0
            elif x == 3.14:
                return self.amplitud * -1
            
        elif self.tipo == 'tangente':
            if x == 0:
                return 0
            elif x == 1.57:  # π/2
                return "infinito"
        return "Valor no disponible"

    def mostrar_funcion(self):
        return f"{self.amplitud} * {self.tipo}(x / {self.periodo})"

    def valor_critico(self):
        if self.tipo == 'seno' or self.tipo == 'coseno':
            return self.amplitud
        else:
            return "No tiene máximo definido"
# Crear una función seno con amplitud 1 y periodo 6.28 (2π)
f = FuncionTrigonometrica('seno', 1, 6.28)

print(f.mostrar_funcion())              # Muestra la fórmula
print("Valor en π/2:", f.evaluar(1.57)) # Muestra el valor en π/2
print("Valor crítico:", f.valor_critico()) # Muestra el máximo
