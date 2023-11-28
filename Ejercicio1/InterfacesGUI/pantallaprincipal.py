from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from InterfacesGUI.pagina_pizza import *
from InterfacesGUI.pagina_personalizada import *
from InterfacesGUI.pagina_menu import *

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.pizza_button = QPushButton("Seleccionar Pizza", self)
        self.customize_button = QPushButton("Personalizar Pizza", self)
        self.menu_button = QPushButton("Seleccionar Menú", self)

        self.pizza_button.clicked.connect(self.show_pizza_page)
        self.customize_button.clicked.connect(self.show_customize_page)
        self.menu_button.clicked.connect(self.show_menu_page)

        self.layout.addWidget(self.pizza_button)
        self.layout.addWidget(self.customize_button)
        self.layout.addWidget(self.menu_button)

        #intancias de

    def show_pizza_page(self):
        self.central_widget.setCurrentIndex(0)

    def show_customize_page(self):
        self.central_widget.setCurrentIndex(1)

    def show_menu_page(self):
        self.central_widget.setCurrentIndex(2)
