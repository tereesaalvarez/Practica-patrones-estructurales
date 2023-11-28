from PizzaComposite.composite import *

class Menu(Composite):

    def __init__(self, name: str) -> None:
        super().__init__(name)