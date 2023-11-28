from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from PizzaComposite.leaf import * 

class BarbacoaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        super().__init__('Pizza Barbacoa', 10)
        self.reset()

    def reset(self) -> None:
        self._pizza = Barbacoa()

    @property
    def pizza(self) -> Barbacoa:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.add('masa gruesa')

    def producir_salsa(self) -> None:
        self._pizza.add('salsa barbacoa')

    def producir_ingredientes(self) -> None:
        self._pizza.add('pollo')
        self._pizza.add('cebolla')
        self._pizza.add('maíz')

    def producir_coccion(self) -> None:
        self._pizza.add('horno de leña')

    def producir_presentacion(self) -> None:
        self._pizza.add('pizza rectangular')

    def producir_maridaje(self) -> None:
        self._pizza.add('refresco de cola')

    def producir_extras(self) -> None:
        self._pizza.add('salsa barbacoa adicional')


class Barbacoa(Leaf):

    def __init__(self) -> None:
        super().__init__('Pizza Barbacoa', 10.0)
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def display(self) -> None:
        print(f"Pizza: {', '.join(self.parts)}", end="")