# Sets / grupo o conjunto - no se puede repetir y no son ordenadas

primer = {1, 2, 3, 4, 4}
print(primer)
segundo = [2, 4, 5]
segundo = set(segundo) # Crear un set en base a una lista, tambien se puede con tuple()

# print(primer | segundo) # Une los sets y siempre eliminara los valores repetidos ( operador union |)

# print(primer & segundo) # Operador Interseccion - devuelve los elementos que se encuentran en ambos set

# print(primer - segundo) # Diferencia - mostrar solamente los datos que solamente se encuentran a la izquierda

# Diferencia cimetrica