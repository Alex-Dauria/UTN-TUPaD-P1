# // EJERCICIO 1

#Utilizamos un ciclo for, que automáticamente va de 1 en 1 y empieza en 0. Ponemos 101 como final ya que al llegar a ese número ya no se repite
for i in range(101):
    print(i)

# // EJERCICIO 2

#Pedimos al usuario que ingrese un número
num = int(input("Escribe un número entero: "))

#Luego con la funcion len() calculamos el largo. Transformamos a string ya que la función no funciona con enteros.
digitos = len(str(num))

#Imprimimos la respuesta
print(f"{num} tiene {digitos} dígitos.")

# // EJERCICIO 3

#Le pedimos 2 valores al usuario
valor1 = int(input("Escribe un número: "))
valor2 = int(input("Escribe un segundo número: "))

#Inicializamos la suma
suma = 0

#Si el primer valor ingresado es menor, empezamos a contar desde el mismo, hasta el valor2
if valor1 < valor2:
    for i in range(valor1 + 1, valor2):
        suma += i

#Caso contrario, empezamos a contar desde el segundo valor
else:
    for i in range(valor2 + 1, valor1):
        suma += i
print(f"La suma de todos los números enteros entre {valor1} y {valor2} da {suma}")

# // EJERCICIO 4

#Inicializamos los valores que necesitaremos
suma2 = 0

#El valor NO puede ser 0, ya que en ese caso no funcionaría el ciclo while
numUsuario = 1

#Determinamos que al usuario escribir 0, el ciclo termina
while numUsuario != 0:
    numUsuario = int(input("Ingrese el número a sumar: "))

#A la variante suma2, le sumamos lo que ingrese el usuario
    suma2 += numUsuario

#Imprimimos en resultado en consola
print(f"La suma de todos los números ingresados da {suma2}.")

# // EJERCICIO 5

#Primero importamos la libreria random para acceder a sus funciones para obtener el número aleatorio
import random

#Inicializamos el número y establecemos los parámetros
numeroAleatorio = random.randint(0, 9)

#Le pedimos al usuario que ingrese un número y e inicializamos el contador de intentos en 1
numUsuario = int(input("Adivina el número del 0 al 9: "))
intentos = 1

#Si el usuario no ingresa un número válido como primer número el juego se detiene y emitimos un mensaje avisandole al usuario
if 0 <= numUsuario <= 9:

#Mientras que el número no sea adivinado:
    while numUsuario != numeroAleatorio:

#Emitimos un mensaje al usuario diciendole que el número no fue adivinado y le pedimos un nuevo número
        numUsuario = int(input("INCORRECTO! Intenta nuevamente: "))
#Sumamos 1 intento cada vez que esto ocurra
        intentos += 1

#Una vez que el usuario adivine el número, emitimos un mensaje diciendo cuántos aciertos le tomó
    print(f"MUY BIEN! Te tomó {intentos} intentos acertar este número.")
else:
    print("El número a adivinar es entre 0 y 9.")

# // EJERCICIO 6

#Realizamos un ciclo for que comience en 100, llegue a 0, con paso en -2 
for x in range(100, -1, -2):

#Imprimimos cada número
    print(x)

# // EJERCICIO 7

#Inicializamos la suma
suma3 = 0

#Pedimos el número al usuario
nUsuario = int(input("Ingrese un número: "))

#Si el número es mayor a 0, sumamos con Paso 1
if nUsuario >= 0:
    for nn in range(0, nUsuario):
        suma3 += nn

#Si el número es negativo, sumamos con Paso -1
else:
    for nn in range(0, nUsuario, -1):
        suma3 += nn

#Imprimimos el resultado
print(f"La suma de todos los números entre 0 y {nUsuario} da {suma3}")

# // EJERCICIO 8

#Inicializamos todas las variables que necesitaremos
pares = impares = positivos = negativos = 0

#Utilizamos un ciclo for del 1 al 100 ya que queremos que el usuario ingrese 100 números
for ii in range(1, 101):

#Le pedimos al usuario un número
    numeroUsuario2 = int(input(f"Número {ii}: "))

#Si es par, el contador de pares aumenta en 1
    if numeroUsuario2 % 2 == 0:
        pares += 1

#Si no (impar), el de impares aumenta en 1
    else:
        impares += 1

#Si el número es mayor a 0, el contador de positivos aumenta
    if numeroUsuario2 > 0:
        positivos += 1

#Si es menor a 0, el de negativos aumenta
    elif numeroUsuario2 < 0:
        negativos += 1

#Imprimimos los resultados uno debajo del otro para mayor legibilidad
print(f"Números Pares: {pares}.\nNúmeros Impares: {impares}.\nNúmeros Positivos: {positivos}.\nNúmeros Negativos: {negativos}.")

# // EJERCICIO 9

#Inicializamos la variable suma4
suma4 = 0

#Hacemos un ciclo for que permita al usuario ingresar 100 números
for iii in range (1,101):
    numeroUsuario3 = int(input(f"Número {iii}: "))

#En cada vuelta sumamos a la variable suma lo que el usuario ingrese
    suma4 += numeroUsuario3

#Calculamos la media, como son 100 valores, dividimos la suma por 100
media = suma4 / 100

#Imprimimos el resultado
print(f"La media de los valores ingresados es de {media}.")

# // EJERCICIO 10

#Le pedimos al usuario un número en forma de string
numeroUsuario4 = input("Ingrese un número: ")

#Hacemos un ciclo for que vaya desde la cantidad de caractéres hasta -1 con Paso -1
#Para que recorra de final a principio el número escrito
for iiii in range(len(numeroUsuario4) - 1, -1, -1):

# Imprimimos cada carácter al revés sin salto de línea 
    print(numeroUsuario4[iiii], end="") #Agregamos un end="" para que no salte de linea

## Alex Dauria ##