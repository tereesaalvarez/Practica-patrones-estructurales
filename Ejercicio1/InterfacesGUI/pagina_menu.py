# Ejercicio1/InterfacesGUI/pagina_menu.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class PaginaMenu(QWidget):
    def __init__(self, menus):
        super().__init__()

        # Lógica para mostrar los menús
        layout = QVBoxLayout()
        for menu in menus:
            label = QLabel(f"Nombre: {menu.name}, Precio Total: {menu.calcular_precio_total()}")
            layout.addWidget(label)

        self.setLayout(layout)