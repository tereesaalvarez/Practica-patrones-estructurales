# Ejercicio1/InterfacesGUI/pagina_personalizada.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class PaginaPersonalizada(QWidget):
    def __init__(self, pizzas_personalizadas):
        super().__init__()

        # Lógica para mostrar las pizzas personalizadas
        layout = QVBoxLayout()
        for pizza in pizzas_personalizadas:
            label = QLabel(f"Ingredientes: {', '.join(pizza.parts)}, Precio: {pizza.get_price()}")
            layout.addWidget(label)

        self.setLayout(layout)