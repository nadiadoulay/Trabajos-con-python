from stack import Stack

texto = input("Ingrese un párrafo que termine en punto: ")

pilaVocales = Stack()
pilaConsonantes = Stack()
pilaOtros = Stack()
const_vocales = "aeiouAEIOU"
C_consonantes=0
C_vocales=0
C_otros=0
espacios=0
total = len(texto)
num= "1234567890"
C_num=0
pilaAuxConsonantes = Stack()

for caracter in texto:
    if caracter.isalpha():
        if caracter in const_vocales:
            pilaVocales.push(caracter)
            C_vocales += 1
        else:
            pilaConsonantes.push(caracter)
            C_consonantes += 1
    else:
        pilaOtros.push(caracter)
        C_otros += 1
        if caracter == " ":
            espacios += 1
        if caracter in num:
            C_num += 1




print(f"Cantidad de vocales: {C_vocales}")
print(f"Cantidad de consonantes: {C_consonantes}")
print(f"Cantidad de otros caracteres: {C_otros}")
print(f"Cantidad de espacios: {espacios}")



porcentaje_vocales = (C_vocales / total) * 100
print(f"Porcentaje de vocales: {porcentaje_vocales:.2f}%")

print(f"Cantidad de números: {C_num}")

if C_vocales == C_otros:
    print("La cantidad de vocales es igual a la cantidad de otros caracteres.")
elif C_vocales > C_otros:
    print("La cantidad de vocales es mayor que la cantidad de otros caracteres.")
else:
    print("La cantidad de vocales es menor que la cantidad de otros caracteres.")


hay_z = False

while pilaConsonantes.size() > 0:
    aux = pilaConsonantes.pop()

    if aux.lower() == "z":
        hay_z = True

    pilaAuxConsonantes.push(aux)

if hay_z:
    print("La letra 'z' se encuentra en el texto.")
else:
    print("La letra 'z' NO se encuentra en el texto.")


while pilaAuxConsonantes.size() > 0:
    pilaConsonantes.push(pilaAuxConsonantes.pop())
