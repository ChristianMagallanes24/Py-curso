"""
Ejercicio 1: Número par o impar
Escribe un programa que pida al usuario un número y determine si es par o impar.
    
"""

# Mi codigo

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for numero in numeros:
#     if numero % 2:
#         print(f"impar=> {numero}")
#     elif numero != 0:
#         print(f"Par {numero}")
        
        
""" 
CORRECCION:
# Ejercicio 1: Número par o impar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for numero in numeros:
    if numero % 2 == 0:
        print(f"Par => {numero}")
    else:
        print(f"Impar => {numero}")

"""


"""
Ejercicio 2: Suma de números
Crea un programa que pida al usuario ingresar dos números y muestre su suma.
"""

#Mi codigo

ingresar_numero = float(input("Ingrese el primer numero porfavor: "))
siguiente_numero = float(input("Ingrese el segundo numero porfavor: "))

def sumar():
    resultado = ingresar_numero + siguiente_numero
    print(resultado)
sumar()

