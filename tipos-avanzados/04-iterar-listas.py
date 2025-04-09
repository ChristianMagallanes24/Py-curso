mascotas = ["Pepe", "Pedro", "Lola"]

for mascota in enumerate(mascotas): # Itera y devuelve el indice / Devuelve tupla
    print(mascota[0]) # Devuelve los indices
    print(mascota[0]) # Devuelve los valores
    
primero, segundo = [1, 2]
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)