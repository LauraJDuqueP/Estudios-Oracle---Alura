"""
# 1
Bruno gestiona un pequeño comercio y quiere saber qué producto tuvo el mejor desempeño de ventas el mes pasado. 
Registró la cantidad vendida de dos productos: manzanas y plátanos. Ahora, necesita escribir un programa que 
identifique y muestre cuál de ellos tuvo más ventas.

Crea un programa que reciba el número de ventas de los dos productos y muestre un mensaje indicando cuál de 
ellos vendió más. Si las cantidades son iguales, muestra un mensaje diciendo que hubo un empate.

CÓDIGO

M =int(input("Cuanas manzanas se vendieron, dame un valor entero "))
P = int(input("Cuantos plátanos se vendieron, dame un valor entero "))

if M > P:
    print(f"Se vendieron más manzanas que plátanos. Manzanas: {M} - Plátanos: {P}")
elif M < P:
    print(f"Se vendieron más plátanos que manzanas. Plátanos: {P} - Manzanas: {M}")
else:
    print(f"Las ventas fueron iguales. Manzanas: {M} - Plátanos: {P}")

"""
"""
# 2
Lucas trabaja en TI y necesita garantizar que la temperatura de una sala de servidores no supere los 25°C.
Quiere un programa que reciba la temperatura actual como entrada y, si es necesario, muestre un mensaje de alerta.

CÓDIGO

T = float(input("Digite la temperatura actual: "))

if T > 25:
    print(f"Alerta Roja: Se bloqueara la energia en los servidores. La temperatura es muy alta: {T}")
elif T > 22 and T <= 25:
    print(f"Alerta naranja: La temperatura esta subiendo al limite. Temperatua en: {T}")
else:
    print(f"La temperatura es estable, en limites normales. Temperatura en: {T}")

"""
"""
# 3
Camila está organizando un proyecto y necesita calcular el tiempo total necesario para concluir tres actividades: 
A, B y C. Sin embargo, si alguna actividad tiene un número de días negativo, el código debe avisar que los valores 
ingresados son inválidos y no calcular el total.

Escribe un programa que reciba el número de días de tres actividades y muestre el tiempo total del proyecto. 
Si algún valor es negativo, muestra un mensaje informando el error.

CÓDIGO

t = 0
A = float(input("Ingrese los días necesarios para terminar la Actividad A: "))
B = float(input("Ingrese los días necesarios para terminar la Actividad B: "))
C = float(input("Ingrese los días necesarios para terminar la Actividad C: "))

if (A>0 and B>0 and C>0):
    dic_actividad = {"Actividad_A": A, "Actividad_B": B, "Actividad_C": C}
    print(f"\n \t el total de horas necesarias para completar las 3 actividades es: {A+B+C} horas")
    for actividad, dias in dic_actividad.items():
        print(f"{actividad}: {dias}")
    
else:
    print("\n \t Error la cantidad de días no pueden ser negativos")

"""
"""
# 4
Anna Júlia está creando un sistema para calcular el Índice de Masa Corporal (IMC) y proporcionar 
recomendaciones básicas. El programa debe recibir el peso y la altura de una persona y mostrar el 
valor del IMC, además de indicar si está por debajo del peso, con peso normal o por encima del peso. 
Crea un programa que reciba el peso (en kg) y la altura (en metros) y calcule el IMC usando la fórmula: 
IMC = peso / (altura ** 2)Luego, muestra el valor del IMC y un mensaje indicando si está por debajo del peso (IMC < 18.5), 
peso normal (18.5 <= IMC < 25) o por encima del peso (IMC >= 25).

CÓDIGO

n = input("Cual es el nombre de la persona: ")
p = float(input("Cual es el peso de la persona en kg: "))
a = float(input("Cual es la altura de la persona en metros: "))
imc = p/(a**2)
if imc < 18.5:
    print(f"\n\t {n} esta por debajo del peso \n\t IMC de: {imc}")
    lista_dic = {"Nombre":n, "Peso":p, "Altura":a}
    for dato, valor in lista_dic.items():
        print(f"{dato} : {valor}")
elif 18.5 <= imc < 25:
    print(f"\n\t {n} esta en un peso normal \n\t  IMC de: {imc}")
    lista_dic = {"Nombre":n, "Peso":p, "Altura":a}
    for dato, valor in lista_dic.items():
        print(f"{dato} : {valor}")
elif imc >= 25:
    print(f"\n\t {n} esta por encima del peso \n\t  IMC de: {imc}")
    lista_dic = {"Nombre":n, "Peso":p, "Altura":a}
    for dato, valor in lista_dic.items():
        print(f"{dato} : {valor}")
"""

