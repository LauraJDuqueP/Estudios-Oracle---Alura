r"""
# 1 - 3
Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.
para hacer esto en un .py debes utilizar:
    1. verifica la ruta: 
        PS C:\Users\duque\Documents\Estudios-Oracle---Alura> // esto es un ejemplo
    2. en la terminal powerchell o bash debes instalar la biblioteca
        pip install matplotlib
    o   python -m pip install matplotlib
    o   py -m pip install matplotlib   ----> si tienes varias versiones
    3. luego si la vas a usar en tu archivo .py debes colocat:
        import matplotlib.pyplot as plt
    ahora si quieres instalar una version especifica:
        pip install matplotlib==3.7.1
    Para evitar problemas de entorno, mejor usa:
        python -m pip install matplotlib==3.7.1
    O si usas py en Windows:
        py -m pip install matplotlib==3.7.1
    como ver si se instalo bien:
      pip show matplotlib
    o dentro de python:
       import matplotlib
        print(matplotlib.__version__) 
  
2 - Escribe un código para importar la biblioteca numpy con el alias np.

3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

CÓDIGO

# 1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.
# la version 3.7.1 no es compatible con la 3.13 asi que dejaremos la 3.10.8que viene por defecto.
import matplotlib
print(matplotlib.__version__) 

# 2 - Escribe un código para importar la biblioteca numpy con el alias np.
# para hacer esto como es una bibioteca nueva hay que recordar instalarla primero en Terminal/CMD
import numpy as np
print(np.__version__)

# 3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.
# random ya viene instalado entonces solo hay que importarlo

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
from random import choice

print(f"El numero elegido es: {choice(lista)} jijiji")
"""
"""
# 4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

CÓDIGO
import random

numero = random.randint(0,99)

print(f"El número aleatorio menor que 100 es: {numero}")
"""
"""
# 5
5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

CÓDIGO
# usando la biblioteca math
import math 
 n = float(input(f"\tDigita el primer número: "))
 x = float(input("\tDigita el segundo número: "))

 print(f"\t{n} a la potencia de {x} es: {math.pow(n,x)}")

#basico usando ** que es potencia ya en el lenguaje

n = float(input(f"\tDigita el primer número: "))
x = float(input("\tDigita el segundo número: "))

print(f"\t{n} a la potencia de {x} es: {n**x}")

"""
"""
# 6
Aplicando a proyectos

6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. 
La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. 
Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

CÓDIGO
import random

n = int(input("\tIngresa el número de participantes del sorteo: "))
print(f"El número de participantes es: {n}")
print(f"El participante elegido es: {random.randint(1, n)}")

"""
"""
# 7
7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. 
El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria 
y muestre un mensaje junto a este token generado aleatoriamente.

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

CÓDIGO
import random
nombre = input("\tNombre del usuario: ")
token = random.randrange(1000, 9999, 2)
print(f"\tHola, {nombre}, tu token de acceso es {token} ¡Bienvenido/a!")
"""
"""
# 8
8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". 
En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que 
realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

import random
frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

seleccion = random.sample(frutas, 3)
print(f"\t¡DISFRUTA!, tus frutas sorpresas son: \n\t{seleccion[0]},\n\t{seleccion[1]},\n\t{seleccion[2]} ")
"""
"""
# 9
9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles 
resultan en un número entero. La lista es la siguiente:

numeros = [2, 8, 15, 23, 91, 112, 256]

CÓDIGO

import math 
numeros = [2, 8, 15, 23, 91, 112, 256]

enteros=[]
decimales=[]

for numero in numeros:
    raiz = math.sqrt(numero)

    if raiz.is_integer():
        enteros.append((numero,raiz))
    else:
        decimales.append((numero,raiz))

print("\tRaices Enteras: ")
for numero, raiz in enteros:
    print(f"\t{numero} : {raiz}")

print("\n\tRaices decimales: ")
for numero, raiz in decimales:
    print(f"\t{numero} :  {raiz}")

"""
"""
# 10
Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines
circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio 
del área circular y devuelve el valor en reales de cuánto tendrá que pagar.

CÓDIGO

import math

precio= 25

r = float(input("\tIngresa el radio de área circular donde quieres poner el cespet: "))
area = math.pi*(r**2)
print(f"\tEl precio del cespet es: ${precio*area:.2f}")

"""






    


