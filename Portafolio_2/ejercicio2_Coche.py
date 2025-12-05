class Coche():

    def __init__(self,marca,gasolina):
        self.marca = str(marca)
        self.gasolina = float(gasolina)
        self.kilometros_recorridos = 0.0

#metodo de la clase coche
    def conducir(self,km):
         # calcular cuantos km se puede recorrer con la gasolina actual
        km_posibles = self.gasolina * 10
        if km_posibles >= km:
            # hay gasolina para el viaje completo
            self.gasolina -= km / 10
            self.kilometros_recorridos += km 
            
        else: #solo se recorre hasta donde alcance la gasolina
            self.kilometros_recorridos += km_posibles
            self.gasolina = 0
            print(f"Solo pudo conducir hasta aquí, el coche se  quedó sin gasolina.")

    def cargar_gasolina(self, litros: float):
        self.gasolina += litros
        print(f"Gasolina actual: {self.gasolina} litros.")


automovil = Coche("Peugeot", 53.0)
automovil.conducir(100)
automovil.cargar_gasolina(20)
automovil.conducir(300)
print(f"Marca:{automovil.marca}")
print(f"Gasolina restante:{automovil.gasolina} litros")
print(f"Kilometros recorridos:{automovil.kilometros_recorridos} km")