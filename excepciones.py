"""
# 1 
Haz un programa que solicite a la persona usuaria ingresar dos números decimales y 
calcular la división entre estos números. El código debe incluir un manejo de error, 
indicando el tipo de error que se generó si la división no es posible.

Prueba el programa con el segundo valor numérico de la entrada igual a 0. 
También prueba usando caracteres textuales en la entrada para verificar los tipos de errores que ocurren.

CODIGO
try:
    x = float(input("ingrese dos números decimales: "))  
    y = float(input("ingrese dos números decimales: "))
    if y == 0:
        raise ValueError("El denominador no puede ser 0, las divisiones por 0 no existen")
    resultado = x/y
except ValueError as e:
    print(f"Error de valor: {e}")
except ZeroDivisionError:
    print(f"Error: {e}")
else: 
    print(f"el resultado es: {resultado}")

"""
"""
# 2 
Haz un programa que solicite a la persona usuaria ingresar un texto 
que será una clave a buscar en el siguiente diccionario: 

edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, 
almacenando el resultado del valor en una variable. El código debe 
incluir un manejo de error KeyError, imprimiendo la información 'Nombre no encontrado' 
en caso de error, e imprimir el valor si no ocurre ninguno.

Prueba el programa con un nombre presente en una de las claves del diccionario y 
con uno que no esté en el diccionario para verificar el mensaje de error.

CODIGO

edades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nombre = input("Ingrese el nombre de la persona: ")
    edad = edades[nombre]
except KeyError: 
    print("Nombre no encontrado")
else:
    print(f"{nombre} tiene {edad} años")

"""

"""
# 3
Crea una función que reciba una lista como parámetro y convierta todos 
los valores de la lista a flotantes. La función debe incluir un manejo 
de error indicando el tipo de error generado y devolver la lista si no ha 
ocurrido ningún error. Por último, debe tener la cláusula finally para imprimir 
el texto: 'Fin de la ejecución de la función'.

CODIGO
listas = ["2.3", 4, "5.7", "5.6"]
def cambiar_flotantess(lista):
    try:
        nueva_lista = [float(i) for i in lista]
        return nueva_lista
    except Exception as e:
        print(f"El Error es: {type(e).__name__} - {e}")
        return None
    finally:
        print("Ejecución terminada")

#cambiar_flotantess(listas)
print(f"la nueva lista es {cambiar_flotantess(listas)}")
"""
"""
4 - Crea una función que reciba dos listas como parámetros y agrupe los elementos 
uno a uno de las listas, formando una lista de tuplas de 3 elementos. El primer y 
segundo elemento de la tupla son los valores en la posición i de las listas y el 
tercer elemento es la suma de los valores en la posición i de las listas.

La función debe incluir un manejo de error indicando el tipo de error 
generado y devolver como resultado la lista de tuplas. Si las listas enviadas 
como parámetro tienen tamaños diferentes, la función debe devolver un IndexError 
con la frase: 'La cantidad de elementos en cada lista es diferente.'.

Datos para probar la función:

Valores sin error:

lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]

Listas con tamaños diferentes:

lista1 = [4, 6, 7, 9, 10, 4]
lista2 = [-4, 6, 8, 7, 9]

Listas con valores incoherentes:

lista1 = [4, 6, 7, 9, 'A']
lista2 = [-4, 'E', 8, 7, 9]

"""
lista1 = [4, 6, 7, 9, 10]
lista2 = [-4, 6, 8, 7, 9]

