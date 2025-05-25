# Práctico 5.1: Listas - Alex Dauria

# ACTIVIDAD 1)

# Creamos una lista, utilizando el método range, mostrando los múltiplos de 4. Comenzamos con el 4, que se incluye, y el stop es 101, ya que ese no se incluiría
multiplos_de_4= list(range(4, 101, 4))
print(multiplos_de_4)

# ACTIVIDAD 2)

# Creamos una lista con 5 elementos
lista_5_elementos= ["Hola", 2, "Mundo", "Hola Mundo!", 10]
# Imprimimos el anteúltimo accediendo al final de la lista con los índices negativos
print(lista_5_elementos[-2])

# ACTIVIDAD 3)

# Creamos la lista vacía
lista_vacia  = []
lista_vacia.append("Agrego")
lista_vacia.append("tres")
lista_vacia.append("palabras")
# Imprimimos el resultado actualizado
print(lista_vacia)

# ACTIVIDAD 4)

animales = ["perro","gato", "conejo", "pez"]
# Reemplazamos el segundo valor
animales[1] = "loro"
# Reemplazamos el último valor
animales[-1] = "oso"
# Imprimimos el resultado actualizado
print(animales)

# ACTIVIDAD 5)

# El programa mencionado crea una lista con números en la primera línea, luego elimina al de mayor valor
# (en este caso 22), e imprime la lista actualizada

# ACTIVIDAD 6)

# Creamos la lista, incluyendo el 30
lista_10al30 = list(range(10, 31, 5))
# Imprimimos los 2 primeros valores
print(lista_10al30[0:2])

# ACTIVIDAD 7) 

autos = ["sedan", "polo", "suran", "gol"]
# Accedemos a los indices deseados y los reemplazamos por otros dos
autos[1:3] = ["clio", "mercedes"]
# Imprimimos el resultado
print(autos)

# ACTIVIDAD 8)

# Creamos la lista vacía
dobles = []
# Agregamos el doble de 5, 10 y 15
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
# Imprimimos el resultado
print(dobles)

# ACTIVIDAD 9)

# Lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Agregamos jugo al tercer cliente
compras[2].append("jugo")
# Reemplazamos fideos por tallarines en el segundo cliente
compras[1][1] = "tallarines"
# Eliminamos pan del primer cliente
compras[0].remove("pan")
# Imprimimos resultado actualizado
print(compras)

# ACTIVIDAD 10)

# Creamos la lista anidada con los datos recibidos
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

#Imprimimos el resultado
print(lista_anidada)

