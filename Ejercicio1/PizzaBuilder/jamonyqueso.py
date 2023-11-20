from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod

class JamonyQuesoBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Jamonyqueso()

    @property
    def pizza(self) -> Jamonyqueso:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        self._pizza.add('masa fina')

    def producir_salsa(self) -> None:
        self._pizza.add('salsa de tomate')

    def producir_ingredientes(self) -> None:
        self._pizza.add('jamón')
        self._pizza.add('queso mozzarella')

    def producir_coccion(self) -> None:
        self._pizza.add('horno tradicional')

    def producir_presentacion(self) -> None:
        self._pizza.add('pizza circular')

    def producir_maridaje(self) -> None:
        self._pizza.add('vino blanco')

    def producir_extras(self) -> None:
        self._pizza.add('aceitunas negras')

class Jamonyqueso():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")