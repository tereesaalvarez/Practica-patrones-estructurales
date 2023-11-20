from __future__ import annotations
from typing import Any
from PizzaBuilder.Builder import PizzaBuilder
from abc import ABC, abstractmethod


class PersonalizadaBuilder(PizzaBuilder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = Personalizada()

    @property
    def pizza(self) -> Personalizada:
        pizza = self._pizza
        self.reset()
        return pizza

    def producir_masa(self) -> None:
        masa = input("Elige el tipo de masa (fina, normal, gruesa)")
        self._pizza.add(f'Masa: {masa}')

    def producir_salsa(self) -> None:
        salsa = input('Elige la salsa (tomate, barbacoa)')
        self._pizza.add(f'Salsa: {salsa}')

    def producir_ingredientes(self) -> None:
        while True:
            ingrediente = input('Elige un ingrediente (jamón, queso, pollo, cebolla, maíz, albahaca, trufa, mozzarella, albahaca, queso azul, queso brie, queso de cabra, queso mozzarella) fin para ninguno')
            if ingrediente == 'fin':
                break
            else:
                self._pizza.add(f'Ingrediente: {ingrediente}')

    def producir_coccion(self) -> None:
        coccion = input('Elige el tipo de cocción (horno tradicional, horno de leña, horno de piedra)')
        self._pizza.add(f'Cocción: {coccion}') 

    def producir_presentacion(self) -> None:
        presentacion = input('Elige la presentación (pizza circular, pizza rectangular)')
        self._pizza.add(f'Presentación: {presentacion}')

    def producir_maridaje(self) -> None:
        maridaje = input('Elige el maridaje (cerveza rubia, vino blanco, refresco de cola, vino tinto)')
        self._pizza.add(f'Maridaje: {maridaje}')
        
    def producir_extras(self) -> None:
        while True:
            extra = input('Elige un extra (aceitunas negras, salsa barbacoa adicional, nuez picada) fin para ninguno')
            if extra == 'fin':
                break
            else:
                self._pizza.add(f'Extra: {extra}')
        

class Personalizada():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Pizza parts: {', '.join(self.parts)}", end="")