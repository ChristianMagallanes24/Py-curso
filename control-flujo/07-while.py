numero = 1

while numero <= 10: # Bucle con condición
    print(numero)
    numero += 1

comando = "exit"
while True: # Bucle infinito
    comando = input("Ingrese un comando: ")
    if comando.lower() == "exit":
        print(comando)
        break
    