datos = {
    "Nombre" : "Pepe",
    "Edad" : 25,
    "feliz": True,
}

# Acceder al dict

print(datos["Edad"]) # Accede por la llave
print(datos.get("Nombre"))

del datos["Nombre"] # Elimina la llave y el valor
print(datos)
datos["Edad"] = 99 # Remplazar el valor de la llave
print(datos)

for dato in datos: # iterar los valores
    print(dato)

for dato in datos.items():
    print(dato)
    
for llave, dato in datos.items(): # Desempaquetado
    print(llave, dato)


usuarios = [
    {"id": 1, "nombre": "Jose"},
    {"id": 2, "nombre": "Pepe"},
    {"id": 3, "nombre": "Tincho"},
    {"id": 4, "nombre": "Pedro"},
]

for usuario in usuarios:
    print(usuario["nombre"])