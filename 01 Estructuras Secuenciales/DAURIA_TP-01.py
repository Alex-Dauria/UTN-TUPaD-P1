# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombre2 = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre2} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"Area: {area}, Perimetro: {perimetro}")

# Ejercicio 5
segundos = int(input("Dime una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

# Ejercicio 6
num = int(input("Escribe un número: "))

# Ciclo para/for para iterar del 1 al 10 y evitar realizarlo manualmente

for i in range(1, 11):
    resultado = num * i
    print(f"{num} * {i} = {resultado}")

# Ejercicio 7
print("Ingrese 2 números distintos a 0: ")
numA = int(input("Primer número: "))
numB = int(input("Segundo número: "))

# Realizamos un if por si el usuario ingresa 0

if numA != 0 and numB != 0:
    suma = numA + numB
    resta = numA - numB
    multiplicacion = numA * numB
    division = numA / numB
    print(f"""    {numA} + {numB} = {suma}
    {numA} - {numB} = {resta}
    {numA} * {numB} = {multiplicacion}
    {numA} / {numB} = {division}""")
else:
    print("Uno de los números es 0. Intenta nuevamente.")

# Ejercicio 8

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal es {imc}")

# Ejercicio 9

celcius = float(input("Dime la temperatura en Grados Celcius: "))
fahrenheit = (9/5) * celcius + 32
print(f"{celcius}° Celcius equivalen a {fahrenheit}° Farenheit.")

# Ejercicio 10

print("Ingrese los 3 números: ")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los 3 números es {promedio}.")
