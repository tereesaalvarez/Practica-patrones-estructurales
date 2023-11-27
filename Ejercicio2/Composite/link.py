from Composite.leaf import *

class Link(Leaf):
    def __init__(self, nombre):
        self.nombre = nombre
        self.link = None

    def operation(self):
        return f"Nombre link: {self.name}, link: {self.link}"
    