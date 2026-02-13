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
