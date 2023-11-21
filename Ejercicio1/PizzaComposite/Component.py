from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class MenuComponent(ABC):

    @property
    def menu(self) -> MenuComponent:
        return self._menu

    @menu.setter
    def menu(self, parent: MenuComponent):
        self._parent = parent

    def add(self, component: MenuComponent) -> None:
        pass

    def remove(self, component: MenuComponent) -> None:
        pass

    def is_composite(self) -> bool:

        return False

    @abstractmethod
    def listar_componenetes(self) -> str:
        pass

    @abstractmethod
    def obtener_precio(self) -> str:
        pass

class Leaf(MenuComponent):

    def operation(self) -> str:
        return "Leaf"


class Postre(MenuComponent):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def listar_componentes(self):
        print(f"Postre: {self.nombre}")

    def obtener_precio(self) -> float:
        return self.precio


def client_code(component: Component) -> None:

    print(f"RESULT: {component.operation()}", end="")


def client_code2(component1: Component, component2: Component) -> None:


    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")


