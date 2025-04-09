mascotas = ["Pepe", "Pepe", "Pedro", "Lola"]

mascotas.insert(1, "Jose") # Agrega el elemento a partir del indice
print(mascotas)

mascotas.append("Chucha") # Agrega el elemento al final
print(mascotas)

mascotas.remove("Lola") # Eliminar el elemento / si esta repetido solo elimina el primero
print(mascotas)

mascotas.pop() # ELimina el ultimo elemento
mascotas.pop(1) # ELimina el elemento segun el indice

del mascotas[0] # Elimina el elemento por el indice

mascotas.clear() # Elimina todos los elementos de la lista