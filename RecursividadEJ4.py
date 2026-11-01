def potencia (b,e: int)-> int:
    if e ==0:
        return 1
    else:
        return b * potencia (b,e-1)

print (potencia (2,3))