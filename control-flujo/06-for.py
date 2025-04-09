numeros = [1,2,3,4,5,6,7,8,9,9]

buscar = input("Ingrese el numero que desea encontrar: ")
buscar = int(buscar)
for numero in numeros:
    if buscar == numero:
        print(f"El numero {numero} se encontro")
        break
else:
    print("no se encontro")
        

    
    