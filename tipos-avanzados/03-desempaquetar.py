numeros = [1, 2, 3]

# Mala practica
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# Buena practica
primero, segundo, tercero = numeros
primero, *otros = numeros # Obtener el primer elemento
primero, segundo, *otros = numeros # Obtener el segundo
print(primero, segundo, otros)