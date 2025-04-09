#Logica para realizar la operacion
def calculadora():
    print("Console Calculator:\n ")
    getNum = int(input("Ingrese el numero a operar: "))
    print("Elija el operador\n 1 - +\n 2 - - \n 3 - * \n 4 - /")
    getOperador = int(input("Ingrese la opcion: "))
    getNum2 = int(input("Ingrese el siguiente numero: "))
    
    if getOperador == 1:
        resultado = getNum + getNum2
        print(resultado)
    elif getOperador == 2:
        resultado = getNum - getNum2
        print(resultado)
    elif getOperador == 3:
        resultado = getNum * getNum2
        print(resultado)
    elif getOperador == 4:
        resultado = getNum / getNum2
        print(resultado)  
    else:
        print("Ingrese una opcion valida")  
calculadora()