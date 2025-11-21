class Membresia:
     creadas = 0
     tarifas_membresias = {"Diario": 10.000, "Pase10":20.000,"Ilimitado":39.000}

     def __init__(self,nombre:str, plan:str):
        '''crea una nueva menbresia. pre:plan válido'''
        assert self.es_plan_valido(plan), f"Plan'{plan}' no es valido. Debe ser: Diario, Pase 10 o Ilimitado"

        self.__nombre = nombre
        self.__plan = plan
        self.__activa = True # todas las menbresias comienzan activas

        #configurar los créditos segun el plan
        if plan == "Pase10":
            self.__creditos =10  # pase 10 inicia con 10 creditos

        else :
            self.__creditos = 0 # otros planes no usan créditos

        #contador "creadas" suma 1 por cada menbresia creada
        Membresia.creadas += 1

        #assert : verifica que pase 10 tenga 10 creditos
        if plan == "Pase10":
            assert self.__creditos == 10, "Pase 10 debe iniciar con 10 creditos"
        else:
            assert self.__creditos == 0, "Planes distintos de Pase 10 no deben tener créditos iniciales"
        
     def __str__ (self) ->str :
        "' devuelde una representación legible del objeto'" 
        estado = "Activa" if self.__activa else "Congelada"
        if self.__plan == "Pase10":
            return f"{self.__nombre}- {self.__plan}({self.__creditos} creditos)- {estado}"
        return f"{self.__nombre}- {self.__plan}- {estado}"

     @staticmethod
     def es_plan_valido(plan:str)->bool:
        '''Retorna True si el plan es valido: diario, pase10, ilimitado'''
        return plan in {"Diario","Pase10", "Ilimitado"}  #verifica si el plan esta
    
     @classmethod
     def total_creadas(cls) ->int:
        assert cls.creadas >=0 #el contador no puede ser negativo
        return cls.creadas
    
     @property
     def plan(self)->str:
        return self.__plan
    
     @plan.setter
     def plan(self, nuevo_plan:str): """Cambia el plan, Pre: membresia activa y plan valido"""
        assert self.__activa, "No se puede cambiar plan de una membresia inactiva"
        assert self.es_plan_valido(nuevo_plan), f "Plan '{nuevo_plan}'no valido"
        if self._plan == "Pase10" and nuevo_plan i ="Pase10":
            self.__creditos = 0

        if nuevo_plan == "Pase10" and self.__plan i = "Pase10"
            self.__creditos = 0

        self.__plan = nuevo_plan
    
        if self.__plan == "Pase10"
            assert self.__creditos == 10, "Al cambiar a Pase10, debe tener 10 creditos"
        else:
            assert self.__creditos == 0, "Planes distintosa Pase10 no deben tener creditos"


     @plan.setter
     def plan(self, nuevo_plan: str):
        """Cambia el plan. Pre: membresía activa y plan válido"""
        assert self.__activa, "No se puede cambiar el plan de una membresía inactiva"
        assert self.es_plan_valido(nuevo_plan), f"Plan '{nuevo_plan}' no es válido"

        # Ajuste de créditos según cambio de plan
        if self.__plan == "Pase10" and nuevo_plan != "Pase10":
            self.__creditos = 0
        elif self.__plan != "Pase10" and nuevo_plan == "Pase10":
            self.__creditos = 10

        self.__plan = nuevo_plan

        # Verificaciones finales
        if self.__plan == "Pase10":
            assert self.__creditos == 10, "Al cambiar a Pase10, debe tener 10 créditos"
        else:
            assert self.__creditos == 0, "Planes distintos a Pase10 no deben tener créditos"

     @plan.setter
     def plan(self, nuevo_plan: str):
        """Cambia el plan. Pre: membresía activa y plan válido"""
        assert self.__activa, "No se puede cambiar el plan de una membresía inactiva"
        assert self.es_plan_valido(nuevo_plan), f"Plan '{nuevo_plan}' no es válido"

        # Ajuste de créditos según cambio de plan
        if self.__plan == "Pase10" and nuevo_plan != "Pase10":
            self.__creditos = 0
        elif self.__plan != "Pase10" and nuevo_plan == "Pase10":
            self.__creditos = 10

        self.__plan = nuevo_plan

        # Verificaciones finales
        if self.__plan == "Pase10":
            assert self.__creditos == 10, "Al cambiar a Pase10, debe tener 10 créditos"
        else:
            assert self.__creditos == 0, "Planes distintos a Pase10 no deben tener créditos"

