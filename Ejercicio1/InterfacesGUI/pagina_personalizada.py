from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PizzaBuilder.personalizada import PersonalizadaBuilder
from CSVHandler.csv_handler import save_to_csv

class PaginaPersonalizada(QWidget):
    def __init__(self, pizza_name):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.builder = PersonalizadaBuilder()
        self.builder.producir_masa()
        self.builder.producir_salsa()
        # ... (continuar con otras llamadas a métodos del builder)

        self.finish_button = QPushButton("Finalizar Pedido", self)
        self.finish_button.clicked.connect(self.save_to_csv)

        self.layout.addWidget(self.finish_button)

    def save_to_csv(self):
        pizza_data = self.builder.pizza.list_parts()
        save_to_csv("Ejercicio1/CSV/pizzas_personalizadas.csv", [pizza_data], header=['Pizza'])
        # ... (otras operaciones, por ejemplo, calcular precio)
