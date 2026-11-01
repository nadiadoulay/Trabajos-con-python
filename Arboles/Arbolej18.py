from tree import BinaryTree

arbol = BinaryTree()

reportes = [
    ["Kylo Ren", "01/09/2026", 48372615, True, "Sith Trooper"],
    ["General Hux", "01/09/2026", 72918463, False, "Imperial Stormtrooper"],
    ["Capitana Phasma", "01/09/2026", 31582749, True, "Imperial Scout Trooper"],
    ["Kylo Ren", "02/09/2026", 64139527, False, "First Order Stormtrooper"],
    ["General Hux", "02/09/2026", 85721634, True, "Imperial Death Trooper"],
    ["Capitana Phasma", "02/09/2026", 29473851, False, "Imperial Stormtrooper"],
    ["Kylo Ren", "03/09/2026", 51648273, True, "Sith Trooper"],
    ["General Hux", "03/09/2026", 37861529, False, "Imperial Scout Trooper"],
    ["Capitana Phasma", "03/09/2026", 92517436, True, "Sith Trooper"],
    ["Kylo Ren", "04/09/2026", 16384927, False, "Imperial Death Trooper"],

    ["General Hux", "04/09/2026", 74823195, True, "Imperial Stormtrooper"],
    ["Capitana Phasma", "04/09/2026", 58271643, False, "First Order Stormtrooper"],
    ["Kylo Ren", "05/09/2026", 31947582, True, "Imperial Scout Trooper"],
    ["General Hux", "05/09/2026", 86421375, False, "Sith Trooper"],
    ["Capitana Phasma", "05/09/2026", 42758196, True, "Imperial Death Trooper"],
    ["Kylo Ren", "06/09/2026", 69138425, False, "Sith Trooper"],
    ["General Hux", "06/09/2026", 23571648, True, "First Order Stormtrooper"],
    ["Capitana Phasma", "06/09/2026", 81746392, False, "Imperial Scout Trooper"],
    ["Kylo Ren", "07/09/2026", 54621983, True, "Imperial Stormtrooper"],
    ["General Hux", "07/09/2026", 97318542, False, "Imperial Death Trooper"],

    ["Capitana Phasma", "07/09/2026", 62483715, True, "Sith Trooper"],
    ["Kylo Ren", "08/09/2026", 18562947, False, "First Order Stormtrooper"],
    ["General Hux", "08/09/2026", 73146285, True, "Imperial Scout Trooper"],
    ["Capitana Phasma", "08/09/2026", 45921763, False, "Imperial Stormtrooper"],
    ["Kylo Ren", "09/09/2026", 84261397, True, "Sith Trooper"],
    ["General Hux", "09/09/2026", 31752864, False, "First Order Stormtrooper"],
    ["Capitana Phasma", "09/09/2026", 68519423, True, "Imperial Death Trooper"],
    ["Kylo Ren", "10/09/2026", 52971638, False, "Imperial Scout Trooper"],
    ["General Hux", "10/09/2026", 19463827, True, "Sith Trooper"],
    ["Capitana Phasma", "10/09/2026", 75382146, False, "Imperial Stormtrooper"],

    ["Kylo Ren", "11/09/2026", 46831592, True, "Imperial Death Trooper"],
    ["General Hux", "11/09/2026", 82194735, False, "Imperial Scout Trooper"],
    ["Capitana Phasma", "11/09/2026", 37652841, True, "Sith Trooper"],
    ["Kylo Ren", "12/09/2026", 61529473, False, "Sith Trooper"],
    ["General Hux", "12/09/2026", 94821637, True, "First Order Stormtrooper"],
    ["Capitana Phasma", "12/09/2026", 25743186, False, "Imperial Death Trooper"],
    ["Kylo Ren", "13/09/2026", 78361524, True, "Imperial Stormtrooper"],
    ["General Hux", "13/09/2026", 43281765, False, "Sith Trooper"],
    ["Capitana Phasma", "13/09/2026", 56924318, True, "Imperial Scout Trooper"],
    ["Kylo Ren", "14/09/2026", 21478563, False, "First Order Stormtrooper"],

    ["General Hux", "14/09/2026", 89643127, True, "Imperial Death Trooper"],
    ["Capitana Phasma", "14/09/2026", 34162795, False, "Sith Trooper"],
    ["Kylo Ren", "15/09/2026", 72541836, True, "Imperial Scout Trooper"],
    ["General Hux", "15/09/2026", 15382764, False, "Imperial Stormtrooper"],
    ["Capitana Phasma", "15/09/2026", 68421539, True, "First Order Stormtrooper"],
    ["Kylo Ren", "16/09/2026", 92743618, False, "Sith Trooper"],
    ["General Hux", "16/09/2026", 51827394, True, "Imperial Death Trooper"],
    ["Capitana Phasma", "16/09/2026", 76314928, False, "Imperial Scout Trooper"],
    ["Kylo Ren", "17/09/2026", 28641573, True, "Sith Trooper"],
    ["General Hux", "17/09/2026", 63972815, False, "First Order Stormtrooper"],
]

