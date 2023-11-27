from Composite.leaf import *

class Documento(Leaf):
    def __init__(self, nombre, tipo, tamaño):
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño

    def operation(self):
        return f"Nombre documento: {self.nombre}, tipo: {self.tipo} y tamaño: {self.tamaño}"