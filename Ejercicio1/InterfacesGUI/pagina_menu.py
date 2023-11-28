from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PizzaComposite.menu import Menu
from CSVHandler.csv_handler import save_to_csv

class PaginaMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.menu_button_1 = QPushButton("Menú 1", self)
        self.menu_button_2 = QPushButton("Menú 2", self)
        self.menu_button_3 = QPushButton("Menú 3", self)

        self.menu_button_1.clicked.connect(self.save_to_csv)
        self.menu_button_2.clicked.connect(self.save_to_csv)
        self.menu_button_3.clicked.connect(self.save_to_csv)

        self.layout.addWidget(self.menu_button_1)
        self.layout.addWidget(self.menu_button_2)
        self.layout.addWidget(self.menu_button_3)

    def save_to_csv(self):
        menu = Menu("Menu")
        # Agregar pizzas u otros elementos al menú según sea necesario
        menu_data = menu.list_parts()
        save_to_csv("Ejercicio1/CSV/menu.csv", [menu_data], header=['Menu'])
        # ... (otras operaciones, por ejemplo, calcular precio)
