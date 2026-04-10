mochila = ["comida", "mapa", "sable", "botella"]

def usar_fuerza(mochila):
    if len(mochila)==0:
        return False,0
    elif mochila[0]=="sable":
        return True,1
    else:
        encontrado, cantidad = usar_fuerza(mochila[1:])
        return encontrado, cantidad + 1
    
encontro, objetos = usar_fuerza(mochila)

print("¿Encontró sable?", encontro)
print("Objetos revisados:", objetos)

    
