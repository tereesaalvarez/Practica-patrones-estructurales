import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QLineEdit, QTextEdit
from PizzaBuilder.barbacoa import BarbacoaBuilder
from PizzaBuilder.cuatroquesos import CuatroQuesosBuilder
from PizzaBuilder.hawaiana import HawaianaBuilder
from PizzaBuilder.jamonyqueso import JamonyQuesoBuilder
from PizzaBuilder.margarita import MargaritaBuilder
from PizzaBuilder.vegetariana import VegetarianaBuilder
from PizzaBuilder.personalizada import PersonalizadaBuilder
from PizzaBuilder.Director import Director
import csv


class PizzaGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Pizza Builder')

        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        #crear pagina principal menu
        self.menu = QWidget()
        self.central_widget.addWidget(self.menu)

        layout = QVBoxLayout()
        self.menu.setLayout(layout)

        boton_menu = QPushButton('Menu', self)
        boton_personalizar = QPushButton('Personalizar', self)

        layout.addWidget(boton_menu)
        layout.addWidget(boton_personalizar)

        boton_menu.clicked.connect(self.pagina_menu)
        boton_personalizar.clicked.connect(self.pagina_personalizar)

        #crear menu
        self.menu = QWidget()
        self.central_widget.addWidget(self.menu)

        menu_layout = QVBoxLayout()
        self.menu.setLayout(menu_layout)

        boton_margarita = QPushButton('Margarita', self)
        boton_barbacoa = QPushButton('Barbacoa', self)
        boton_cuatroquesos = QPushButton('Cuatro Quesos', self)
        boton_hawaiana = QPushButton('Hawaiana', self)
        boton_jamonyqueso = QPushButton('Jamón y Queso', self)
        boton_vegetariana = QPushButton('Vegetariana', self)

        menu_layout.addWidget(boton_margarita)
        menu_layout.addWidget(boton_barbacoa)
        menu_layout.addWidget(boton_cuatroquesos)
        menu_layout.addWidget(boton_hawaiana)
        menu_layout.addWidget(boton_jamonyqueso)
        menu_layout.addWidget(boton_vegetariana)

        boton_margarita.clicked.connect(lambda: self.crear_pizza('Margarita'))
        boton_barbacoa.clicked.connect(lambda: self.crear_pizza('Barbacoa'))
        boton_cuatroquesos.clicked.connect(lambda: self.crear_pizza('Cuatro Quesos'))
        boton_hawaiana.clicked.connect(lambda: self.crear_pizza('Hawaiana'))
        boton_jamonyqueso.clicked.connect(lambda: self.crear_pizza('Jamón y Queso'))
        boton_vegetariana.clicked.connect(lambda: self.crear_pizza('Vegetariana'))

        #crear pagina personalizar
        self.personalizar = QWidget()
        self.central_widget.addWidget(self.personalizar)

        self.masa_input = QLineEdit(self)
        self.salsa_input = QLineEdit(self)
        self.ingredientes_input = QLineEdit(self)
        self.coccion_input = QLineEdit(self)
        self.presentacion_input = QLineEdit(self)
        self.maridaje_input = QLineEdit(self)
        self.extras_input = QLineEdit(self)

        personalizar_layout = QVBoxLayout()
        self.personalizar.setLayout(personalizar_layout)

        personalizar_layout.addWidget(QLabel('Masa: '))
        personalizar_layout.addWidget(self.masa_input)
        personalizar_layout.addWidget(QLabel('Salsa: '))
        personalizar_layout.addWidget(self.salsa_input)
        personalizar_layout.addWidget(QLabel('Ingredientes: '))
        personalizar_layout.addWidget(self.ingredientes_input)
        personalizar_layout.addWidget(QLabel('Cocción: '))
        personalizar_layout.addWidget(self.coccion_input)
        personalizar_layout.addWidget(QLabel('Presentación: '))
        personalizar_layout.addWidget(self.presentacion_input)
        personalizar_layout.addWidget(QLabel('Maridaje: '))
        personalizar_layout.addWidget(self.maridaje_input)
        personalizar_layout.addWidget(QLabel('Extras: '))
        personalizar_layout.addWidget(self.extras_input)

        boton_crear = QPushButton('Personalizar Pizza', self)
        boton_crear.clicked.connect(self.personalizar_pizza)

        personalizar_layout.addWidget(boton_crear)
        
    
    def pagina_menu(self):
        self.central_widget.setCurrentIndex(1)
        
    
    def pagina_personalizar(self):
        self.central_widget.setCurrentIndex(2)
        
    
    def crear_pizza(self, tipo_pizza):
        builder = None

        if tipo_pizza == 'Margarita':
            builder = MargaritaBuilder()
        elif tipo_pizza == 'Barbacoa':
            builder = BarbacoaBuilder()
        elif tipo_pizza == 'Cuatro Quesos':
            builder = CuatroQuesosBuilder()
        elif tipo_pizza == 'Hawaiana':
            builder = HawaianaBuilder()
        elif tipo_pizza == 'Jamón y Queso':
            builder = JamonyQuesoBuilder()
        elif tipo_pizza == 'Vegetariana':
            builder = VegetarianaBuilder()

        director = Director()
        director.builder = builder
        director.build_full_featured_product()

        pizza = builder.pizza
        pizza.list_parts()

        #guardar en el csv pizzas_existentes.csv
        with open('Ejercicio1/CSV/pizzas_existentes.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([tipo_pizza, pizza.parts])

        #resetear los campos
        self.masa_input.clear()
        self.salsa_input.clear()
        self.ingredientes_input.clear()
        self.coccion_input.clear()
        self.presentacion_input.clear()
        self.maridaje_input.clear()
        self.extras_input.clear()

    def personalizar_pizza(self):
        masa = self.masa_input.text()
        salsa = self.salsa_input.text()
        ingredientes = self.ingredientes_input.text().split(',')
        coccion = self.coccion_input.text()
        presentacion = self.presentacion_input.text()
        maridaje = self.maridaje_input.text()
        extras = self.extras_input.text().split(',')

        builder = PersonalizadaBuilder()
        director = Director()
        director.builder = builder
        director.build_full_featured_product()

        builder.producir_masa(masa)
        builder.producir_salsa(salsa)
        builder.producir_ingredientes(ingredientes)
        builder.producir_coccion(coccion)
        builder.producir_presentacion(presentacion)
        builder.producir_maridaje(maridaje)
        builder.producir_extras(extras)

        pizza_personalizada = builder.pizza
        pizza_personalizada.list_parts()

        #guardar en el csv pizzas_personalizadas.csv
        with open('Ejercicio1/CSV/pizzas_personalizadas.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([pizza_personalizada.parts])

        #resetear los campos
        self.masa_input.clear()
        self.salsa_input.clear()
        self.ingredientes_input.clear()
        self.coccion_input.clear()
        self.presentacion_input.clear()
        self.maridaje_input.clear()
        self.extras_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PizzaGUI()
    gui.show()
    sys.exit(app.exec_())

