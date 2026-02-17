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


