from __future__ import annotations
from typing import Any

from abc import ABC, abstractmethod


class PizzaBuilder(ABC):

    @property
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def producir_masa(self) -> None:
        pass

    @abstractmethod
    def producir_salsa(self) -> None:
        pass

    @abstractmethod
    def producir_ingredientes(self) -> None:
        pass

    @abstractmethod
    def producir_coccion(self) -> None:
        pass

    @abstractmethod
    def producir_presentacion(self) -> None:
        pass

    @abstractmethod
    def producir_maridaje(self) -> None:
        pass

    @abstractmethod
    def producir_extras(self) -> None:
        pass






