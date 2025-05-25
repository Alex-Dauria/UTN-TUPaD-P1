# Práctico 5: Funciones - Alex Dauria

# ACTIVIDAD 1)

# Definir Funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa Principal
imprimir_hola_mundo()

# ACTIVIDAD 2)

# Definir Funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa Principal
nombre = input("Cual es tu nombre? ")
print(saludar_usuario(nombre))

# ACTIVIDAD 3)

# Definir Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa Principal
name = input("Nombre: ")
surname = input("Apellido: ")
age = input("Edad: ")
home = input("Residencia: ")

informacion_personal(name, surname, age, home)

# ACTIVIDAD 4) 

import math
# Definir Funciones
def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

def imprimir_resultados(area, perimetro):
    print(f"Area del circulo: {area:.2f}")
    print(f"Perimetro del circulo: {perimetro:.2f}")

# Programa Principal
radio = float(input("Radio del circulo: "))
imprimir_resultados(calcular_area_circulo(radio), calcular_perimetro_circulo(radio))

# ACTIVIDAD 5)

# Definir Funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

def imprimir_rta(segundos, horas):
    print(f"{segundos} segundos equivalen a {horas:.1f} horas.")

# Programa Principal
seg = int(input("Segundos: "))
imprimir_rta(seg, segundos_a_horas(seg))

# ACTIVIDAD 6) 

# Definir Funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

        
# Programa Principal
tabla_multiplicar(int(input("Tabla del número: ")))


# ACTIVIDAD 7)

# Definir Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None  # None si no se puede dividir
    return (suma, resta, multiplicacion, division)

# Programa Principal

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

resultados = operaciones_basicas(num1, num2)

print(f"{num1} + {num2} = {resultados[0]}")
print(f"{num1} - {num2} = {resultados[1]}")
print(f"{num1} * {num2} = {resultados[2]}")

if resultados[3] is not None:
    print(f"{num1} / {num2} = {resultados[3]:.1f}")
else:
    print("Error en la división. No se puede dividir por 0.")

# ACTIVIDAD 8) 

# Definir Funciones
def calcular_imc(peso, altura):
    imc = peso / ( altura ** 2)
    print(f"Indice de masa corporal (IMC): {imc:.2f}")
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif 18.5 <= imc < 25:
        print("Clasificación: Normal")
    elif 25 <= imc < 30:
        print("Clasificación: Sobrepeso")
    elif 30 <= imc < 35:
        print("Clasificación: Obesidad grado I")
    elif 35 <= imc < 40:
        print("Clasificación: Obesidad grado II")
    else:
        print("Clasificación: Obesidad grado III (mórbida)")

# Programa Principal
while True:
    try:
        peso = float(input("Peso en kilogramos: "))
        if peso <= 0:
            print("Ingrese un número mayor a 0.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

while True:
    try:
        altura = float(input("Altura en metros: "))
        if altura <= 0:
            print("Ingrese un número mayor a 0.")
        else:
            break
    except ValueError:
        print("Ingrese un número válido.")

calcular_imc(peso, altura)

# ACTIVIDAD 9)

# Definir Funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    print(f"{celsius}° Celsius = {fahrenheit:.2f}° Fahrenheit.")

# Programa Principal

while True:
    try:
        celsius = float(input("Temperatura en Celsius: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

celsius_a_fahrenheit(celsius)

# ACTIVIDAD 10)

# Definir Funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio es: {promedio}.")

# Programa Principal

print("¡Calculemos el promedio!")

while True:
    try:
        num1 = float(input("Número 1: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

while True:
    try:
        num2 = float(input("Número 2: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

while True:
    try:
        num3 = float(input("Número 3: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

calcular_promedio(num1, num2, num3)




