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
"""c = 1
while c<=5:
    print("\t¡Bienvenido a Buscante!")
    c +=1
"""
for i in range(5):
    print("\t¡Bienvenido a Buscante!")

"""


