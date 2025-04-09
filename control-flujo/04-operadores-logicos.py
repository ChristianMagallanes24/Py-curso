# and, or, not
# and se deven cumplir ambas condiciones
# or se debe cumplir solo una condicion para dar true
# not es la negacion

edad = 18
gasolina = False
encendido = True

if  18 <= edad >= 18:
    print("Es mayor")
else:
    print("Es menor de 18")
    
if edad <= 18 and gasolina == True and encendido == True:
    print("Usted es mayor de y edad y\n puede manejar el cehiculo")
else:
    print("una de todas las condiciones no se cumple entonces usted no puede manejar el vehiculo")
    