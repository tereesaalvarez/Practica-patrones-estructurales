from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from CSVHandler.csv_handler import read_from_csv
from InterfacesGUI.pagina_personalizada import *

class PaginaPizza(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.pizza_button_1 = QPushButton("Pizza 1", self)
        self.pizza_button_2 = QPushButton("Pizza 2", self)
        self.pizza_button_3 = QPushButton("Pizza 3", self)

        self.pizza_button_1.clicked.connect(self.show_customize_page)
        self.pizza_button_2.clicked.connect(self.show_customize_page)
        self.pizza_button_3.clicked.connect(self.show_customize_page)

        self.layout.addWidget(self.pizza_button_1)
        self.layout.addWidget(self.pizza_button_2)
        self.layout.addWidget(self.pizza_button_3)

    def show_customize_page(self):
        # Aquí deberías cargar la información de la pizza seleccionada y pasársela a CustomizePage
        self.parent().parent().show_customize_page()
