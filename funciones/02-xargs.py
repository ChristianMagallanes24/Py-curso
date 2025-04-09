# Xargs
def suma(*numeros): #Convierte los parametros en iterables
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)
        
suma(2, 5)
suma(2, 5, 7)