# Ejercicio
# Queremos hacer un sistema de notificaciones (SMS, email, push, ...)
# Crear un servicio de alertas que procese estas notificaciones
# puntos extra: separar la definición de la notificación y su implementación con una fabrica

""" 
    # no funciona
from abc import ABC, abstractmethod


# INTERFAZ: clase abstracta.....
class Notificacion(ABC):
    def __init__(self, mensaje):
        self.tipo=""
        self.msg=mensaje
    
    @abstractmethod
    def enviar(self):
        print("Enviando ",end="") 

class SMS(Notificacion):
    def __init__(self):
        self.tipo="SMS"
    
    def enviar(self):
        print(f"{self.__class__.__name__}...")

class Sistema_alertas:

    def __init__(self,tipo:Notificacion,mensaje:str):
        self.tipo=tipo 
        self.tipo.msg=mensaje

    
def crear_notificacion(self,tipo:Notificacion):
    self.tipo=tipo

alerta=Sistema_alertas(SMS,"mañana llueve")
alerta.
miSMS=alerta.crear_notificacion(SMS)
miSMS.enviar()
#miSMS.enviar()
 """


# SOLUCIÓN 1
from abc import ABC, abstractmethod

# INTERFAZ: clase abstracta...
class Notificador(ABC):
    def __init__(self):
        self.historial = []
    
    @abstractmethod
    def enviar(self, mensaje):  # ESTE MÉTODO VA A SER SOBREESCRITO POR EL MÉTODO DE LA SUBCLASE QUE HEREDA
        ...                     # por lo tanto no tiene sentido definir nada

class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Email: {mensaje}")
        self.historial.append(mensaje)

class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"SMS: {mensaje}")
        self.historial.append(mensaje)

class PushNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Push: {mensaje}")
        self.historial.append(mensaje)

class NotificadorFabrica:
    @staticmethod
    def crear(tipo):
        if tipo == "email":
            return EmailNotificador()
        if tipo == "sms":
            return SMSNotificador()
        if tipo == "push":
            return PushNotificador()
        raise ValueError("Notificador no implementado")

class ServicioAlerta:
    def __init__(self, notificador):
        self.notificador = notificador

    def notificar(self, mensaje):
        self.notificador.enviar(mensaje)




notificador = NotificadorFabrica.crear("email")
servicio = ServicioAlerta(notificador)
servicio.notificar("Hola mundo")


# SOLUCIÓN 2:
from abc import ABC, abstractmethod

class Notificador(ABC):  # Interfaz
    historial = []
    
    @abstractmethod
    def enviar(self, mensaje):
        ...
    
    def añadir_historial(self, mensaje):
        self.historial.append((mensaje, self.__class__.__name__))


class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Email: {mensaje}")
        self.añadir_historial(mensaje)

class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"SMS: {mensaje}")
        self.añadir_historial(mensaje)

class PushNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Push: {mensaje}")
        self.añadir_historial(mensaje)


class NotificadorFabrica:
    @staticmethod
    def crear(tipo):
        if tipo == "email":
            return EmailNotificador()
        if tipo == "sms":
            return SMSNotificador()
        if tipo == "push":
            return PushNotificador()
        raise ValueError("Notificador no implementado")


class ServicioAlerta:
    def __init__(self, notificador):
        self.notificador = notificador

    def notificar(self, mensaje):
        self.notificador.enviar(mensaje)


notificador = NotificadorFabrica.crear("push")
servicio = ServicioAlerta(notificador)
servicio.notificar("Hola mundo")
servicio.notificar("Test")
notificador_2 = NotificadorFabrica.crear("sms")
servicio.notificador = notificador_2
servicio.notificar("Test en otro servicio")
print(notificador.historial)
print(notificador_2.historial)