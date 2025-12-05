class GestorEventos:
 # atributos de la clase
    creados = 0 #contadorsglobal
    def __init__(self):
        # atributo privado (diccionario de eventos)
        self.__eventos = {} # que guarda mi dic.( "titulo:str", capacidad:int, "inscritos" : )

    def registrar(self,titulo:str,capacidad:int) ->int:
           if not titulo.strip():
               raise ValueError ("El titulo no puede estar vacío")
           if capacidad <= 0:
               raise ValueError ("La capacidad debe ser mayor a 0")
           
            # incrementa el contador global
           GestorEventos.creados +=1
           id_evento = GestorEventos.creados

             #crea el evento que va ir guardando en el dic.
           self.__eventos[id_evento] = {
            "titulo": titulo,
            "capacidad": capacidad,
            "inscritos": 0
            }
           return id_evento
    
    def inscribir(self,id:int,cantidad:int=1) -> None:
        if id not in self.__eventos:
             raise ValueError("ID Invalido")
        if cantidad <= 0 :
             raise ValueError("La cantidad debe ser mayor a :0")
        
        evento = self.__eventos[id]
        if evento["inscritos"] + cantidad > evento["capacidad"]:
             raise ValueError ("No hay suficientes cupos disponibles")
        evento["inscritos"]  += cantidad
    

    def cancelar(self,id:int,cantidad:int=1) -> None:
         if id not in self.__eventos:
              raise ValueError("ID invalido")
         if cantidad <= 0:
              raise ValueError("la cantidad debe ser mayor que 0")
         
         evento = self.__eventos[id]
         if cantidad > evento ["inscritos"]:
              raise ValueError("No puedes cancelar mas de los inscritos")
    
         evento["inscritos"] -= cantidad

    def cupos_disponibles(self,id:int) ->int:
         if id not in self.__eventos:
              raise ValueError("ID invalido")
         evento = self.__eventos[id]
         return evento ["capacidad"] - evento ["inscritos"]
    
    def __len__(self) -> int:
         return len(self.__eventos)
    
    @classmethod
    def total_creados(cls) -> int:
         return cls.creados
    
    def mostrar_eventos (self):
         for id, datos in self.__eventos.items():
            print(f"ID: {id} | Título: {datos['titulo']} | Capacidad: {datos['capacidad']} | Inscritos: {datos['inscritos']}")



#crea objetos o instancias de clase
evento1 = GestorEventos()
evento2 = GestorEventos()

id1 = evento1.registrar("Charla IA",100)
id2 = evento2.registrar("Charla FÍsica Aplicada" ,50)

evento1.mostrar_eventos()


    







