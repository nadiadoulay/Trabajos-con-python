from list_ import List

l = List()

alumnos = [
    ["Juan", "Lopez", 1001,
        [
            ["Algoritmos y estructuras de datos", 8, "10/03/2020"],
            ["Base de datos", 6, "15/06/2020"],
            ["Programación", 9, "20/09/2020"]
        ]
    ],

    ["Ana", "Martinez", 1002,
        [
            ["Algoritmos y estructuras de datos", 10, "12/03/2020"],
            ["Base de datos", 9, "18/06/2020"],
            ["Programación", 10, "22/09/2020"]
        ]
    ],

    ["Lucas", "Luna", 1003,
        [
            ["Algoritmos y estructuras de datos", 4, "08/03/2020"],
            ["Base de datos", 5, "12/06/2020"],
            ["Programación", 7, "18/09/2020"]
        ]
    ],

    ["María", "López", 1004,
        [
            ["Algoritmos y estructuras de datos", 7, "11/03/2020"],
            ["Base de datos", 8, "17/06/2020"],
            ["Programación", 9, "25/09/2020"]
        ]
    ],

    ["Sofía", "Ledesma", 1005,
        [
            ["Algoritmos y estructuras de datos", 10, "09/03/2020"],
            ["Base de datos", 10, "14/06/2020"],
            ["Programación", 10, "19/09/2020"]
        ]
    ],

    ["Martín", "Gomez", 1006,
        [
            ["Algoritmos y estructuras de datos", 3, "13/03/2020"],
            ["Base de datos", 4, "16/06/2020"],
            ["Programación", 6, "24/09/2020"]
        ]
    ]
]

for alumno in alumnos:
    l.append(alumno)

l.sort(key=lambda alumno: alumno[1])

print("Alumnos ordenados por apellido:")
for alumno in l:
    print(f"{alumno[0]} {alumno[1]} - Legajo: {alumno[2]}")

for alumno in l:
    desaprobo = False
    for parcial in alumno[3]:
        if parcial[1] < 6:
            desaprobo = True
    if desaprobo==False:
         print (alumno[0], alumno[1], "aprobó todas las materias")

for alumno in l:
    suma=0
    for parcial in alumno[3]:
        suma+=parcial[1]
    promedio=suma/len(alumno[3])
    if promedio>8.89:  
        print (alumno[0], alumno[1], "promedio:", promedio)

for alumno in l:
    if alumno[1][0]=="L":
        print ("Alumnos que comienzan con L:", alumno)

for alumno in l:
    suma=0
    for parcial in alumno[3]:
        suma+=parcial[1]
    promedio=suma/len(alumno[3])
    print (alumno[0], alumno[1], "promedio:", promedio)

for alumno in l:
    for parcial in alumno[3]:
        if parcial[0]=="Algoritmos y estructuras de datos":
            print (alumno[0], alumno[1], "cursa Algoritmos y estructuras de datos")

nombre = input("Ingrese el nombre del alumno del que desea conocer el promedio: ")

for alumno in l:
    if alumno[0] == nombre:
        suma=0
        for parcial in alumno[3]:
            suma+=parcial[1]
        promedio=suma/len(alumno[3])
        print (alumno[0], alumno[1], "promedio:", promedio)

aprobadosBDD=0
desaprobadosBDD=0

for alumno in l:
    for parcial in alumno[3]:
        if parcial[0]=="Base de datos":
            if parcial[1]>=7:
                aprobadosBDD+=1
            else:
                desaprobadosBDD+=1

print ("Cantidad de alumnos que aprobaron Base de datos:", aprobadosBDD)
print ("Cantidad de alumnos que desaprobaron Base de datos:", desaprobadosBDD)

for alumno in l:
    for parcial in alumno[3]:
        if "2020" in parcial[2]:
            print (alumno[0], alumno[1], "cursó", parcial[0], "en el año 2020")