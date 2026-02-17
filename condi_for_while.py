"""
# 1
Ana está desarrollando un programa que necesita procesar una lista de 5 nombres de clientes para generar informes mensuales. 
Para ello, necesita escribir un programa que recorra la lista de nombres y muestre cada cliente.
clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]
Ayuda a Ana a decidir entre usar un lazo for o while. Escribe el programa usando el lazo que creas más adecuado para esta 
tarea y explica por qué elegiste ese lazo.

CÓDIGO
clientes = ["Juan", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print("Cliente:", cliente)
"""
"""
# 2
André está probando una nueva función en el backend de Buscante que procesa datos en un bucle. 
Durante las pruebas, se dio cuenta de que el sistema dejó de responder y sospecha que el problema está en un bucle infinito.
contador = 0

while contador < 10:
    print("Procesando datos...")

¿Cuál es el problema del código de André y cómo resolverlo?

CÓDIGO
# el problema es que no creo un contador para iterar varias veces
# por lo tanto al definir contador en 0 y no tener el contador la proposición es siempre verdadera"
# para solucionarlo debemos colocar un contador

contador = 0

while contador < 10:
    print("Procesando datos...")
    contador += 1
"""
"""
# 3
Marcos está desarrollando un programa para mostrar un mensaje de bienvenida repetidamente en la consola, 
como parte de una campaña de marketing de su plataforma llamada Buscante. Quiere asegurarse de que el mensaje se muestre 5 veces.

Ayuda a Marcos a escribir un programa que muestre el mensaje: "¡Bienvenido a Buscante!" el número exacto de veces que necesita.

Salida esperada:

Texto repetido cinco veces con la frase "¡Bienvenido a Buscante!" 

CÓDIGO
mensaje = "¡Bienvenido a Buscante!"
c = 1
while c<=5:
    print("\t¡Bienvenido a Buscante!")
    c +=1
_______otra forma mas facil _________
for i in range(5):
    print("\t¡Bienvenido a Buscante!")

"""
"""
# 4
Estás recibiendo una lista de valores que representan los productos de tu tienda virtual 
y te gustaría calcular la suma total de esos productos para entender el desempeño financiero semanal.
valores = [10, 20, 30, 40, 50]
Crea un programa para implementar la suma.

CÓDIGO
valores = [10, 20, 30, 40, 50]

# t = sum(valores)
# print(f"\n\tLa suma total de los ingresos es: ${t}")
# la anterior esta bien pero para entrenar con bucles debemos

suma = 0

for i in valores:
    suma += i  
# esto es que para cada i (osea cada puesto) en valores, agarre suma (que ya definimos en 0) y le sume 
# el i iterable que tenemos
print(f"\n\tLa suma total de los ingresos es: ${suma}")
"""
"""
# 5
Ana está desarrollando su portafolio para exhibir los proyectos de Python que ha completado. 
Ella organizó una lista con el nombre de cada proyecto, pero se dio cuenta de que algunos 
elementos pueden estar ausentes, apareciendo como None:
proyectos = ["sitio web", "juego", "análisis de datos", None, "aplicativo móvil"]
Crea un programa que ayude a Ana a recorrer la lista de proyectos y muestre los nombres de 
los proyectos válidos. Si encuentra un elemento None, el programa debe mostrar el mensaje: "Proyecto ausente".

Salida esperada: 
sitio web
juego
análisis de datos
proyecto ausente
aplicativo móvil

CÓDIGO

proyectos = ["sitio web", "juego", "análisis de datos", None, "aplicativo móvil"]

for i in proyectos:
    if not i:
    # if proyectos is None
        print("\tproyecto ausente")
        continue   
    # aqui en vez de continue se puede colocar else y de una print(proyecto)
    print(f"\t{i}")

"""
"""
# 6
José está desarrollando una funcionalidad en el sistema de Buscante para interrumpir 
la búsqueda tan pronto como se encuentre un libro específico. La lista de libros ya 
registrados en el sistema es la siguiente:
libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]
Ayuda a José a crear un programa que recorra la lista y muestre el mensaje "Libro encontrado: 
<nombre del libro>" tan pronto como se encuentre el libro "El Hobbit". Después de encontrar 
el libro, el programa debe detener inmediatamente la búsqueda, sin verificar los libros restantes.

Salida esperada:
Libro encontrado: El Hobbit

CÓDIGO
libros = ["1984", "Cien años de soledad", "El Principito", "El Hobbit", "Orgullo y Prejuicio"]
buscando = "El Hobbit"

for i in libros:
    if i == buscando:
        print(f"\n\tNombre del Libro: {buscando}")
        break

"""
"""
# 7
Estás desarrollando un sistema de control de inventario para Buscante. 
Uno de los requisitos es verificar la cantidad de ejemplares de un libro en inventario y 
continuar vendiendo hasta que el inventario se agote. Siempre que se realiza una venta, 
el sistema debe informar al usuario y actualizar la cantidad disponible.

Crea un programa que simule las ventas de un libro con el inventario inicial de 5 ejemplares.
 El programa debe mostrar el mensaje "¡Venta realizada! Inventario restante: <cantidad>" con cada venta y, 
al final, mostrar el mensaje "Inventario agotado".
Salida esperada:
¡venta realizada! Inventario Restante: 5
¡venta realizada! Inventario Restante: 4
¡venta realizada! Inventario Restante: 3
¡venta realizada! Inventario Restante: 2
¡venta realizada! Inventario Restante: 1
Inventario Agotado

CÓDIGO
cantidad = 5
while cantidad <=5:
    print(f"\t¡venta realizada! Inventario Restante: {cantidad}")
    cantidad -= 1
    if cantidad == 0:
        print("\tInventario Agotado")
        break
"""
"""
# 8
Aline está implementando una funcionalidad que muestra mensajes personalizados 
para los clientes durante una promoción especial de su nueva librería. El sistema debe 
mostrar un mensaje de cuenta regresiva personalizado para cada número de 10 a 1, y al 
final mostrar el mensaje: "¡Aprovecha la promoción ahora!".

Crea un programa que utilice un bucle for para mostrar los siguientes mensajes:

Para números pares, muestra: "Faltan solo <número> segundos - ¡No pierdas esta oportunidad!".
Para números impares, muestra: "La cuenta continúa: <número> segundos restantes.".
Al final de la cuenta, muestra el mensaje: "¡Aprovecha la promoción ahora!".
Salida esperada:

CÓDIGO
cuenta = 10

while cuenta >= 0:
    if cuenta % 2 == 0 and cuenta != 0:
        print(f"\tFaltan solo {cuenta} segundos - ¡No pierdas esta oportunidad!")
    elif cuenta == 0:
        print("\t¡Aprovecha la promoción ahora!")
    else:
        print(f"\tLa cuenta continúa: {cuenta} segundos restantes.")
    cuenta -= 1

"""
"""
# 9 
Ana está implementando un sistema de filtrado de libros en Buscante. 
La funcionalidad debe recorrer una lista de libros y mostrar el nombre de cada 
libro disponible en stock. Sin embargo, si el libro está agotado, debe ser ignorado durante la iteración.
libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]
Crea un programa que ayude a Ana a mostrar solamente los libros que tienen stock disponible, 
en el formato: "Libro disponible: <nombre del libro>".

Salida esperada:
Libro disponible: 1984
Libro disponible: El principito
Libro disponible: Orgullo y Prejuicio

CÓDIGO

libros = [
    {"nombre": "1984", "stock": 5},
    {"nombre": "Dom Casmurro", "stock": 0},
    {"nombre": "El Principito", "stock": 3},
    {"nombre": "El Hobbit", "stock": 0},
    {"nombre": "Orgullo y Prejuicio", "stock": 2}
]
 
for i in libros:
    if i["stock"] == 0:
        continue
    else:
        print(f"\tLibro disponible: {i["nombre"]}")
"""
"""
# 10
João está desarrollando un sistema de registro para un sitio de lectura. 
Necesita asegurarse de que los usuarios ingresen un nombre de usuario y una 
contraseña válidos. Las reglas son las siguientes:

El nombre de usuario debe tener al menos 5 caracteres.
La contraseña debe tener al menos 8 caracteres.
João quiere que el sistema siga solicitando la información hasta que ambas 
condiciones se cumplan. Cuando el usuario ingresa datos válidos, el programa 
debe mostrar el mensaje: "¡Registro realizado con éxito!".

Crea un programa que implemente esta lógica usando un bucle while.

Salida esperada:

CÓDIGO

// Este primer código es el que se le ocurre a uno por defecto, sin embargo no pide la contraseña varias veces sino
// que se reinicia, para no tener este error ver el código 2
código 1
# nombre = input("\tEscriba su nombre de usuario: ")
# while len(nombre) < 5:
#         print("\tNombre de usuario muy corto, debe tener al menos 5 caracteres")
#         nombre = input("\tEscriba su nombre de usuario: ")



# while true:
#     contra = input("\tEscriba una contraseña: ")
#     if len(contra) < 8:
#         print("\tContraseña de usuario muy corta, debe tener al menos 8 caracteres")
#     else: 
#         break
# print("\t¡Registro realizado con éxito! \n\t su nombre de usuario es: {nombre}\n\t su contraseña es: {contra} ")

código 2

nombre = ""
contra = ""

while len(nombre) < 5 or len(contra) < 8:
    if len(nombre) < 5:
        nombre = input("\tEscriba el nombre de usuario: ")
        if len(nombre) < 5:
            print("\tNombre de usuario muy corto, debe tener al menos 5 caracteres")  
            continue
        
    contra= input("\tEscriba la contraseña: ")
    if len(contra) < 8:
        print("\tContraseña de usuario muy corta, debe tener al menos 8 caracteres")
        continue
    print(f"\t¡Registro realizado con éxito! \n\t su nombre de usuario es: {nombre}\n\t su contraseña es: {contra} ")

Esta es la que envían como opinion del instructor.
sin embargo pasa lo mismo que con el código 1

while True:
    nombre_usuario = input("Digite su nombre de usuario: ")
    contraseña = input("Digite su contraseña: ")

    if len(nombre_usuario) < 5:
        print("El nombre de usuario debe tener al menos 5 caracteres.")
        continue

    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue

    print("¡Registro realizado con éxito!")
    break
"""
