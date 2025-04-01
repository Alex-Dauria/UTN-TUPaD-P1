# Ejercicio 1

# Pedimos la edad al usuario
edad = int(input("Ingrese su edad por favor: "))

#Si el usuario es mayor de 18 (incluimos los 18)
if edad >= 18: 
# Imprimimos el mensaje
    print("Es mayor de edad") 

# Ejercicio 2

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
# Si la nota no es mayor o igual a 6:
else: 
# Imprimimos este mensaje
    print("Desaprobado") 

# Ejercicio 3

num = int(input("Ingrese un número par: "))
# Si el resto de la división del numero por 2 es 0 (es par)
if num % 2 == 0: 
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# Ejercicio 4

edad2 = int(input("Ingrese su edad: "))
# Agregamos las opciones dependiendo de la edad
if edad2 < 12:
    print("Usted es un niño/a")
# Si no se cumple que sea menor de 12, escribimos otro rango de edades
elif edad2 >= 12 and edad2 < 18:
    print("Usted es un adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Usted es un adulto/a joven")

# Si ninguna de las opciones anteriores se cumple:
else:
    print("Usted es un adulto/a")

# Ejercicio 5

contra = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

# Utilizamos la funcion len() que toma la cantidad de caracteres de la palabra y ponemos los parámetros deseados
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")

# Si no se cumple la cantidad de caracteres, pedimos que se ingrese una contraseña válida
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6

# Importamos las bibliotecas necesarias para que el codigo funcione
from statistics import mode, median, mean
import random

# Generamos una lista de 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Definimos en qué se basa cada sesgo e imprimimos la conclusión
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo o a la derecha")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo o a la izquierda")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")

# Ejercicio 7

# Le pedimos una frase o palabra al usuario
frase = input("Ingrese una frase o palabra: ")

# Localizamos la ultima letra o caracter de la misma y la convertimos a minúscula, para que en caso de que el usuario escriba en mayúscula, el código funcione igualmente
ult = frase[-1].lower()

# Si termina en vocal, agregamos un signo de exclamación al final de la frase y la imprimimos en pantalla
if ult == "a" or ult == "e" or ult == "i" or ult == "o" or ult == "u":
    print(f"{frase}!")
# Si no lo es, simplemente escribimos la frase tal cual
else:
    print(frase)

# Ejercicio 8

nombre = input("Ingrese su nombre: ")

#Le damos las opciones al usuario, escribimos una debajo de la otra para mayor legibilidad
numb = int(input("Ingrese:\n1: Si quiere su nombre en mayúsculas\n2: Si quiere su nombre en minúsculas\n3: Si quiere su nombre con la primera letra mayúscula."))
# Usamos el upper() para escribir en mayúsculas
if numb == 1:
    nombre = nombre.upper()
    print(nombre)
elif numb == 2:
# Utilizamos lower() para escribir en minúsculas
    nombre = nombre.lower()
    print(nombre)
elif numb == 3:
# Utilizamos title() para escribir la primer letra en mayúscula de cada palabra y las demás en minúsculas
    nombre = nombre.title()
    print(nombre)
# Dejamos una opción en caso de que el usuario no escriba ninguno de los números deseados
else:
    print("Ingrese un número correcto.")

# Ejercicio 9

# Pedimos al usuario que ingrese la magnitud, utilizamos float ya que suelen ser decimales
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Agrupamos cada opción e imprimos en pantalla cada caso con su explicación
if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:
    print("Extremo (puede causar graves daños a gran escala).")

# Ejercicio 10

# Le pedimos al usuario los datos hemisferio, dia y mes para determinar la estación
hemisferio = input("En qué hemisferio te encuentras? Escribir N o S: ").lower()
mes = int(input("En qué mes? Escribir en números: "))
dia = int(input("Qué día es?: "))

# Empezamos con los casos del Norte
if hemisferio == "n":
# Desde el 21 de Diciembre hasta el 20 de Marzo (incluidos)
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Se encuentra en Invierno")
# Desde el 21 de Marzo hasta el 20 de Junio (incluidos)
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Se encuentra en Primavera")
# Desde el 21 de Junio hasta el 20 de Septiembre (incluidos)
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Se encuentra en Verano")
# Todos los casos restantes, es decir, desde el 21 de Septiembre hasta el 20 de Diciembre (incluidos)
    else:
        print("Se encuentra en Otoño")

# Seguimos con los casos del Sur
elif hemisferio == "s":
# Desde el 21 de Diciembre hasta el 20 de Marzo (incluidos)
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
        print("Se encuentra en Verano")
# Desde el 21 de Marzo hasta el 20 de Junio (incluidos)
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
        print("Se encuentra en Otoño")
# Desde el 21 de Junio hasta el 20 de Septiembre (incluidos)
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
        print("Se encuentra en Invierno")
# Todos los casos restantes, es decir, desde el 21 de Septiembre hasta el 20 de Diciembre (incluidos)
    else:
        print("Se encuentra en Primavera")

# En caso de que el usuario no haya escrito S ni N, le pedimos que ingrese el dato correctamente
else:
    print("Por favor ingrese 'N' para el hemisferio norte o 'S' para el hemisferio sur.")


