saludo = "Hola" # Variable global

def saludar():
    saludo = "Hola mundo" # Variable con alcance
    print(saludo)
    
    
def saludaJose():
    saludo = "hola jose"
    print(saludo)
    
saludar()
saludaJose()
saludar()

"""QUEDA PENDIENTE VER UN POCO MAS SOBRE EL ALCANCE DE LAS FUNCIONES"""