"""
# 5
Laura está desarrollando un sistema para saber si una persona tiene derecho a recibir un beneficio social. 
Para eso, la persona debe cumplir las siguientes condiciones:

Tener ingresos menores o iguales a $2,000.
Tener al menos un hijo o hija.
Crea un programa que reciba los ingresos mensuales y la cantidad de hijos de una persona, y diga si tiene derecho al beneficio.

CÓDIGO
n = input("Ingrese el nombre de la persona ")
ingresos = float(input("Ingreso mensual de la persona "))
hijos = int(input("Ingrese la cantidad de hijos de la persona "))

palabra_hijo = "hijo" if hijos == 1 else "hijos"


if ingresos <= 2000 and hijos >= 1: 
    print(f"\n\t{n} tiene derecho a recibir el beneficio \n\t Tiene {hijos} {palabra_hijo} \n\t Ingreso mensual de: {ingresos}" )
elif ingresos > 2000 and hijos >= 1:
    print(f"\n\t{n} NO tiene derecho a recibir el beneficio \n\t Tu ingreso mensual es mayor a 2000, es de: {ingresos}")
elif ingresos <= 2000 and hijos == 0: 
    print(f"\n\t{n} NO tiene derecho a recibir el beneficio \n\t No tienes hijos")
elif  ingresos > 2000 and hijos == 0:
   print(f"\n\t{n} NO tiene derecho a recibir el beneficio \n\t No tienes hijos y tu ingreso es mayor a 2000, es de: {ingresos}")
   
"""
"""
# 6
Una empresa evalúa a sus empleados con base en dos criterios:

Puntuación de desempeño (de 0 a 10)
Años trabajados
Reglas:

Si la puntuación es mayor o igual a 7:
Si trabajó más de 5 años: "Elegible para ascenso"
Si trabajó 5 años o menos: "Buen desempeño, sigue así"
Si la puntuación es menor a 7: "Necesita mejorar"
Crea un programa que reciba la puntuación y los años trabajados, y muestre el mensaje adecuado.

CÓDIGO

nombre = input("Cual es el nombre del empleado: ")
puntuacion = float(input(f"Cual es la puntuacion de trabajo de {nombre}: ")) 
años_trabajo = int(input(f"Cuanto tiempo en años tiene {nombre} de antiguedad en la empresa: "))

print(f"\n\tEvaluación de {nombre}")
if puntuacion >= 7 and años_trabajo > 5:
     print(f"\t{nombre} es elegible para ascenso")    
elif puntuacion >= 7 and años_trabajo <= 5:
    print(f"\t{nombre} tienes un buen desempeño en la empresa. ¡sigue así!")
else:
    print(f"\t{nombre} tu evaluación de desempeño es menor a 7 puntos. Necesitas mejorar")
"""
"""
# 7
Estás desarrollando un pequeño juego. El usuario ingresa un número entero y el programa debe evaluar lo siguiente:

Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"
Este tipo de lógica es muy útil en juegos, validaciones o filtros.

CÓDIGO

numero = int(input("\tIngresa un número entero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"\tFelicidades tú número es un ¡número mágico!")
elif numero % 3 == 0:
    print(f"\tTú número es divisible por 3")
elif numero % 5 == 0:
    print(f"\tTú número es divisible por 5")
else:
    print(f"\tTú número NO es un número mágico")

"""

