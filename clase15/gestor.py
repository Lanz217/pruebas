import eventos2
from abc import ABC, abstractmethod

class Gestor_generico(ABC):
    historial=[]
    
    @abstractmethod
    def log(self,evento):
        ...

# class gestor_txt(gestor_generico):
#     def log(self, event):
#         ...

class Gestor_consola(Gestor_generico):
    def log(self,evento):
        print(f"Evento: {eventos2.Login.result}")
        # print(f"Evento: {evento}")

class Gestor_eventos:
    def __init__(self,tipo_gestor:Gestor_generico):
        self.tipo=tipo_gestor
        
    def registrar(self,evento):
        self.tipo.log(evento)
        