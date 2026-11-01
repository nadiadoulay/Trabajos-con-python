from tree import BinaryTree
from Archivo import Archivo

arbol_titulo = BinaryTree()
arbol_isbn = BinaryTree()
arbol_autor = BinaryTree()

libros = [
    ["Harry Potter y la piedra filosofal", "978-8478884452", ["J.K. Rowling"], "Salamandra", 288],
    ["Harry Potter y la cámara secreta", "978-8478884459", ["J.K. Rowling"], "Salamandra", 320],
    ["Harry Potter y el prisionero de Azkaban", "978-8478884456", ["J.K. Rowling"], "Salamandra", 384],
    ["El principito", "978-987-1138263", ["Antoine de Saint-Exupéry"], "Emecé", 96],
    ["Cien años de soledad", "978-8437604947", ["Gabriel García Márquez"], "Cátedra", 496],
    ["Don Quijote de la Mancha", "978-8420412146", ["Miguel de Cervantes"], "Alfaguara", 1056],
    ["1984", "978-0451524935", ["George Orwell"], "Signet Classics", 328],
    ["Rebelión en la granja", "978-0451526342", ["George Orwell"], "Signet Classics", 128],
    ["Orgullo y prejuicio", "978-0141439518", ["Jane Austen"], "Penguin Classics", 432],
    ["Drácula", "978-0486411095", ["Bram Stoker"], "Dover Publications", 336],
    ["Frankenstein", "978-0486282114", ["Mary Shelley"], "Dover Publications", 280],
    ["El Hobbit", "978-0261102217", ["J.R.R. Tolkien"], "HarperCollins", 310],
    ["El señor de los anillos", "978-0261102385", ["J.R.R. Tolkien"], "HarperCollins", 1216],
    ["Crónica de una muerte anunciada", "978-1400034710", ["Gabriel García Márquez"], "Vintage", 128],
    ["Rayuela", "978-8437604935", ["Julio Cortázar"], "Cátedra", 736],
    ["La sombra del viento", "978-8408172170", ["Carlos Ruiz Zafón"], "Planeta", 576],
    ["It", "978-1501142970", ["Stephen King"], "Scribner", 1138],
    ["Carrie", "978-0307743664", ["Stephen King"], "Anchor Books", 304],
    ["Los juegos del hambre", "978-0439023481", ["Suzanne Collins"], "Scholastic Press", 374],
    ["Buenos presagios", "978-0552137039", ["Neil Gaiman", "Terry Pratchett"], "Corgi Books", 432],
    ["Sistemas operativos modernos", "978-0133591620", ["Andrew S. Tanenbaum"], "Pearson", 1136],
    ["Redes de computadoras", "978-6074421204", ["Andrew S. Tanenbaum", "David J. Wetherall"], "Pearson", 960],
    ["Sistemas distribuidos", "978-0132143011", ["Andrew S. Tanenbaum", "Maarten van Steen"], "Pearson", 704],
    ["Database Systems", "978-0321197849", ["Thomas Connolly", "Carolyn Begg"], "Pearson", 1392],
    ["Database Systems: A Practical Approach", "978-1292061184", ["Thomas Connolly", "Carolyn Begg"], "Pearson", 1440],
    ["Data Mining: Concepts and Techniques", "978-0123814791", ["Jiawei Han", "Micheline Kamber", "Jian Pei"], "Morgan Kaufmann", 744],
    ["Introducción a la minería de datos", "978-8428333450", ["Pang-Ning Tan", "Michael Steinbach", "Vipin Kumar"], "Pearson", 768],
    ["Minería de datos", "978-6073209642", ["José Hernández Orallo"], "Alfaomega", 500],
    ["Introducción a los algoritmos", "978-0262046305", ["Thomas H. Cormen", "Charles E. Leiserson", "Ronald L. Rivest", "Clifford Stein"], "MIT Press", 1312],
    ["Algoritmos", "978-8426724384", ["Robert Sedgewick", "Kevin Wayne"], "Pearson", 976],
    ["Algoritmos y estructuras de datos", "978-6074380793", ["Nivio Ziviani"], "Cengage Learning", 720],
    ["Fundamentos de bases de datos", "978-8448190345", ["Abraham Silberschatz", "Henry F. Korth", "S. Sudarshan"], "McGraw-Hill", 1376],
    ["Database Management Systems", "978-0072465631", ["Raghu Ramakrishnan", "Johannes Gehrke"], "McGraw-Hill", 1065],
    ["Harry Potter y el cáliz de fuego", "978-8478886450", ["J.K. Rowling"], "Salamandra", 640],
    ["Harry Potter y la Orden del Fénix", "978-8478887426", ["J.K. Rowling"], "Salamandra", 896],
    ["Harry Potter y el misterio del príncipe", "978-8478887679", ["J.K. Rowling"], "Salamandra", 608],
    ["Harry Potter y las reliquias de la Muerte", "978-8478889284", ["J.K. Rowling"], "Salamandra", 640],
    ["Percy Jackson y el ladrón del rayo", "978-8498386266", ["Rick Riordan"], "Salamandra", 288],
    ["Percy Jackson y el mar de los monstruos", "978-8498386280", ["Rick Riordan"], "Salamandra", 288],
    ["Percy Jackson y la maldición del titán", "978-8498386273", ["Rick Riordan"], "Salamandra", 320],
    ["Percy Jackson y la batalla del laberinto", "978-8498386297", ["Rick Riordan"], "Salamandra", 384],
    ["Los 100", "978-9504967453", ["Kass Morgan"], "Alfaguara", 320],
    ["Los 100: Día 21", "978-8420483939", ["Kass Morgan"], "Alfaguara", 320],
    ["Los 100: Regreso", "978-8420483946", ["Kass Morgan"], "Alfaguara", 352],
    ["Los 100: Rebelión", "978-8420483953", ["Kass Morgan"], "Alfaguara", 368],
    ["El nombre del viento", "978-8401337208", ["Patrick Rothfuss"], "Plaza & Janés", 880],
    ["Juego de tronos", "978-8496208929", ["George R.R. Martin"], "Gigamesh", 800],
    ["Choque de reyes", "978-8496208936", ["George R.R. Martin"], "Gigamesh", 912],
    ["Festín de cuervos", "978-8496208967", ["George R.R. Martin"], "Gigamesh", 864],
    ["Dune", "978-0441172719", ["Frank Herbert"], "Ace Books", 896]
]

