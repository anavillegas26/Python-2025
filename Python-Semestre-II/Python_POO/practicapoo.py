import pandas as pd
df = pd.read_csv("Data/libros_filtrados.csv")


class Libro:
    def __init__(self,autor,idioma,año,genero,precio=10000):
        self.autor = autor
        self.idioma = idioma
        self.año = año
        self.genero = genero
        self.precio = precio
        
    def __str__ (self): 
         return f" {self.autor} ({self.año})- {self.genero}[{self.idioma}]"
    


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_por_autor(self, autor):
        return [libro for libro in self.catalogo if autor.lower() in libro.autor.lower()]
    
    
class Carrito:
    def __init__(self):
        self.items = []

    def agregar(self, libro):
        self.items.append(libro)

    def total(self):
        return sum(libro.precio for libro in self.items)


# Cargar CSV
df = pd.read_csv("Data/libros_filtrados.csv")

biblioteca = Biblioteca()
carrito = Carrito()

# Cargar libros desde el DataFrame
for _, fila in df.iterrows():
    libro = Libro(
        autor=fila["Author(s)"],
        idioma=fila["Original language"],
        año=fila["First published"],
        genero=fila["Genre"]
    )
    biblioteca.agregar_libro(libro)


# Buscar libros por autor
resultados = biblioteca.buscar_por_autor("Gabriel García Márquez")
for libro in resultados:
    print(libro)
    carrito.agregar(libro)

print("Total a pagar:", carrito.total())


