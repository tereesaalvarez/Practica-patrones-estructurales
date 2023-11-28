from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def display(self) -> None:
        pass



