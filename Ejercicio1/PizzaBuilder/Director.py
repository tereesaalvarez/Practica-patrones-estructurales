from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> PizzaBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def build_full_featured_product(self) -> None:
        self.builder.producir_masa()
        self.builder.producir_salsa()
        self.builder.producir_ingredientes()
        self.builder.producir_coccion()
        self.builder.producir_presentacion()
        self.builder.producir_maridaje()
        self.builder.producir_extras()

