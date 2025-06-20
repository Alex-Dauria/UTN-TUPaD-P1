# Práctico 7: Datos Complejos - Alex Dauria

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 1)
# ----------------------------------------------------------------------------------------

#Escribimos el diccionario precios_frutas inicial
precios_frutas = {"Banana" : 1200, "Ananá" : 2500, "Melón" : 3000, "Uva" : 1450}

print("Diccionario Inicial: ")
print(precios_frutas)
print("")

#Agregamos las frutas con sus precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

#Imprimimos para corroborar que se haya realizado correctamente
print("1. Agregamos frutas con precios: ")
print(precios_frutas)
print("")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 2) 
# ----------------------------------------------------------------------------------------

#Actualizamos los respectivos precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

#Imprimimos para corroborar que se haya realizado correctamente
print("2. Actualizamos precios: ")
print(precios_frutas)
print("")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 3)
# ----------------------------------------------------------------------------------------

# Creamos una lista utilizando solo las frutas (keys) de nuestro diccionario
solo_frutas = list(precios_frutas.keys())

#Imprimimos para corroborar que se haya realizado correctamente
print("3. Lista de solo frutas: ")
print(solo_frutas)
print("")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 4)
# ----------------------------------------------------------------------------------------

print("4. Crearemos una lista de contactos")
# Creamos el diccionario vacío
contactos = {}

# El usuario ingresa 5 nombres (keys) y 5 números asociados (values)
for i in range(5):
    nombre = input("Nombre de contacto: ").capitalize()
    numero = input("Número de teléfono: ")
    contactos[nombre] = numero

print("")
print("Perfecto! Lista actualizada.")
print("")
# El usuario ingresará un contacto a buscar
busqueda = input("Buscar un contacto: ").capitalize()

# Si el usuario ingresó un contacto válido, se le mostrará su número,
# si no, se emite un mensaje 
if busqueda in contactos:
    print(f"El número de {busqueda} es {contactos[busqueda]}.")
else:
    print("Contacto no encontrado.")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 5)
# ----------------------------------------------------------------------------------------

# Solicitamos la frase al usuario
frase = input("5. Escribe una frase: ")

# Creamos el set de palabras únicas que ignore mayúsculas y minúsculas y lo imprimimos
palabras_unicas = set(frase.lower().split())
print("")
print("Set de Palabras Únicas: ")
print(palabras_unicas)

# Creamos una lista con las palabras de la frase e inicializamos el diccionario
lista_frase = list(frase.lower().split())
diccionario_palabras = {}

# Recorremos la lista y agregamos al diccionario la cantidad de veces que se repite cada una
for palabra in lista_frase:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] += 1
    else:
        diccionario_palabras[palabra] = 1

# Imprimimos el diccionario
print("")
print("Diccionario con la cantidad de veces que aparece cada palabra: ")
print(diccionario_palabras)
print("")
     

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 6)
# ----------------------------------------------------------------------------------------

print("6. Alumnos y Promedios:")
print("")

# Creamos un diccionario vacío
alumnos = {}

# Pedimos los datos de 3 alumnos
for alumno in range(3):
    nombre = input("Nombre del alumno: ") 
    notas = [] 

# Pedimos las 3 notas del alumno
    for i in range(1, 4):
        nota = float(input(f"Nota {i} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("")
print("Promedios de los alumnos:")

# Recorremos el diccionario para calcular y mostrar promedios
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas) # Sumamos las notas y dividimos por la cantidad
    print(f"{nombre}: {promedio:.2f}") # Mostramos el promedio con 2 decimales

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 7)
# ----------------------------------------------------------------------------------------

print("")
print("7. Alumnos y Parciales: ")
print("")

# Sets con estudiantes que aprobaron cada parcial
parcial1 = {"Ana", "Luis", "Juan", "Marta", "Sofía"}
parcial2 = {"Juan", "Sofía", "Carlos", "Lucía", "Ana"}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:")
print(ambos)

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("")
print("Aprobaron solo uno de los dos:")
print(solo_uno)

# Estudiantes que aprobaron al menos uno (unión)
al_menos_uno = parcial1 | parcial2
print("")
print("Aprobaron al menos un parcial:")
print(al_menos_uno)
print("")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 8)
# ----------------------------------------------------------------------------------------

print("8. Productos y Stock: ")
print("")

# Diccionario con algunos productos iniciales
stock_productos = {"manzanas": 20, "bananas": 15, "peras": 10}

# Mostramos el stock inicial
print("Stock inicial:")
for producto, stock in stock_productos.items():
    print(f"{producto.capitalize()}: {stock} unidades")
print("")

# El usuario ingresa un producto a consultar o modificar
producto = input("Ingresá el nombre de un producto: ").lower()

# Verificamos si el producto ya existe en el diccionario
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]} unidades")
    print("")
# Preguntamos si quiere agregar más unidades
    agregar = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if agregar == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]} unidades")
else:
# Si no existe, preguntamos si lo quiere agregar
    print(f"{producto.capitalize()} no está en el stock.")
    nuevo = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if nuevo == "s":
        unidades = int(input("¿Cuántas unidades tiene?: "))
        stock_productos[producto] = unidades
        print(f"{producto.capitalize()} agregado con {unidades} unidades.")

# Mostramos el stock actualizado
print("")
print("Stock actualizado:")
for producto, stock in stock_productos.items():
    print(f"{producto.capitalize()}: {stock} unidades")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 9)
# ----------------------------------------------------------------------------------------

print("")
print("9. Creación de Agenda: ")
print("")

# Creamos la agenda con algunas actividades de ejemplo
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "08:00"): "Gimnasio",
    ("viernes", "20:00"): "Cena con amigos"
}

# Mostramos la agenda completa
print("AGENDA ACTUAL:")
for (dia, hora), evento in agenda.items():
    print(f"{dia.capitalize()} a las {hora} → {evento}")

print("")
print("CONSULTA DE EVENTO")

# El usuario puede consultar qué actividad hay en cierto día y hora
dia = input("Ingresá el día que querés consultar: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

# Buscamos si hay evento en esa combinación día/hora
if (dia, hora) in agenda:
    print(f"El evento agendado el {dia.capitalize()} a las {hora} es: {agenda[(dia, hora)]}")
else:
    print(f"No hay ningún evento agendado el {dia.capitalize()} a las {hora}.")

# ----------------------------------------------------------------------------------------
# ACTIVIDAD 10)
# ----------------------------------------------------------------------------------------

print("")
print("10. Países y Capitales: ")
print("")

# Diccionario original con países como claves y capitales como valores
original = {"Argentina": "Buenos Aires","Chile": "Santiago","Brasil": "Brasilia","Uruguay": "Montevideo","Paraguay": "Asunción"}

# Invertimos el diccionario: las capitales pasan a ser las claves, y los países los valores
invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

# Mostramos el diccionario invertido
print("Diccionario original:")
print(original)
print("")
print("Diccionario invertido (capitales como claves):")
print(invertido)