from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from InterfacesGUI.pagina_pizza import *
from InterfacesGUI.pagina_personalizada import *
from InterfacesGUI.pagina_menu import *
from CSVHandler.csv_handler import * 

class PantallaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pizzas_existentes = []
        self.pizzas_personalizadas = []
        self.menus = []

        # Asegúrate de hacer que las instancias de las páginas sean atributos de la clase
        self.pagina_pizza = PaginaPizza(self.pizzas_existentes)
        self.pagina_personalizada = PaginaPersonalizada(self.pizzas_personalizadas)
        self.pagina_menu = PaginaMenu(self.menus)

        btn_pizza = QPushButton('Hacer Pedido de Pizza', self)
        btn_personalizada = QPushButton('Personalizar Pizza', self)
        btn_menu = QPushButton('Pedir Menú', self)

        btn_pizza.clicked.connect(self.mostrar_pagina_pizza)
        btn_personalizada.clicked.connect(self.mostrar_pagina_personalizada)
        btn_menu.clicked.connect(self.mostrar_pagina_menu)

        layout = QVBoxLayout()
        layout.addWidget(btn_pizza)
        layout.addWidget(btn_personalizada)
        layout.addWidget(btn_menu)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_pagina_pizza(self):
        self.pagina_pizza.show()

    def mostrar_pagina_personalizada(self):
        self.pagina_personalizada.show()

    def mostrar_pagina_menu(self):
        self.pagina_menu.show()
