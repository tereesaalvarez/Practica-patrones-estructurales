from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod


class BarbacoaBuilder(PizzaBuilder):

    def __init__(self) -> None:
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


class Barbacoa():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")