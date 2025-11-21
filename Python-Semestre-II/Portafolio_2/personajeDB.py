class personajeDB:
    contador_personajes = 0  #contador global

    def __init__(self, nombre:str, raza:str, nivel_poder=1000):
        self.__nombre = nombre
        self.__raza = raza
        self.__niveL_poder= nivel_poder
        self.__transformacion_actual = "Base"

    # incrementar el contador
        personajeDB.contador_personajes += 1
        self._id_personaje = personajeDB.contador_personajes

    #metodos magicos
    def __str__(self)->str:
        return f"{self.__nombre} ({self.__raza}) - Poder: {self.__niveL_poder} - Tranformacion: {self.__transformacion_actual}"    

    def __repr__(self):
        return f"PersonajeDB(nombre='{self.__nombre}', raza='{self.__raza}', nivel_poder={self.__niveL_poder})"
    
    def __len__(self):
        return len(self.__nombre)
    
    def __add__(self,otro):
        if isinstance(otro, personajeDB):
           nuevo_poder= self.__niveL_poder + otro.__niveL_poder
           return personajeDB(f"Fusión_{self.__nombre}_{otro.__nombre}","Fusión", nuevo_poder)
        return self
    
    def __gt__(self, otro):
        return self.__niveL_poder > otro.__nivel_poder
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if isinstance(nuevo_nombre,str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            print("El nombre debe ser una cadena no vacia")

    @property
    def nivel_poder(self):
        return self.__niveL_poder
    
    @nivel_poder.setter
    def nivel_poder(self, nuevo_poder):
        if isinstance(nuevo_poder,(int,float)) and nuevo_poder >=0:
          self.__niveL_poder = nuevo_poder
        else:
            print("El nivel de poder debe ser un numero positivo")

    @property
    def transformacion_actual(self):
        return self.__transformacion_actual
    #metodos de la clase
      
    @classmethod
    def getcontador_personajes(cls):
        return cls.contador_personajes
    
    @classmethod
    def resetcontador(cls):
        cls.contador_personajes = 0

    #metodos de instancia
    def mostrar_info(self):
        print(f"ID:{self._id_personaje} | {self}")
        
    def entrenar(self,incremento=100)->int:
        self.__niveL_poder += incremento
        print(f"{self.__nombre} ha entrenado mucho!! Poder aumentado a{self.__niveL_poder}")