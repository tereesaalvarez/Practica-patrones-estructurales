from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod
from PizzaComposite.leaf import * 


class VegetarianaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        super().__init__('Pizza Vegetariana', 10)
        self.reset()

    def reset(self) -> None:
        self._pizza = Vegetariana()

    @property
    def pizza(self) -> Vegetariana:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.add('masa fina')

    def producir_salsa(self) -> None:
        self._pizza.add('salsa de tomate')

    def producir_ingredientes(self) -> None:
        self._pizza.add('tomate')
        self._pizza.add('pimientos')
        self._pizza.add('cebolla')
        self._pizza.add('aceitunas negras')
        self._pizza.add('champiñones')

    def producir_coccion(self) -> None:
        self._pizza.add('horno tradicional')

    def producir_presentacion(self) -> None:
        self._pizza.add('pizza circular')

    def producir_maridaje(self) -> None:
        self._pizza.add('vino blanco')

    def producir_extras(self) -> None:
        self._pizza.add('albahaca fresca')
        self._pizza.add('queso parmesano')

class Vegetariana(Leaf):

    def __init__(self) -> None:
        super().__init__('Pizza Vegetariana', 10.0)
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def display(self) -> None:
        print(f"Pizza: {', '.join(self.parts)}", end="")