"""
# 8
Una escuela otorga becas según tres criterios:

Ingreso familiar mensual.
Promedio del estudiante.
Asistencia (en porcentaje).
Reglas:

Si el ingreso es menor a $1,500 y el promedio es mayor a 8.0 y la asistencia es al menos 90% → "Beca completa"
Si el ingreso es menor a $2,500 y promedio mayor a 7.0 y asistencia al menos 85% → "Media beca"
En otros casos → "No elegible para beca"

CÓDIGO
nombre = input("\t Ingresa el nombre del estudiante: ")
ingreso_familiar = float(input(f"\t Ingresa el ingreso mensual familiar (en pesos) de {nombre}: "))
promedio = float(input(f"\t Cual es el promedio estudiantil de {nombre}: "))
asistencia = float(input(f"Ingresa la asistencia a clases en % de {nombre}: "))

print(f"\tEstudiante: {nombre}")

if ingreso_familiar < 1500 and promedio > 8 and asistencia >= 90:
    print(f"\t{nombre} Tienes una Beca Completa")
elif ingreso_familiar < 2500 and promedio > 7 and asistencia >= 80:
    print(f"\t{nombre} Tienes Media Beca")
else:
    print(f"\t{nombre} No eres elegible para una beca")
"""
"""
# 9 

Un sistema de transporte cobra según la edad del pasajero y la distancia recorrida:

Menores de 6 años: Viajan gratis.
De 6 a 18 años:
Hasta 20 km: $1.50
Más de 20 km: $2.50
Mayores de 18:
Hasta 20 km: $2.50
Más de 20 km: $4.00
Crea un programa que reciba la edad y distancia, y muestre el valor a pagar.

CÓDIGO
edad = float(input("\tIngresa la edad del pasajero: "))
distancia = float(input("\tIngresa la distancia que vas a recorrer en km: "))

if edad < 6:
    print("\tTu viaje es gratis")
elif edad <= 18:
    if distancia <= 20:
        print("\ttu pasaje cuesta $1.50")
    else:
         print("\ttu pasaje cuesta $2.50")
      
else: 
    if distancia <= 20:
        print("\ttu pasaje cuesta $2.50")
    else:
        print("\ttu pasaje cuesta $4.00")

CÓDIGO OPTIMiZADO
edad = float(input("\tIngresa la edad del pasajero: "))
distancia = float(input("\tIngresa la distancia que vas a recorrer en km: "))

tarifa_base = 1.50
tarifa_media = 2.50
tarifa_alta = 4.00

if edad < 6:
    print("\tTu viaje es gratis")
elif edad <= 18 and distancia <= 20:
    print(f"\ttu pasaje cuesta ${tarifa_base}")
elif edad <= 18 and distancia > 20:
    print(f"\ttu pasaje cuesta ${tarifa_media}")
elif edad > 18 and distancia <= 20:
    print(f"\ttu pasaje cuesta ${tarifa_media}")
else:
    print(f"\ttu pasaje cuesta ${tarifa_alta}")
"""
"""
# 10
Una empresa evalúa su trimestre con base en:

Ingresos totales
Gastos totales
Número de nuevos clientes
Clasificación:

Si ingresos - gastos > $10,000 y más de 50 nuevos clientes → "Trimestre Excelente"
Si ingresos - gastos > $5,000 y al menos 20 clientes → "Trimestre Bueno"
Si ingresos - gastos > 0 → "Trimestre Regular"
Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"

CÓDIGO
nombre = "Empresa_Laura"

ingresos = float(input(f"Cuanto es el ingreso total de la empresa {nombre}: "))
gastos = float(input(f"Cuanto es el gasto total de la empresa {nombre}: "))
clientes_nuevos = int(input(f"Cuantos clientes nuevos tiene la empresa {nombre}: "))

print(f"\t{nombre} \n\t Los Ingresos Totales Fueron: {ingresos}"
f"\n\t Los Gastos Totales Son: {gastos}"
f"\n\t El Número de Clientes Nuevos Es: {clientes_nuevos}"  
)

if ingresos - gastos > 10000 and clientes_nuevos > 50:
    print("\n\tTrimestre Excelente")
elif ingresos - gastos > 5000 and clientes_nuevos >= 20:
    print("\n\tTrimestre Bueno")
elif ingresos - gastos == 0:
    print("\n\tTrimestre Regular")
else:
    print("\n\tTrimestre Deficitario")
"""

c = 0

while(c<10):
    c += 1 
    print(c)
    if c <5: 
        break 
     




    
    











