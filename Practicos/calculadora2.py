print("Bienvenido a la calculadora")
try:
    # Solicitar el primer número
    ingresar = float(input("Ingrese el primer número: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

# Bucle principal
while True:
    # Solicitar el operador
    operador = input("Ingrese el operador (suma, resta, div, multi) o 'Salir' para terminar: ").lower()

    if operador in ["salir", "exit"]:
        print("Saliendo del programa. ¡Adiós!")
        break

    # Validar el operador
    if operador not in ["suma", "resta", "div", "multi"]:
        print("Operador no válido. Intente nuevamente.")
        continue

    try:
        # Solicitar el siguiente número
        siguiente_numero = float(input("Ingrese el siguiente número: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    # Realizar la operación correspondiente
    if operador == "suma":
        ingresar += siguiente_numero
    elif operador == "resta":
        ingresar -= siguiente_numero
    elif operador == "div":
        if siguiente_numero == 0:
            print("No se puede dividir entre 0. Intente nuevamente.")
            continue
        ingresar /= siguiente_numero
    elif operador == "multi":
        ingresar *= siguiente_numero

    # Mostrar el resultado
    print(f"El resultado actual es: {ingresar}")

nombre = ""

while True:
    if not nombre:
        nombre = input("Porfavor ingrese su nombre ")
        break
    
   