import pickle


class Archivo:

    def __init__(self, nombre):
        self.nombre = nombre

    def abrir(self):
        self.archivo = open(self.nombre, "a+b")

    def cerrar(self):
        self.archivo.close()

    def guardar(self, registro):
        self.archivo.seek(0, 2)
        nrr = self.archivo.tell()
        pickle.dump(registro, self.archivo)
        return nrr

    def leer(self, nrr):
        self.archivo.seek(nrr)
        return pickle.load(self.archivo)

    def modificar(self, nrr, registro):
        self.archivo.seek(nrr)
        pickle.dump(registro, self.archivo)
