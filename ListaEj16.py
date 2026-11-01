from list_ import List

# Inicialización de variables
tiempo_acumulado = 0
tiempo_promedio = 0
contador = 0
costo_total = 0

# Lista de datos de actividades
actividades = [
    {
        "costo": 5000,
        "tiempo": 10,
        "inicio": "01/06/2025",
        "fin_estimada": "11/06/2025",
        "fin_efectiva": "10/06/2025",
        "persona": "Juan"
    },
    {
        "costo": 8000,
        "tiempo": 15,
        "inicio": "05/06/2025",
        "fin_estimada": "20/06/2025",
        "fin_efectiva": "25/06/2025",
        "persona": "Ana"
    },
    {
        "costo": 3000,
        "tiempo": 5,
        "inicio": "10/06/2025",
        "fin_estimada": "15/06/2025",
        "fin_efectiva": "15/06/2025",
        "persona": "Juan"
    },
    {
        "costo": 12000,
        "tiempo": 20,
        "inicio": "12/06/2025",
        "fin_estimada": "02/07/2025",
        "fin_efectiva": "30/06/2025",
        "persona": "Pedro"
    },
    {
        "costo": 6500,
        "tiempo": 12,
        "inicio": "15/06/2025",
        "fin_estimada": "27/06/2025",
        "fin_efectiva": "29/06/2025",
        "persona": "María"
    },
    {
        "costo": 4500,
        "tiempo": 8,
        "inicio": "18/06/2025",
        "fin_estimada": "26/06/2025",
        "fin_efectiva": "24/06/2025",
        "persona": "Ana"
    },
    {
        "costo": 9000,
        "tiempo": 18,
        "inicio": "20/06/2025",
        "fin_estimada": "08/07/2025",
        "fin_efectiva": "12/07/2025",
        "persona": "Lucas"
    },
    {
        "costo": 5500,
        "tiempo": 9,
        "inicio": "22/06/2025",
        "fin_estimada": "01/07/2025",
        "fin_efectiva": "01/07/2025",
        "persona": "Pedro"
    },
    {
        "costo": 7000,
        "tiempo": 14,
        "inicio": "25/06/2025",
        "fin_estimada": "09/07/2025",
        "fin_efectiva": "07/07/2025",
        "persona": "María"
    },
    {
        "costo": 11000,
        "tiempo": 22,
        "inicio": "28/06/2025",
        "fin_estimada": "20/07/2025",
        "fin_efectiva": "23/07/2025",
        "persona": "Juan"
    }

    {
    "costo": 9000,
    "tiempo": 18,
    "inicio": "20/06/2025",
    "fin_estimada": "08/07/2025",
    "fin_efectiva": None,
    "persona": "Lucas"
}
]

# Definición de la clase Actividad
class Actividad:
    def __init__(self, costo, tiempo, inicio, fin_estimada, fin_efectiva, persona):
        self.costo = costo
        self.tiempo = tiempo
        self.inicio = inicio
        self.fin_estimada = fin_estimada
        self.fin_efectiva = fin_efectiva
        self.persona = persona

    def __str__(self):
        return f"{self.persona} - ${self.costo} - {self.tiempo} días"

# Función de criterio para la lista estructurada
def by_persona(item):
    return item.persona

# Configuración de la estructura de datos personalizada
lista_actividades = List()
lista_actividades.add_criterion('persona', by_persona)

# Carga de objetos Actividad en la lista
for act in actividades:
    lista_actividades.append(
        Actividad(
            act['costo'],
            act['tiempo'],
            act['inicio'],
            act['fin_estimada'],
            act['fin_efectiva'],
            act['persona']
        )
    )

# Mostrar la lista
lista_actividades.show()

# Cálculo del promedio de tiempo de las actividades
for act in lista_actividades:
    tiempo_acumulado += act.tiempo
    contador += 1

tiempo_promedio = tiempo_acumulado / contador

print(f"Tiempo promedio de todas las actividades: {tiempo_promedio:.2f} días")

#Costo total de todas las actividades
for act in lista_actividades:
    costo_total += act.costo

print(f"Costo total de todas las actividades: ${costo_total}")

persona_buscada= input("Ingrese la persona de la cual desea conocer sus actividades: ")

for act in lista_actividades:
    if act.persona == persona_buscada:
        print(act)

desde = input("Ingrese fecha desde: ")
hasta = input("Ingrese fecha hasta: ")

for act in lista_actividades:
    if desde <= act.inicio <= hasta:
        print(act)

print("Tareas finalizadas en tiempo:")

for act in lista_actividades:
    if act.fin_efectiva <= act.fin_estimada:
        print(act)

print("Tareas finalizadas fuera de tiempo:")

for act in lista_actividades:
    if act.fin_efectiva > act.fin_estimada:
        print(act)

persona_act_pendientes = input("Ingrese una persona de la cual se quiera saber cuantas actividades pendientes tienen: ")

pendientes = 0

for act in lista_actividades:
    if act.persona == persona_act_pendientes and act.fin_efectiva is None:
        pendientes += 1

print(f"{persona_act_pendientes} tiene {pendientes} tareas pendientes")

