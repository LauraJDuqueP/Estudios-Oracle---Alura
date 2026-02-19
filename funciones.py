"""
# 1
1 - Escribe un código que lee la lista siguiente y realiza:
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 1. Leer el tamaño de la lista
# 2. Leer el valor máximo y mínimo
# 3. Calcular la suma de los valores de la lista
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.

CÓDIGO
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

tamano = len(lista)
maxi = max(lista)
mini = min(lista)
suma = sum(lista)
# cuando coloques esto en codigo debes poner triple comilla en f-strings para que el salto de linea
# no afecte el código
print(f"\t La lista tiene {tamano} números, donde el mayor es {maxi} y el menor es {mini}. 
             la suma de los valores es: {suma} ")
"""
"""
# 2 
2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, 
según la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:
# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70

CÓDIGO
numero = int(input("Digite un número del 1 - 10: "))
def tabla_multiplicar():
    print(f"\tTabla de multiplicar del número {numero}")
    for i in range(11):
        print(f"{numero} * {i} = {numero*i}")

tabla_multiplicar()
"""
"""
# 3
3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:
[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

CÓDIGO
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def nueva_lista(x):
    return [i for i in x if i % 3 ==0]

print(nueva_lista(lista))

"""
"""
# 4
4 - Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.
CÓDIGO
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nueva_lista = list(map(lambda i : i**2, lista))
print("- ".join(map(str, lista)))
print("- ".join(map(str, nueva_lista)))

"""
"""
# 5 
Aplicando a proyectos

5 - Has sido contratado como científico(a) de datos de una asociación de skate. 
Para analizar las notas recibidas por los skaters en algunas competiciones a lo 
largo del año, necesitas crear un código que calcule la puntuación de los atletas. 
Para ello, tu código debe recibir 5 notas ingresadas por los jueces.

CÓDIGO
    
notas = []
for i in range(5):
    notas.append(float(input(f"Ingrese la {i+1} nota: ")))

notas.sort()
notas.pop(0)
notas.pop(len(notas)-1)
print(f"\tLas notas son {" - ".join(map(str, notas))}")
puntaje = sum(notas)/len(notas)
print(f"\tLa puntuación es: {puntaje:.2f}")
"""

