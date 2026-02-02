# EJERCICIOS VARIABLES
""" 
# Ejercicio: Poner todos los nombres en minuscula
variables = ("john", "DOE", "sTaRlEtTe", "TesT")
variables2=[]

for nombre in variables:
    variables2.append(nombre.upper())
print(variables2) 
"""


""" 
# Aqui me vais a hacer los ejercicios para mañana
 
# 1. Un alumno con varias notas y quiero que me imprima todas sus notas
alumno1 = {
    "nombre": "Juan",
    "notas": [7.5, 8.0, 6.9, 9.2, 7.8]
}
alumno2 = {
    "nombre": "Pedro",
    "notas": [9.5, 4.0, 8, 5.2, 8.8]
} 

lista_alumnos=(alumno1,alumno2)
for al in lista_alumnos:
    print(al["nombre"], sum(al["notas"])/len(al["notas"]))
"""

#Ejercicio: Hacer un diccionario que represente una persona, pidiendo por terminal su edad y su nombre
# (debería de meterse dentro del diccionario), y validar si es mayor o menor de edad, si es mayor de edad, 
# imprimir toda la información, y si es menor de edad, hay que censurar su nombre con # 

""" 
# VERSIÓN POCO PYTHONESCA
# inicializacion en vacío
persona={
    "nombre":"",
    "edad":0        
}
persona["nombre"]=input("Nombre del sujeto? ")
persona["edad"]=int(input("Edad del sujeto? ")) 

# if TONTAINA
if persona["edad"]>=18:
    print(f"\tNombre:\t{persona["nombre"]}\n\tEdad:\t{persona["edad"]}")
else:
    print(f"\tNombre:\t###\n\tEdad:\t{persona["edad"]}") 
"""
""" 
# VERSIÓN ELEGANTE
persona={
    "nombre": input("Nombre del sujeto? "),
    "edad": int(input("Edad del sujeto? ")),        
}

print(f"\tNombre:\t{persona["nombre"] if persona["edad"]>=18 else "###"}\n\tEdad:\t{persona["edad"]}")  # CONDICIONAL TERNARIO :)

 """
 
#Ejercicio avanzado: 
# Tenemos un área donde van a ir cayendo cajas, las cajas se deben de ir amontonando verticalmente, 
# pero cuando una capa completa esta cubierta de cajas, ese nivel desaparece. Hacer un sistema que simule esto, 
# y donde pueda consultar en cualquier momento la altura máxima de cajas 
# (suponer que voy a ir iterando lanzar cajas de forma aleatoria)
# es área x e Y, pero se van a acumular en Z
# todas las cajas son iguales, y si, pueden caer en cualquier posicion

import random
import numpy as np
dimX,dimY=3,2

caja=(1,1,1)
almacen2D=np.zeros((dimX,dimY))

while input("Pulsa ENTER para ir dejando caer cada caja, 'q' para salir: ")!="q":
    
    coordXYnuevaCaja=(random.randint(0,dimX-1),random.randint(0,dimY-1))
    print(coordXYnuevaCaja)

    almacen2D[coordXYnuevaCaja[0],coordXYnuevaCaja[1]]+=1

    numCajasFila0=0
    for i in range(dimX):
        for j in range(dimY):
            if almacen2D[i,j]!=0:
                numCajasFila0+=1

    if numCajasFila0 == dimX*dimY:
        almacen2D=almacen2D-1

    print(almacen2D)            
    print(f"Num cajas: {numCajasFila0}")
    
    
""" 
# ESTO ES UN DOLOR
almacen2D=[[0 for x in range(dimX)] for y in range(dimY)]
almacen2DNuevo=[[0 for x in range(dimX)] for y in range(dimY)]  # Recálculo si primera fila completa

stop=""
while stop!="q":
    stop=input("Pulsa ENTER para ir dejando caer cada caja, 'q' para salir")
    coordXYnuevaCaja=(random.randint(0,dimX-1),random.randint(0,dimY-1))
    print(coordXYnuevaCaja)

    almacen2D[coordXYnuevaCaja[1]][coordXYnuevaCaja[0]]+=1      # almacen2D[coordY][coordX] << absolutamente antiintuitivo


    
    for i in range(dimX):
        for j in range(dimY):
            if almacen2D[j][i]!=0:
                almacen2DNuevo[j][i]=almacen2D[j][i]-1
            else: break
 """

""" 
    numCajasFila0=0
    for fila in almacen2D:
        for pos in fila:
            if pos!=0:               
                numCajasFila0+=1
            else: break
        
        print(fila)
 """
"""
a=[1,2,3]
b=[1,1,1]
#b=a

b=[x-1 for x in a]
a[0]=8
print(b)
print(b is a)
"""
"""
import numpy
c=[a,b]
c=numpy.array(c)
print(c)
d=c-1
#d=[x-1 for x in c]
d[0,1]=10
print(d)
"""
