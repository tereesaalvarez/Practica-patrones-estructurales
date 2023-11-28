from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class PaginaPizza(QWidget):
    def __init__(self, pizzas_existentes):
        super().__init__()

        # Lógica para mostrar las pizzas existentes
        layout = QVBoxLayout()
        for pizza in pizzas_existentes:
            label = QLabel(f"Nombre: {pizza.name}, Precio: {pizza.get_price()}")
            layout.addWidget(label)

        self.setLayout(layout)