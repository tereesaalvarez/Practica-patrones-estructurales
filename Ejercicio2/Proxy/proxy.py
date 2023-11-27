from abc import ABC, abstractmethod
from Proxy.subject import *

class Proxy(Subject):
    """
    The Proxy has an interface identical to the RealSubject.
    """

    def __init__(self, real_subject, usuario, log_db) -> None:
        self._real_subject = real_subject
        self.usuario = usuario
        self.log_db = log_db

    def operacion(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked RealSubject object.
        """

        if self.check_access():
            self._real_subject.operacion()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        accion = f"Se ha accedido a {self._real_subject.name} por {self.usuario} a las {datetime.now()}"
        self.log_db.logear(self.usuario, accion)
        print("Proxy: Logging the time of request.", end="")

