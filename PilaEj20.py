from stack import Stack

movimientos = [
    (2, "norte"),
    (3, "oeste"),
    (4, "noreste"),
    (1, "oeste")
]

pila=Stack()

opuestos = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste"
}

for movimiento in movimientos:
    pila.push(movimiento)

while pila.size()>0:
    pasos, direccion = pila.pop()
    direccion_opuesta = opuestos[direccion]
    print(f"Volver: {pasos} pasos hacia {direccion_opuesta}")

