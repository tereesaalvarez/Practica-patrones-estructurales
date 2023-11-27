from leaf import *

class Link(Leaf):
    def __init__(self, name):
        self.name = name
        self.link = None

    def operation(self):
        return f"Nombre link: {self.name}, link: {self.link}"
    