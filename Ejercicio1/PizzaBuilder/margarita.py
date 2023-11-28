from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod
from PizzaComposite.leaf import * 


class MargaritaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        super().__init__('Pizza Margarita', 10)
        self.reset()

    def reset(self) -> None:
        self._pizza = Margarita()

    @property
    def pizza(self) -> Margarita:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.add('masa fina')

    def producir_salsa(self) -> None:
        self._pizza.add('salsa de tomate')

    def producir_ingredientes(self) -> None:
        self._pizza.add('mozzarella, albahaca')

    def producir_coccion(self) -> None:
        self._pizza.add('horno tradicional')

    def producir_presentacion(self) -> None:
        self._pizza.add('pizza circular')

    def producir_maridaje(self) -> None:
        self._pizza.add('cerveza rubia')

    def producir_extras(self) -> None:
        self._pizza.add('trufa')


class Margarita(Leaf):

    def __init__(self) -> None:
        super().__init__('Pizza Margarita', 10.0)
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def display(self) -> None:
        print(f"Pizza: {', '.join(self.parts)}", end="")