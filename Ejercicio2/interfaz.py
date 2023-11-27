import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox, QVBoxLayout

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

class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.usuario_db = UsuarioDatabase()
        self.acceder_db = AccederDatabase()

        self.setWindowTitle("Ventana")
        self.setGeometry(100, 100, 800, 600)

        self.boton_registro = QPushButton("Registro")
        self.boton_registro.clicked.connect(self.registro)

        self.boton_acceso = QPushButton("Acceder Documento")
        self.boton_acceso.clicked.connect(self.acceso)

        layout = QVBoxLayout()
        layout.addWidget(self.boton_registro)
        layout.addWidget(self.boton_acceso)

    def registro
