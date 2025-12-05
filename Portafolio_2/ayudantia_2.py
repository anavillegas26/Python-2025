class Trabajador:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def tareas_generales(self):
        return (f" El trabajador {self.nombre} esta barriendo")
    
class Chef(Trabajador):
    def __init__(self,nombre,edad):
        super().__init__(self,nombre)
        self.edad = edad

    def tareas_generales(self):
        return super().tareas_generales( f"El Chef {self.nombre} esta haciendo un pastel")
    
class Mesero(Trabajador):
    def __init__(self, nombre ):
        super().__init__(self,nombre)
        

    def tareas_generales(self):
        return super().tareas_generales(f"El Mesero{self.nombre} esta tomando pedido en la mesa 4")
    
class Ayudante(Chef,Mesero):
    def __init__(self, nombre,edad,color_delantal):
        Chef().__init__(self,nombre, edad)
        Mesero().__init__(self,nombre)
        self.color_delantar = color_delantal
    
 #  instaciar clase
Trabajador= ("Benja")
Mesero = ("Juanito","Azul")
Chef = ("Pedrito", 35)
Ayudante =("Daniel",15, "Verde")


Mesero.tareas_generales
Chef.tareas_generales
Ayudante.tareas_generales

    
