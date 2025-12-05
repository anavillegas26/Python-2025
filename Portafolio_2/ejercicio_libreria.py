
class Libro:
    def __init__(self, titulo, autor, valor, cantidad_disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__valor = valor
        self.cantidad_disponible = cantidad_disponible
    
        assert valor > 0, "Valor mayor a Cero"  # assert es para asegurar que el valor no sea menor a 0

    def mostrar_info(self):
     print(f"{self.__titulo} de {self.__autor} - ${self.__valor:,} CLP - Stock: {self.cantidad_disponible}")


    #metodos Getter 
    def get_titulo(self):
        return self.__titulo
    
    #metodos setter
    def set_titulo(self,nuevo_titulo):
        if isinstance(nuevo_titulo,str) and nuevo_titulo.strip(): #verifica que sea una cadena de texto
            self.__titulo =  nuevo_titulo
        else:
            print("El titulo del libro no puede estar vacio")

# Getter para valor
    def get_valor(self):
        return self.__valor

    # Setter para valor
    def set_valor(self, nuevo_valor):
        if isinstance(nuevo_valor, (int, float)) and nuevo_valor > 0: # isinstance verfica que sea un valor valido
            self.__valor = nuevo_valor
        else:
            print("El valor debe ser un número positivo.")

    @staticmethod
    def calcular_precio(valor):
        return valor * Libro._tasa_descuento
    


class Libreria:
    def __init__(self):
        self.catalogo = {}  # Diccionario: clave = título, valor = valor del libro

    def agregar_libro(self, libro):
        titulo = libro.get_titulo()
        if titulo in self.catalogo:
            print(f"El libro '{titulo}' ya está en el catálogo.")
        else:
            self.catalogo[titulo] = libro
            print(f"Libro agregado: {titulo}")

    def mostrar_catalogo(self):
        print("\n Catálogo de la librería:")
        for libro in self.catalogo.values():
            libro.mostrar_info()

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.catalogo.values() if titulo.lower() in libro.get_titulo().lower()]
    


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_libro(self, libro):
        self.items.append(libro)
        print(f"Libro añadido al carrito: {libro.get_titulo()}")

    def calcular_total(self):
        return sum(libro.get_valor() for libro in self.items)


    def calcular_total_con_descuento(self):
         total = self.calcular_total()
         cantidad = len(self.items)

        # Descuento progresivo: desde 3 libros en adelante
         if cantidad >= 3:
            descuento = min((cantidad - 2) * 0.05, 0.30)  # Máximo 30%
            total_descuento = total * (1 - descuento)
            print(f" Descuento aplicado: {descuento*100:.0f}%")
            return total_descuento
         else:
            print(" No hay descuento aplicado.")
            return total

    def mostrar_carrito(self):
        print("\n Carrito de compras:")
        for libro in self.items:
            libro.mostrar_info()
        total_final = self.calcular_total_con_descuento()
        print(f"Total a pagar: ${total_final:,.0f} Pesos")
              

categoria = Libreria()
# creando lod objetos(libros)
  
libro1 = Libro("Historia de dos ciudades","Charles Dickens",9990,3)
libro2 = Libro("El Principito","Antoine de Saint-Exupéry",7500,3)
libro3 = Libro("Harry Potter y la piedra filosofal","J. K. Rowling",12990,4)
libro4 = Libro("Diez negritos","Agatha Christie",8990,2)
libro5 = Libro("El cuento de Perico el conejo","Beatrix Potter",6990,1)
libro6 = Libro("Juan Salvador Gaviota","Richard Bach",8990,2)
libro7 = Libro("La oruga muy hambrienta","Eric Carle",6990,3)
libro8 = Libro("Un mensaje a García","Elbert Hubbard",5990,4)



categoria.agregar_libro(libro1)
categoria.agregar_libro(libro2)
categoria.agregar_libro(libro3)
categoria.agregar_libro(libro4)
categoria.agregar_libro(libro5)
categoria.agregar_libro(libro6)
categoria.agregar_libro(libro7)
categoria.agregar_libro(libro8)

categoria.mostrar_catalogo()

compras = Carrito()
compras.agregar_libro(libro1)
compras.agregar_libro(libro3,libro5,libro4)


compras.mostrar_carrito()

