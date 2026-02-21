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

"""
# 6
6 - Para cumplir con una demanda de una institución educativa para el 
análisis del rendimiento de sus estudiantes, necesitas crear una función 
que reciba una lista de 4 notas y devuelva:

# mayor nota
# menor nota
# media
# situación (Aprobado(a) o Reprobado(a))
# Uso de la función
# Mostrar: El estudiante obtuvo una media de `media`, 
# con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)

CODIGO
#aunque esto resuelve, lo mejor es separar los principio
# Funciones → procesan datos
# print() → muestra datos
# input() → recibe datos
print('\tAnalisis de rendimiento del estudiante, digite las notas:')
lista_notas = [float(input(f"Digite la {i+1} nota ")) for i in range(4) ]
def lis(lista):
    
    mayor = max(lista)
    mini = min(lista)
    media = sum(lista)/len(lista)
    situa = "Aprobado" if media >= 6 else "Reprobado"
    return (print(f'\tEl estudiante obtuvo una media de: {media},'
        f'\n\tcon la mayor nota de: {mayor} puntos'
        f'\n\tla menor nota de: {mini} puntos'
        f'\n\tsituacion: {situa}'
        ))

lis(lista_notas)

# aqui separemos las responsabilidades

print('\tAnalisis de rendimiento del estudiante, digite las notas:')

def lis(lista):
    
    mayor = max(lista)
    mini = min(lista)
    media = sum(lista)/len(lista)
    situa = "Aprobado" if media >= 6 else "Reprobado"
    return mayor, mini, media, situa

lista_notas = [float(input(f"Digite la {i+1} nota ")) for i in range(4) ]
mayor, mini, media, situa = lis(lista_notas)
mostrar_datos = (print(f'\tEl estudiante obtuvo una media de: {media:.2f},'
        f'\n\tcon la mayor nota de: {mayor:.2f} puntos'
        f'\n\tla menor nota de: {mini:.2f} puntos'
        f'\n\tsituacion: {situa}'
        ))

"""
"""
# 7
 Has recibido una demanda para tratar 2 listas con los nombres y apellidos de 
 cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:
nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# Puedes apoyarte en la función map()

CODIGO
nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

def convertir_nombres(list1, list2):
    nombres_nuevos = list(map(str.capitalize, list1))
    apellido_nuevos = list(map(str.capitalize, list2))
    nuevos_nombres = list(map(lambda x,y : x +" "+ y, nombres_nuevos, apellido_nuevos))
    return nuevos_nombres    

resultado = convertir_nombres(nombres, apellidos)
print(', '.join(resultado))
"""
"""
# 8
Como científico de datos en un equipo de fútbol, necesitas implementar nuevas 
formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo 
en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del 
equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas 
de números enteros, representando los goles marcados y recibidos por el equipo en cada 
partido del campeonato. La función debe devolver la puntuación del equipo y el 
rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, 
el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. 
Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y 
la puntuación máxima que podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:
goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"

CODIGO
goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]

def calcula_puntos(x,y):
    puntos = list(map(lambda x,y: 3 if x>y else 1 if x==y else 0, goles_marcados,goles_recibidos))
    # 3,0,3,1,0
    rendimiento = (100*sum(puntos))/(len(puntos)*3)
    pun_max = sum(puntos)
    
    return pun_max, rendimiento

pun, rendi = calcula_puntos(goles_marcados,goles_recibidos)
print(f'\tLa puntuacion del equipo fue de: {pun} y su rendimiento fue de: {rendi:.2f}')
"""
"""
# 9
Te han desafiado a crear un código que calcule los gastos de un viaje a una de las 
cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina 
en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. 
Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, 
crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula 
los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# Recife costaría [gastos] reales.

CODIGO

#Salvador = 200, Fortaleza=400, Natal=250 y Aracaju=300 gastos
#Salvador = 850, Fortaleza=800, Natal=300 y Aracaju=550 km
#hotel 150 diarios
#gasolina 14 km/l
#gasolina costo 5 * 1l

gastos_por_ciudad = [200, 400, 250, 300]
km_distacia = [850, 800, 300, 550]

print('\tEstas son las ciudades a las que puedes ir desde Recife:\n\tSalvador = s\n\tFortaleza = f\n\tNatal = n\n\tAracaju = a')
destino = (input('A donde vas a viajar? Escribe la inicial de tu sitio favorito: '))
dias = int(input('Cuantos dias vas a viajar: '))

def gastos_hotel():
    h = dias*150
    return h
def lugar(destino):
    if destino == 's':
        l = 'Salvador'
        return l
    elif destino == 'f':
        l = 'Fortaleza'
        return g
    elif destino == 'n':
        l = 'Natal'
        return l
    elif destino == 'a':
        l = 'Aracaju'
        return l
    else:
        return ("Dato no valido, vuelve a empezar")
def gastos_gaso(destino):
    if destino == 's':
        g = (850*2)*14
        return g
    elif destino == 'f':
        g = (800*2)*14
        return g
    elif destino == 'n':
        g = (300*2)*14
        return g
    elif destino == 'a':
        g = (550*2)*14
        return g
    else:
        return 0

def gastos_viaje(destino, dias):
    if destino == 's':
        v = 200*dias
        return v
    elif destino == 'f':
        v= 400*dias
        return v
    elif destino == 'n':
        v = 250* dias
        return v
    elif destino == 'a':
        v = 300* dias
        return v
    else:
        return 0

costos_gaso = gastos_gaso(destino)
costos_hotel = gastos_hotel()
costos_viaje = gastos_viaje(destino, dias)
lugar = lugar(destino)

print(f'\tCon base en los datos, un viaje desde Recife a: {lugar} costaria en total {costos_gaso + costos_hotel + costos_viaje}: '
f'\n\tgasolina ida y vuelta: {costos_gaso}'
f'\n\thotel por los {dias} dias: {costos_hotel}'
f'\n\tcostos de paseos y alimentación: {costos_viaje} '
)

"""

"""
# 10
Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP). 
Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y 
filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda se 
centra en el análisis del patrón de comportamiento de las personas al escribir palabras de esta cantidad de caracteres o más.

Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la 
función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un 
iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.

Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para probar el código.

"""

frase= input('Escribe una frase de por lo menos 5 palabras')

frase_tratada = ( frase.replace(',',' ')
                     .replace('.',' ')
                     .replace('!',' ')
                     .replace('$',' ')
                     .replace(':',' ')
                     .replace(';',' ')
                     .replace('?',' ')
                     .replace('%',' ')
                     .replace('(',' ')
                     .replace(')',' ')
)

lista = frase_tratada.split()
nueva_lista = list(filter(lambda palabra: len(palabra) >= 5, lista))

print(nueva_lista)


