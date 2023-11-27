from abc import ABC, abstractmethod
from datetime import datetime

class Subject(ABC):
    """
    The Subject interface declares common operations for both RealSubject and
    the Proxy. As long as the client works with RealSubject using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def operacion(self) -> None:
        pass

class RealSubject(Subject):
    def __init__(self, name):
        self.name = name

    def operacion(self):
        print(f"realSubject: Handling request for {self.name}")