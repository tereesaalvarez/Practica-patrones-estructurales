from PizzaComposite.component import *
from PizzaComposite.leaf import *

class Composite(Component):

    def __init__(self, name: str) -> None:
        self.name = name
        self.children: list[Component] = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def remove(self, component: Component) -> None:
        self.children.remove(component)

    def get_price(self) -> float:
        total_price = 0
        for child in self.children:
            total_price += child.get_price()
        return total_price

    def display(self) -> None:
        print(f"{self.name}:")
        for child in self.children:
            child.display()