class Reserva_Hostal:
    #contructor
    def __init__(self,nombre_cliente,fecha_entrada, fecha_salida,num_habitacion):
        self. nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada #formato de fecha Año/mes/dia
        self.fecha_salida = fecha_salida
        self.num_habitacion = num_habitacion


#Métodos de clase


    def calcular_duracion_estadia(self):
        #Calcula duración aproximada en días
        entrada = list(map(int, self.fecha_entrada.split("-")))
        salida = list(map(int, self.fecha_salida.split("-")))
        dias = (salida[0] - entrada[0]) * 365 + (salida[1] - entrada[1]) * 30 + (salida[2] - entrada[2])
        return dias

    def cambiar_fecha_salida(self, nueva_fecha):
        #Cambia la fecha de salida
        self.fecha_salida = nueva_fecha
        print(f"Nueva fecha de salida: {self.fecha_salida}")

    def __str__(self):
        #Muestra la información de la reserva
        return (f"Reserva de {self.nombre_cliente} en habitación {self.num_habitacion}.\n"
                f"Entrada: {self.fecha_entrada} | Salida: {self.fecha_salida} | "
                f"Duración estimada: {self.calcular_duracion_estadia()} noches.")

    def __del__(self):
        
        print(f"La reserva de {self.nombre_cliente} ha sido cancelada.")

# Ejemplo de uso
reserva = Reserva_Hostal("Andrea ", "2025-09-10", "2025-09-15", "Suite 3")
print(reserva)
reserva.cambiar_fecha_salida("2025-09-17")
print(reserva)
del reserva

