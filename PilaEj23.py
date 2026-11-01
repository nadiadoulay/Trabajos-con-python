from stack import Stack

temperaturas = [20, 22, 18, 25, 27, 19, 21, 23, 24, 26,
                22, 20, 19, 18, 21, 23, 25, 27, 28, 26,
                24, 22, 20, 19, 18, 17, 21, 23, 24, 25]

pila= Stack()
pilaAux= Stack()
min_temp = None
max_temp = None
suma = 0
promedio = 0
cont_mayor_promedio = 0
cont_menor_promedio = 0

for temp in temperaturas:
    pila.push(temp)

while pila.size()>0:
    temp= pila.pop()
    if min_temp is None or temp<min_temp:
        min_temp = temp
    if max_temp is None or temp>max_temp:
        max_temp = temp
    suma += temp
    pilaAux.push(temp)



print(f"Temperatura mínima: {min_temp}")
print(f"Temperatura máxima: {max_temp}")

promedio = suma / len(temperaturas)
print(f"Temperatura promedio: {promedio:.2f}")

while pilaAux.size()>0:
    temp= pilaAux.pop()
    if temp > promedio:
        cont_mayor_promedio += 1 
    else:
        cont_menor_promedio += 1
    pila.push(temp)

print(f"Cantidad de días con temperatura mayor al promedio: {cont_mayor_promedio}")
print(f"Cantidad de días con temperatura menor al promedio: {cont_menor_promedio}")