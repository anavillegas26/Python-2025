class MetodoDePago:
    
    def __init__(self, monto):
        self.monto = monto
        self.estado = "pendiente"
    
    def procesar_pago(self):
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def obtener_estado(self):
        return self.estado
    
    def obtener_monto(self):
        return self.monto

class MetodoDePagoConValidacion(MetodoDePago):
    
    def __init__(self, monto):
        super().__init__(monto)
        self.validado = False
    
    def validar(self):
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def procesar_pago(self):
        if not self.validado:
            return {"exito": False, "mensaje": "El pago debe ser validado primero"}
        
        return self._ejecutar_pago()
    
    def _ejecutar_pago(self):
        raise NotImplementedError("Las subclases deben implementar este método")

class TarjetaCredito(MetodoDePagoConValidacion):

    def __init__(self, monto, numero_tarjeta, cvv):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv
    
    def validar(self):
        # Simulación de validación
        if len(self.numero_tarjeta) == 16 and len(self.cvv) == 3:
            self.validado = True
            return {"exito": True, "mensaje": "Tarjeta validada correctamente"}
        else:
            self.validado = False
            return {"exito": False, "mensaje": "Datos de tarjeta inválidos"}
    
    def _ejecutar_pago(self):
        self.estado = "completado"
        return {
            "exito": True,
            "mensaje": f"Pago de ${self.monto} procesado con tarjeta ****{self.numero_tarjeta[-4:]}"
        }


class TransferenciaBancaria(MetodoDePagoConValidacion):
    
    def __init__(self, monto, cuenta_origen):
        super().__init__(monto)
        self.cuenta_origen = cuenta_origen
        self.codigo_confirmacion = None
    
    def validar(self):
        # Simulación de validación
        if len(self.cuenta_origen) >= 10:
            self.validado = True
            # Genera código de confirmación
            self.codigo_confirmacion = f"CONF-{self.cuenta_origen[-4:]}-{id(self) % 10000}"
            return {
                "exito": True,
                "mensaje": f"Cuenta validada. Código de confirmación: {self.codigo_confirmacion}"
            }
        else:
            self.validado = False
            return {"exito": False, "mensaje": "Cuenta bancaria inválida"}
    
    def _ejecutar_pago(self):
        self.estado = "completado"
        return {
            "exito": True,
            "mensaje": f"Transferencia de ${self.monto} completada. Código: {self.codigo_confirmacion}"
        }


class PagoEfectivo(MetodoDePago):
    
    def __init__(self, monto, monto_recibido):
        super().__init__(monto)
        self.monto_recibido = monto_recibido
    
    def procesar_pago(self):
        if self.monto_recibido >= self.monto:
            self.estado = "completado"
            cambio = self.monto_recibido - self.monto
            return {
                "exito": True,
                "mensaje": f"Pago de ${self.monto} recibido en efectivo",
                "cambio": cambio
            }
        else:
            return {
                "exito": False,
                "mensaje": f"Monto insuficiente. Faltan ${self.monto - self.monto_recibido}"
            }

class ProcesadorPagos:
    
    def ejecutar_pago(self, metodo_pago):
        
        print(f"Procesando pago de ${metodo_pago.obtener_monto()}")
        print(f"Tipo: {metodo_pago.__class__.__name__}")
        
        
        # Si el método requiere validación, la ejecutamos
        if isinstance(metodo_pago, MetodoDePagoConValidacion):
            if not metodo_pago.validado:
                print("\n→ Validando método de pago...")
                resultado_validacion = metodo_pago.validar()
                print(f"  {resultado_validacion['mensaje']}")
                
                if not resultado_validacion['exito']:
                    return resultado_validacion
        
        # Procesamos el pago
        print("\n→ Procesando pago...")
        resultado = metodo_pago.procesar_pago()
        print(f"  {resultado['mensaje']}")
        
        if 'cambio' in resultado and resultado['cambio'] > 0:
            print(f"  Cambio: ${resultado['cambio']}")
        
        return resultado

def demo_sistema_pagos():
 
    procesador = ProcesadorPagos()
    
    # Caso 1: Tarjeta de crédito
    
    print("CASO 1: PAGO CON TARJETA DE CRÉDITO")
    tarjeta = TarjetaCredito(
        monto=150.00,
        numero_tarjeta="1234567890123456",
        cvv="123"
    )
    procesador.ejecutar_pago(tarjeta)
    print(f"\nEstado final: {tarjeta.obtener_estado()}")
    
    # Caso 2: Transferencia bancaria
    print("CASO 2: PAGO CON TRANSFERENCIA BANCARIA")
    transferencia = TransferenciaBancaria(
        monto=500.00,
        cuenta_origen="1234567890"
    )
    procesador.ejecutar_pago(transferencia)
    print(f"\nEstado final: {transferencia.obtener_estado()}")
    
    # Caso 3: Pago en efectivo
    print("CASO 3: PAGO EN EFECTIVO")
    efectivo = PagoEfectivo(
        monto=75.00,
        monto_recibido=100.00
    )
    procesador.ejecutar_pago(efectivo)
    print(f"\nEstado final: {efectivo.obtener_estado()}")
    
    # Caso 4: Tarjeta inválida (demostración de validación fallida)
    print("CASO 4: TARJETA INVÁLIDA")
    tarjeta_invalida = TarjetaCredito(
        monto=200.00,
        numero_tarjeta="123",  # Número inválido
        cvv="1"
    )
    procesador.ejecutar_pago(tarjeta_invalida)
    print(f"\nEstado final: {tarjeta_invalida.obtener_estado()}")
    
    # Demostración de LSP: Todos los métodos pueden usarse intercambiablemente
    print("DEMOSTRACIÓN LSP: LISTA DE PAGOS MIXTOS")

    
    pagos = [
        TarjetaCredito(100, "1234567890123456", "123"),
        PagoEfectivo(50, 60),
        TransferenciaBancaria(300, "9876543210")
    ]
    
    for i, pago in enumerate(pagos, 1):
        print(f"\n--- Pago {i} ---")
        procesador.ejecutar_pago(pago)


# Ejecutar demostración
if __name__ == "__main__":
    demo_sistema_pagos()
        
       