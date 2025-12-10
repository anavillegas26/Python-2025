class Productos:
    IVA = 0.19
    PRODUCTOS_CREADOS={}
    CATEGORIA ={"ABARROTES","BEBIDAS","CARNE"}
    contador_productos = 0

    def __init__(self,nombre:str,categoria:str,precio_base:float):
        self.nombre =nombre
        self.categoria = categoria
        self.precio_base = precio_base
        self.descuento = 0

        assert self.es_categoria_valida (categoria)
        if precio_base < 0:
           raise ValueError("El precio no puede ser negativo")


    
def __str__(self):
    return f"Estos son lo mejor en {self.nombre}, la mejor calidad en {self.categoria}\n",
        
@classmethod
def total_productos_creados(cls):
    return cls.contador_productos

@classmethod
def listar_productos(cls):
    return cls.PRODUCTOS_CREADOS

def aplicar_descuento(self, porcentaje: float = None):
        
        if porcentaje is not None:
            # Descuento manual
            if 0 <= porcentaje <= 100:
                self.descuento = porcentaje
            else:
                raise ValueError("El porcentaje debe estar entre 0 y 100")
        else:
            # Descuento automático basado en precio
            if self.precio_base >= 10000:
                self.descuento = 10
                print(f"¡Ganaste un descuento del 10%!")
            elif self.precio_base >= 8000:
                self.descuento = 0.5
                print(f"¡Ganaste un descuento del 0.5%!")
            else:
                self.descuento = 0
                print("No tienes derecho a descuento")
    
def calcular_precio_con_descuento(self) -> float:
       
        if self.descuento > 0:
            descuento_monto = self.precio_base * (self.descuento / 100)
            return self.precio_base - descuento_monto
        return self.precio_base

def precio_final(self, incluir_iva: bool = True) -> float:
        
        precio = self.calcular_precio_con_descuento()
        
        if incluir_iva:
            precio += precio * self.IVA
        
        return precio
    
def mostrar_info_completa(self):
     
        precio_con_descuento = self.calcular_precio_con_descuento()
        precio_final_con_iva = self.precio_final()
        
        print(f" ganaste un descuento del 10%!!")
   
def precio_final(self,incluir_iva:bool):
    if (self.precio_base) + (self.IVA) =(self.precio_final)
       (self.precio_final) <10000
       aplicar_descuento

producto1 = Productos(self,"los chinos","arroz",800)
producto2 = Productos(self,"Trattoria","spaguettis"750)
producto3 = Productos(self,"Pepsi", "bebida",1000)

print(self.producto1)
print(self.producto2)

       

    
