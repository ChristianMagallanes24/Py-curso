print("Adivina si es palindromo")
ingresar_texto = input("Ingrese el Texto: ") # Ingresa el texto a comprarar
ingresar_texto = ingresar_texto.replace(" ", "").lower() # Replace remplaza los espacios " " por "" sin espacios
def comparar(): # Funcion para comparar
    polindromo = ingresar_texto[::-1] # Creo una variable que almacenara el texto ingresado pero lo transforma a invertido
    if polindromo == ingresar_texto: # Compara el texto invertido con el texto original
        print(polindromo)
        print("Es palindromo")
    else:
        print(polindromo)
        print("No es palindromo")
comparar()
        