from tree import BinaryTree

arbol = BinaryTree()

for reporte in reportes:
    arbol.insert_node(reporte[2], reporte)

def contar_fallos(root):
    if root is None:
        return [0, 0, 0]

    contadores = contar_fallos(root.left)

    reporte = root.other_values

    if reporte[3]:
        if reporte[0] == "Kylo Ren":
            contadores[0] += 1
        elif reporte[0] == "General Hux":
            contadores[1] += 1
        elif reporte[0] == "Capitana Phasma":
            contadores[2] += 1

    contadores_derecha = contar_fallos(root.right)

    contadores[0] += contadores_derecha[0]
    contadores[1] += contadores_derecha[1]
    contadores[2] += contadores_derecha[2]

    return contadores

fallos = contar_fallos(arbol.root)

print("Fallos de Kylo Ren:", fallos[0])
print("Fallos de General Hux:", fallos[1])
print("Fallos de Capitana Phasma:", fallos[2])


reporte[0] == "Kylo Ren"

soldados_kylo = {}

def misiones_kylo(root):
    if root is not None:
        misiones_kylo(root.left)

        reporte = root.other_values

        if reporte[0] == "Kylo Ren":
            tipo = reporte[4]

            if tipo in soldados_kylo:
                soldados_kylo[tipo] += 1
            else:
                soldados_kylo[tipo] = 1

        misiones_kylo(root.right)

misiones_kylo(arbol.root)

for tipo, cantidad in soldados_kylo.items():
    print(tipo, cantidad)


contadores = {
    "sith": 0,
    "fallaron": 0
}

def contar_sith(root):
    if root is not None:
        contar_sith(root.left)

        reporte = root.other_values

        if reporte[4] == "Sith Trooper":
            contadores["sith"] += 1

            if reporte[3]:
                contadores["fallaron"] += 1

        contar_sith(root.right)

contar_sith(arbol.root)

print("Sith Troopers que salieron en misiones:", contadores["sith"])
print("Sith Troopers a los que les falló el blaster:", contadores["fallaron"])

fecha = input("Ingrese la fecha: ")

datos = {
    "total": 0,
    "fallaron": 0
}

def buscar_fecha(root):
    if root is not None:
        buscar_fecha(root.left)

        reporte = root.other_values

        if reporte[1] == fecha:
            print("Código:", reporte[2])

            datos["total"] += 1

            if reporte[3]:
                datos["fallaron"] += 1

        buscar_fecha(root.right)

buscar_fecha(arbol.root)

if datos["total"] > 0:
    porcentaje = datos["fallaron"] * 100 / datos["total"]
    print("Porcentaje de armas que fallaron:", porcentaje, "%")
else:
    print("No hay misiones en esa fecha.")


codigo = 75961380

nodo = arbol.search(codigo)

if nodo is not None:
    print("Blaster encontrado:")
    print(nodo.other_values)
else:
    print("El blaster no fue utilizado en ninguna misión.")


