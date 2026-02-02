 

# Ejercicio 1 - Voy a crear estudiantes y voy a imprimir sus notas, dame su nota mas alta
""" 
estudiantes = [
    {
        "nombre": "Paula",
        "edad": 24,
        "notas": [7.5, 5.1, 3.0, 7.7]
    },
    {
        "nombre": "David",
        "edad": 666,
        "notas": [3.3, 6.2, 7.8, 4.9]
    },
    {
        "nombre": "Carlos",
        "edad": 6,
        "notas": [3.0, 6.9, 7.8, 1.0]
    }
              ]
for estudiante in estudiantes:
    minima_nota = min(estudiante["notas"])
    print(minima_nota)
 """    


# Ejercicio 2 - Crear un perro e imprimir su raza
""" 
perro={
     "raza":"border collie",
     "peso":35,
     "nombre": "Rolo"
}
perros=[
    {
     "raza":"border collie",
     "peso":30,
     "nombre": "Toby"
    },
    {
     "raza":"dogo",
     "peso":24,
     "nombre": "Lassie"
    }
]

for perro in perros:
    print(f"\traza: {perro["raza"]}, peso {perro["peso"]}")


a=[f"nombre: {perro["nombre"]}" for perro in perros]
print(a)
"""
""" 
#DICCIONARIOS
dic1={1:"hola", "clave2":"trompeta"} 
dic2={3:"adios", "clave2":"trompeta"} 
dic3=dic1|dic2      # si existe la clave, la actualiza, si no existe, la añade: Comando "pipe" '|' de actualización
print(dic3)
"""

#Ejercicio:
# Quiero que hagáis un usuario con contraseña y email (opcional), algunas veces tiene email, otras veces NO
# quiero que me imprimais ambos casos (sin error de clave!)
"""
usuarios=[
    {"nombre": "fulano",
     "email":"fulano@gmail.com",
     "pswd":"aaa"},
    
    {"nombre": "mengano",
     "email":""},
    
    {"nombre": "zutano",
     "email":"zulano@gmail.com"}    
]


for usuario in usuarios:
    #print(usuario["nombre"],usuario["email"],usuario["pswd"])   # esto peta para el segundo usuario, porque no existe
    
    # esto funciona
    #usuario.setdefault("email","")
    #usuario.setdefault("pswd","")
    #print(usuario["nombre"],usuario["email"],usuario["pswd"]) 
    
    #esto también
    print(usuario.get("nombre"),usuario.get("email"),usuario.get("pswd")) 
    
#inicializacion diccionario
lista_claves=["nombre","email","pswd"]
valor_comun=""

diccionario={}
for usuario in range(3):
    diccionario=diccionario.fromkeys(lista_claves,valor_comun)
    print(diccionario)
    
#enumerate: vomita clave y valor de una lista
lista=[10,20,30,40]

for clave,valor in enumerate(lista):
    print(clave,valor)


for clave,valor in enumerate(usuarios):
    print(clave,valor)
"""
""" 
# EJERCICIO:
notas=[3.4, 5.0, 7.1, 4.8]
#añadir nota
notas.append(6.0)
print(notas)

#eliminar la segunda (por posicion)
print(notas.pop(1))

#total de notas
print(f"total de notas: {len(notas)}")

#ordenar
notas.sort()
print(notas)

#eliminar la mínima (por valor)
notas.remove(min(notas))
print(notas)
 """

"""
# EJERCICIO:
#  Quiero que me hagáis una lista que sea una playlist de canciones, y quiero que me hagáis, en este orden:
canciones=["aaa","bbb","zzz","rrrr"]
canciones.reverse()
#  ver que canciones hay en la playlist
print(canciones)
#  añadir al final de la playlist una canción nueva
canciones.append("ccc")
print(canciones)
#  eliminar la segunda canción
canciones.pop(1)
print(canciones)
#  buscar en que posición esta una canción que hayas metido
print(canciones.index("rrrr"))
#  decirme cuantas canciones hay en la playlist
print(f"Hay {len(canciones)} en la lista")
#  darle la vuelta a la playlist
canciones.sort(reverse=True)
print(canciones)
"""

usuario={"nombre": "fulano",
         "email":"fulano@gmail.com",
         "pswd":"aaa"}
clave_valor_1, valorclave_valor_2, _ = usuario.items()
print(clave, valor)