archivo = Archivo("libros.txt")
archivo.abrir()

for libro in libros:
    nrr=archivo.guardar(libro)

    arbol_titulo.insert_node(libro[0], nrr)
    arbol_isbn.insert_node(libro[1], nrr)
    for autor in libro[2]:
        arbol_autor.insert_node(autor, nrr)

archivo.cerrar()

isbn = input("Ingrese el ISBN del libro: ")

nodo_isbn = arbol_isbn.search(isbn)

if nodo_isbn is not None:
    archivo.abrir()
    libro = archivo.leer(nodo_isbn.other_values)
    archivo.cerrar()

    print(libro)
else:
    print("No se encontró el libro con el ISBN proporcionado.")


def buscar_autor(root, autor):
    if root is not None:
        buscar_autor(root.left, autor)

        if root.value.lower() == autor.lower():
            archivo.abrir()
            libro = archivo.leer(root.other_values)
            archivo.cerrar()
            print(libro)

        buscar_autor(root.right, autor)

autor = input("Ingrese el autor: ")
buscar_autor(arbol_autor.root, autor)

def buscar_titulo(root, texto):
    if root is not None:
        buscar_titulo(root.left, texto)

        if root.value.lower().startswith(texto.lower()):
            archivo.abrir()
            libro = archivo.leer(root.other_values)
            archivo.cerrar()
            print(libro)

        buscar_titulo(root.right, texto)

texto = input("Ingrese el comienzo del título: ")
buscar_titulo(arbol_titulo.root, texto)

def buscar_tema(root, tema):
    if root is not None:
        buscar_tema(root.left, tema)

        if tema.lower() in root.value.lower():
            archivo.abrir()
            libro = archivo.leer(root.other_values)
            archivo.cerrar()
            print(libro)

        buscar_tema(root.right, tema)

buscar_tema(arbol_titulo.root, "minería de datos")
buscar_tema(arbol_titulo.root, "algoritmos")
buscar_tema(arbol_titulo.root, "bases de datos")

print ("Libros de mas de 873 paginas:  ")
def libros_mas_873(root):
    if root is not None:
        libros_mas_873(root.left)

        archivo.abrir()
        libro = archivo.leer(root.other_values)
        archivo.cerrar()

        if libro[4] > 873:
            print(libro)

        libros_mas_873(root.right)
libros_mas_873(arbol_titulo.root)


isbn = "9789504967453"

nodo = arbol_isbn.search(isbn)

if nodo is not None:
    archivo.abrir()
    libro = archivo.leer(nodo.other_values)
    archivo.cerrar()

    print(libro)
else:
    print("Libro no encontrado")


print("Autor del libro Los 100: ")
titulo = "Los 100"

nodo = arbol_titulo.search(titulo)

if nodo is not None:
    archivo.abrir()
    libro = archivo.leer(nodo.other_values)
    archivo.cerrar()

    print("Autor:", libro[2])
else:
    print("Libro no encontrado")