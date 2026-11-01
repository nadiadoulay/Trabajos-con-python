from tree import BinaryTree

class Nodo:
    def __init__(self, nombre, es_archivo=False):
        self.nombre = nombre
        self.es_archivo = es_archivo
        self.hijos = []
        self.izquierda = None  # Para la transformada de Knuth
        self.derecha = None    # Para la transformada de Knuth

# Crear raíz
raiz = Nodo("/")

# ===== libraries =====
lib = Nodo("libraries")
raiz.hijos.append(lib)
lib.hijos.append(Nodo("readme.txt", True))

# ===== documentos =====
docs = Nodo("documentos")
raiz.hijos.append(docs)

# libros
libros = Nodo("libros")
docs.hijos.append(libros)
libros.hijos.append(Nodo("el pequeño libro de redes.pdf", True))
libros.hijos.append(Nodo("el pequeño libro de mongo.pdf", True))
libros.hijos.append(Nodo("domine javascript.pdf", True))
libros.hijos.append(Nodo("python para todos.pdf", True))

# nodejs
nodejs = Nodo("nodejs")
docs.hijos.append(nodejs)
nodejs.hijos.append(Nodo("api-star-wars"))  # carpeta vacía
nodejs.hijos.append(Nodo("app.js", True))
nodejs.hijos.append(Nodo("package.json", True))

# ===== python-projects =====
py = Nodo("python-projects")
raiz.hijos.append(py)

# algoritmos
alg = Nodo("algoritmos")
py.hijos.append(alg)
alg.hijos.append(Nodo("sorting.py", True))
alg.hijos.append(Nodo("examples.py", True))

# apis
apis = Nodo("apis")
py.hijos.append(apis)
apis.hijos.append(Nodo("cluster.cfg", True))

# vue-flask
vue = Nodo("vue-flask")
py.hijos.append(vue)
vue.hijos.append(Nodo("app.py", True))

# ===== templates =====
templates = Nodo("templates")
raiz.hijos.append(templates)
templates.hijos.append(Nodo("logo.png", True))

# ===== static =====
raiz.hijos.append(Nodo("static"))

# ===== TRANSFORMADA DE KNUTH =====
def knuth(nodo):
    if nodo is None:
        return None
    
    if nodo.hijos:
        nodo.izquierda = knuth(nodo.hijos[0])
    
    actual = nodo.izquierda
    for hijo in nodo.hijos[1:]:
        actual.derecha = knuth(hijo)
        actual = actual.derecha
    
    return nodo

raiz = knuth(raiz)

# ===== a. INORDEN =====
def inorden(nodo):
    if nodo is None:
        return
    inorden(nodo.izquierda)
    print(nodo.nombre)
    inorden(nodo.derecha)

print("=== INORDEN ===")
inorden(raiz)

# ===== b. LISTAR /Imágenes =====
def listar_carpeta(nodo, nombre):
    if nodo is None:
        return

    if nodo.nombre == nombre and not nodo.es_archivo:
        print(f"\nContenido de /{nombre}:")
        for hijo in nodo.hijos:
            print(f"  - {hijo.nombre}")
        return

    for hijo in nodo.hijos:
        listar_carpeta(hijo, nombre)

print("\n=== LISTAR /Imágenes ===")
listar_carpeta(raiz, "Imágenes")
listar_carpeta(raiz, "libros")  # Probá con una que sí existe

# ===== c. CONTAR ARCHIVOS POR CARPETA =====
def contar_archivos(nodo):
    if nodo is None:
        return 0
    if nodo.es_archivo:
        return 1
    total = 0
    for hijo in nodo.hijos:
        total += contar_archivos(hijo)
    return total

def mostrar_archivos_por_carpeta(nodo, path=""):
    if nodo is None:
        return
    if not nodo.es_archivo:
        cantidad = contar_archivos(nodo)
        print(f"{path}/{nodo.nombre}: {cantidad} archivo(s)")
    for hijo in nodo.hijos:
        nuevo_path = f"{path}/{nodo.nombre}" if path else f"/{nodo.nombre}"
        mostrar_archivos_por_carpeta(hijo, nuevo_path)

print("\n=== ARCHIVOS POR CARPETA ===")
mostrar_archivos_por_carpeta(raiz)

# ===== d. MOSTRAR TODOS LOS ARCHIVOS =====
def mostrar_archivos(nodo, path=""):
    if nodo is None:
        return
    if nodo.es_archivo:
        print(f"📄 {path}/{nodo.nombre}")
    for hijo in nodo.hijos:
        nuevo_path = f"{path}/{nodo.nombre}" if path else f"/{nodo.nombre}"
        mostrar_archivos(hijo, nuevo_path)

print("\n=== TODOS LOS ARCHIVOS ===")
mostrar_archivos(raiz)