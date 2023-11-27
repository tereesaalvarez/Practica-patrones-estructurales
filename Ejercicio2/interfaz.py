import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout
from PyQt5.QtCore import Qt

#importar todas las clases de las carpetas
from Proxy.proxy import *
from Proxy.subject import *
from Composite.carpeta import *
from Composite.leaf import *
from Composite.link import *
from Composite.component import *
from Composite.document import * 
from BaseDatos.login import *
from BaseDatos.usuario import *

# Ejercicio2/interfaz.py
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import Qt

class PaginaInicio(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("SAMUR-Protección Civil Document Management System")
        self.setGeometry(100, 100, 400, 200)

        self.boton_registro = QPushButton("Registro")
        self.boton_login = QPushButton("Login")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bienvenido"))
        layout.addWidget(self.boton_registro)
        layout.addWidget(self.boton_login)

        self.setLayout(layout)

class PaginaPrincipal(QWidget):
    def __init__(self, usuario, parent=None):
        super().__init__(parent)

        self.setWindowTitle(f"Bienvenido, {usuario}")
        self.setGeometry(100, 100, 800, 600)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Elemento"])
        self.boton_modificar = QPushButton("Modificar")
        self.boton_eliminar = QPushButton("Eliminar")
        self.boton_desconectar = QPushButton("Desconectar")

        layout = QVBoxLayout()
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.boton_modificar)
        layout.addWidget(self.boton_eliminar)
        layout.addWidget(self.boton_desconectar)

        self.setLayout(layout)

class InterfazApp:
    def __init__(self):
        self.app = QApplication([])

    def mostrar_pagina_inicio(self):
        self.pagina_inicio = PaginaInicio()
        self.pagina_inicio.boton_registro.clicked.connect(self.mostrar_pagina_principal)
        self.pagina_inicio.show()
        self.app.exec_()

    def mostrar_pagina_principal(self):
        # Lógica para verificar el usuario en la base de datos
        usuario = "UsuarioEjemplo"  # Obtén el usuario de la base de datos
        self.pagina_principal = PaginaPrincipal(usuario)
        self.pagina_principal.boton_desconectar.clicked.connect(self.desconectar_usuario)
        self.pagina_principal.show()
        self.app.exec_()

    def desconectar_usuario(self):
        # Lógica para desconectar al usuario y cerrar la sesión
        self.pagina_principal.close()
        self.mostrar_pagina_inicio()

if __name__ == "__main__":
    app_interfaz = InterfazApp()
    app_interfaz.mostrar_pagina_inicio()
