#Kwargs

def get_product(**datos):
    print(datos["name"], datos["desc"]) #Acceder a dicho parametro
    
get_product(id="id",
            name="pc",
            #param / argumento
            desc="esto es una pc")