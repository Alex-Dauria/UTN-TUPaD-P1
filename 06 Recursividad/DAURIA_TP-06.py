# Práctico 6: Recursividad - Alex Dauria

# ACTIVIDAD 1)
# Calcular el factorial de un número de forma recursiva y mostrar los factoriales desde 1 hasta n

# Definir Funciones
def factorial_recursivo(num):
    # Calcula el factorial de num usando recursión
    if num == 0:
        return 1 # Caso base
    else: 
        return num * factorial_recursivo(num - 1)

def mostrar_factoriales(desde, hasta):
    if desde > hasta:
        return # Caso base
    print(f"Factorial de {desde} es {factorial_recursivo(desde)}")
    mostrar_factoriales(desde + 1, hasta)

# Programa Principal
try:
    n = int(input("Ingresá un número entero positivo: "))
    if n <= 0:
        print("Por favor, ingresá un número entero positivo.")
    else:
        mostrar_factoriales(1, n)
except ValueError:
    print("Por favor, ingresá un número entero válido.")  # Maneja entradas inválidas

# ACTIVIDAD 2)
# Calcular el valor de la serie de Fibonacci en una posición y mostrar la serie hasta esa posición

# Definir Funciones
def fibonacci(n):
    if n == 0:
        return 0 # Caso base
    elif n == 1:
        return 1 # Caso base 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie(posicion, actual=0):
    if actual > posicion:
        return # Caso base
    print(fibonacci(actual), end=" ") # Imprime el valor de Fibonacci en la posición actual
    mostrar_serie(posicion, actual + 1) 

# Programa Principal
n = int(input("Ingresá la posición hasta la cual querés ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
mostrar_serie(n)
print() # Salto de línea para mejorar la presentación

# ACTIVIDAD 3)
# Calcular la potencia de un número base elevado a un exponente usando recursión

# Definir Funciones
def potencia(base, exponente):
    # Calcula base^exponente de forma recursiva
    if exponente == 0:
        return 1 # Caso base
    else:
        return base * potencia(base, exponente - 1)

# Programa Principal
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# ACTIVIDAD 4)
# Convertir un número decimal a binario usando recursión

# Definir Funciones
def decimal_a_binario(num_decimal):
    if num_decimal == 0:
        return "0" # Caso base
    elif num_decimal == 1:
        return "1" # Caso base 2
    else:
        return decimal_a_binario(num_decimal // 2) + str(num_decimal % 2)


# Programa Principal
num_decimal = int(input("Ingrese un número entero positivo: "))
if num_decimal < 0:
    print("Por favor, ingrese un número positivo.")
else:
    print(f"El número {num_decimal} en binario es: {decimal_a_binario(num_decimal)}")

# ACTIVIDAD 5)
# Verificar si una palabra es palíndroma usando recursión, sin usar [::-1] ni reversed()

# Definir Funciones
def es_palindromo(palabra, inicio=0, fin=None):
    if fin is None:
        fin = len(palabra) - 1
    if inicio >= fin:
        return True # Caso base: si los índices se cruzan, es palíndromo
    if palabra[inicio] != palabra[fin]:
        return False # Caso base: si los caracteres no coinciden, no es palíndromo
    return es_palindromo(palabra, inicio + 1, fin - 1)



# Programa Principal
palabra = input("Ingrese una palabra: ").lower()
if es_palindromo(palabra):
    print(f"VERDADERO. {palabra.capitalize()} es palíndromo.")
else:
    print(f"FALSO. {palabra.capitalize()} NO es palíndromo.")

# ACTIVIDAD 6)
# Calcular la suma de los dígitos de un número usando recursión y operaciones matemáticas

# Definir Funciones
def suma_digitos(n):
    if n < 10:  # Caso base: si es un solo dígito, devolvés ese dígito
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)  # Suma el último dígito + recursión con el resto


# Programa Principal
while True:
    num1 = input("Ingrese un número entero positivo para calcular la suma de sus dígitos: ")
    if num1.isdigit() and int(num1) > 0:
        num1 = int(num1)
        print(f"La suma de sus dígitos es {suma_digitos(num1)}.")
        break
    else:
        print("Ingrese un número válido.")

# ACTIVIDAD 7)
# Calcular el total de bloques en una pirámide con n bloques en el nivel más bajo

# Definir Funciones
def contar_bloques(n):
    if n == 1:  
        return 1 # Caso base
    else:
        return n + contar_bloques(n - 1)  # Suma los bloques del nivel actual + los del resto de la pirámide

# Programa Principal
nivel_base = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))
if nivel_base > 0:
    total = contar_bloques(nivel_base)
    print(f"Total de bloques necesarios: {total}")
else:
    print("Debe ingresar un número positivo.")

# ACTIVIDAD 8)
# Contar cuántas veces aparece un dígito en un número usando recursión

# Definir Funciones
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        contador = 1 if ultimo == digito else 0
        return contador + contar_digito(numero // 10, digito)

# Programa Principal
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a contar (0 a 9): "))

if num >= 0 and 0 <= dig <= 9:
    resultado = contar_digito(num, dig)
    print(f"El dígito {dig} aparece {resultado} veces en el número {num}.")
else:
    print("Datos inválidos. Asegurate de que el número sea positivo y el dígito esté entre 0 y 9.")
