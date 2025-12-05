class Pedido:
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.platos = []  # Lista de platos (nombre, precio)
        self.total = 0

    def agregar_plato(self, nombre, precio):
        self.platos.append((nombre, precio))
        self.total += precio

    def calcular_total(self):
        return self.total

    def __len__(self):
        return len(self.platos)

    def __add__(self, otro):
        if self.numero_mesa == otro.numero_mesa:
            nuevo = Pedido(self.numero_mesa)
            nuevo.platos = self.platos + otro.platos
            nuevo.total = self.total + otro.total
            return nuevo
        else:
            return "No se pueden combinar pedidos de mesas distintas"

    def __str__(self):
        texto = f"Pedido Mesa {self.numero_mesa}:\n"
        for nombre, precio in self.platos:
            texto += f"- {nombre}: ${precio}\n"
        texto += f"Total: ${self.total}"
        return texto

    def __del__(self):
        print(f"Pedido de la mesa {self.numero_mesa} ha sido completado.")

        #creacion de objetos
p1 = Pedido(4)
p1.agregar_plato("Hamburguesa", 5000)
p1.agregar_plato("Bebida", 1500)
p1.agregar_plato("Pancito",1000)

print(p1)               # Muestra el pedido
print(len(p1))          # Muestra cuántos platos hay

p2 = Pedido(3)
p2.agregar_plato("Postre", 3000)

p3 = p1 + p2            # Combina los pedidos
print(p3)

del p3                  # Elimina el pedido combinado
