# Ejercicio:
# Hacer un sistema de eventos
# Necesitaremos un sistema de eventos para mandar/procesar estos eventos 
# y tendremos eventos de tipo json, tipo txt y tipo console
# quiero que implementeis la lógica real de estos eventos
#   los eventos json me crearan un json del evento
#   los eventos txt me crearan un txt con líneas que representan el evento
#   y los console me permitirán ver por pantalla los eventos (muy útil para debugear)
# ejemplo de uso:
# crear un gestor de eventos (console por ejemplo)
# crear un sistema de ventos  (tambiene llamado bus de eventos)
# hacer una lista de eventos como puede ser "login", "logout", "error"
# ejecutar/procesar estos eventos por orden, y comprobar que los gestores de eventos hacen esto correctamente
    # sistema.procesar("login", "open", "user auth", "logout", "close")
    # y eso va al gestor
    # si el gestos es json, pues tendrás un diccionario
    # imagínate que tiene como clave los comandos y como valor las veces que se han usado (un contador)
    # si el gestor es txt, pues tendrá una línea con cada vez que se uso, tal vez un timestamp, y todo en orden
    # si el gestor es console, hará un print en orden, para que se vea por consola el propio evento 
# puntos extra si me dividis bien el código en módulos, si me hacéis el anotado de tipos correctamente, 
# y si me subis el código a github para corregirlo

import eventos
import eventos2
from gestor import *

evento=eventos2.Login()
inst=Gestor_eventos(Gestor_consola)
# inst.registrar(eventos.callback_fun(eventos.open,"Manuel","archivo.xlsx"))
inst.registrar(evento)