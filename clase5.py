""" 
lista=[1,2,3,4,5,6]
lista2=lista
print(lista2)

var1,var2,*resto,varN=lista
print(resto)
 """

#EJERCICIO:
# Filtrar lista de votantes
""" 
lista_votantes=[
    {"nombre":"fulano",
     "edad":14},
    {"nombre":"mengano",
     "edad":18},
    {"nombre":"zutano",
     "edad":82},
    {"nombre":"joselui",
     "edad":35}
]
print(f"lista votante tiene {len(lista_votantes)} miembros")
for votante in lista_votantes:
    if votante["edad"]>=18:
        print(f"{votante["nombre"]} puede votar")
 """
"""  
#EJERCICIO:
# lista de la compra
lista=[]
continuar=True
while continuar:
    # Opción 1
    #articulo=input("intruduce artículo ('q' para salir): ")
    #articulo=articulo.lower()    

    # Opción 2
    articulo=input("intruduce artículo ('q' para salir): ").lower()
    
    if articulo=="q":
        break
    
    if articulo in lista:
        lista.remove(articulo)
    else:
        lista.append(articulo)
    
    print(lista) 
"""

#EJERCICIO:
#ordenar temperaturas:
""" 
temps=[1,65,8.6,56,24,5,-8,-65,0.5,4]
valoracion=[]
for temp in temps:
    valoracion.append("caliente" if temp>40 else "frio" if temp<10 else "templado")
listaDeTuplas=zip(temps,valoracion)
diccionario=dict(listaDeTuplas)
#print(valoracion)
print(list(listaDeTuplas))
#print(diccionario)
print(diccionario.keys())
 """

#EJERCICIO: Constrasñas 
# Compruebo si coinciden
# Si coinciden: Usuario hacen login
# No coinciden: Hay que volver a intentarlo
# Pero MAXIMO se puede intentar 3 veces, si no lo ha conseguido, se imprime "Usuario bloqueado"
""" 
pswd_real="hola1"
max_intentos=3

for intento in range(max_intentos):

    pswd=input("Introduce contraseña: ")

    if pswd_real==pswd:
        print("LOGIN...")
        break
    else:
        if intento==max_intentos-1: 
            print("Usuario bloqueado")
 """
""" 
#EJERCICIO: Carrito compra
carrito={
    "camiseta":1,
    "puzzle":2,
    "mandarinas":6,
    "cebollas":0,
    "jersey":3,
    "pijama":0
}
#borrando de una copia 
carrito_filtrado=carrito.copy()
for clave in carrito.keys():
    if carrito[clave]==0:
         carrito_filtrado.pop(clave)
    
print(carrito_filtrado)

#generando de 0
carrito_filtrado={}
for clave in carrito.keys():
    if carrito[clave]!=0:
        carrito_filtrado.update({clave:carrito[clave]})

print(carrito_filtrado)

#otra opcion generando de 0
carrito_filtrado={}
for clave,valor in carrito.items():
    if valor!=0:
        carrito_filtrado.update({clave:valor})

print(carrito_filtrado)

#otra opcion generando de 0
carrito_filtrado={}
for clave,valor in carrito.items():
    if valor!=0:
        carrito_filtrado[clave]=valor   #si se asigna y no existe, lo crea

print(carrito_filtrado)

#otra opción, generando dos listas: una de claves y otra de valores
#ABSOLUTAMENTE ANTI-PYTHONesco
lista_claves=list(carrito.keys())
lista_valores=list(carrito.values())
#print(list(enumerate(lista_claves)))
for indice,numero in enumerate(lista_valores):
    if numero>0:
        carrito_filtrado[lista_claves[indice]]=numero

print(carrito_filtrado)
 """
# EJERCICIO
# Hacer un sistema de lista de alumnos
# Podemos meter los alumnos que queramos (tienen nombre)
# y cuando paremos (por ejemplo STOP), me dice el total de alumnos
# además, el limite de alumnos es 8
# si hay mas de 8, quiero que me deis un mensaje especial CADA VEZ QUE SE METE UN NUEVO ALUMNO a partir de esa cantidad, 
# y entonces podéis meter hasta 10, pero me habrá avisado de que la clase ya se estaba llenando
# y no debería dejar meter mas de 10
 
lista=[]
limite=4
limiteExt=6

for it in range(limiteExt):
    nuevoAlumno=input("Introduce nombre nuevo alumno ('q' para salir): ").title()
    
    if nuevoAlumno.lower()=="q":
        break

    lista.append(nuevoAlumno)
    total=len(lista)    
    
    if total<=limite:
        continue
    elif total<limiteExt:
        print("Llegando al límite...")
    else:
        print("Listado completo")
        break

print(lista)
print(f"Total alumnos = {total}")