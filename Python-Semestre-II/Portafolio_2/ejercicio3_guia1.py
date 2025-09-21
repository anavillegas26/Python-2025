class Producto:
    def __init__(self, nombre, precio, cantidad, codigo): #creando constructor
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.historial = [] # lista para guardar

    def actualizar_stock(self, cambio):
        self.cantidad += cambio   
        self.historial.append(cambio) # agregar con append

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} | Código: {self.codigo} | Precio: ${self.precio} | Stock: {self.cantidad}"
class Inventario:
    def __init__(self):
        self.productos = {} # guardar en diccionario

    def agregar_producto(self, producto):
        self.productos[producto.codigo] = producto

    def actualizar_stock(self, codigo, cambio):
        if codigo in self.productos:
            self.productos[codigo].actualizar_stock(cambio)

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def valor_total_inventario(self):
        total = 0
        for producto in self.productos.values():
            total += producto.valor_total()
        return total
# Crear productos
p1 = Producto("Lápiz", 100, 50, "001")
p2 = Producto("Cuaderno", 500, 30, "002")

# Crear inventario
inv = Inventario()

# Agregar productos al inventario
inv.agregar_producto(p1)
inv.agregar_producto(p2)

# Actualizar stock
inv.actualizar_stock("001", 10)   # Se agregan 10 lápices
inv.actualizar_stock("002", -5)   # Se venden 5 cuadernos

# Mostrar productos
inv.mostrar_productos()

# Mostrar valor total del inventario
print("Valor total del inventario: $", inv.valor_total_inventario())
