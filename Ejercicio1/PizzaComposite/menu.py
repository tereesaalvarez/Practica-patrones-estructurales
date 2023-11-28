from PizzaComposite.composite import *

class Menu(Composite):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def calcular_precio_total(self) -> float:
        total_price = 0
        for child in self.children:
            total_price += child.get_price()
        return total_price

    def mostrar_informacion(self) -> None:
        print(f"{self.name}:")
        for child in self.children:
            child.display()