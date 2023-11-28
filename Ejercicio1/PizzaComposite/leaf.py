
from PizzaComposite.component import *

class Leaf(Component):

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def display(self) -> None:
        print(f"{self.name}: ${self.price}")