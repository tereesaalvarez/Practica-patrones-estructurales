from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from InterfacesGUI.pagina_pizza import *
from InterfacesGUI.pagina_personalizada import *
from InterfacesGUI.pagina_menu import *
from CSVHandler.csv_handler import * 

class PantallaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.pizzas_existentes = []  # Lista para almacenar pizzas existentes
        self.pizzas_personalizadas = []  # Lista para almacenar pizzas personalizadas
        self.menus = []  # Lista para almacenar menús

        # Crear botones para cada opción
        btn_pizza = QPushButton('Hacer Pedido de Pizza', self)
        btn_personalizada = QPushButton('Personalizar Pizza', self)
        btn_menu = QPushButton('Pedir Menú', self)

        # Conectar botones a las páginas correspondientes
        btn_pizza.clicked.connect(self.mostrar_pagina_pizza)
        btn_personalizada.clicked.connect(self.mostrar_pagina_personalizada)
        btn_menu.clicked.connect(self.mostrar_pagina_menu)

        # Diseño de la pantalla principal
        layout = QVBoxLayout()
        layout.addWidget(btn_pizza)
        layout.addWidget(btn_personalizada)
        layout.addWidget(btn_menu)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def mostrar_pagina_pizza(self):
        # Lógica para mostrar la página de hacer pedido de pizza
        pagina_pizza = PaginaPizza(self.pizzas_existentes)
        pagina_pizza.show()

    def mostrar_pagina_personalizada(self):
        # Lógica para mostrar la página de personalizar pizza
        pagina_personalizada = PaginaPersonalizada(self.pizzas_personalizadas)
        pagina_personalizada.show()

    def mostrar_pagina_menu(self):
        # Lógica para mostrar la página de pedir menú
        pagina_menu = PaginaMenu(self.menus)
        pagina_menu.show()
