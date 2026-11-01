def caracter (texto:str) -> str:
    if len(texto)==1:
        return texto
    else:
        return caracter(texto[1:])+texto[0]

print(caracter("hola"))
