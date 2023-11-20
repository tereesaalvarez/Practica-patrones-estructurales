# GUIpizza.py
import tkinter as tk
from tkinter import messagebox
from PizzaBuilder.barbacoa import BarbacoaBuilder
from PizzaBuilder.cuatroquesos import CuatroQuesosBuilder
from PizzaBuilder.hawaiana import HawaianaBuilder
from PizzaBuilder.jamonyqueso import JamonyQuesoBuilder
from PizzaBuilder.margarita import MargaritaBuilder
from PizzaBuilder.vegetariana import VegetarianaBuilder
from PizzaBuilder.Director import Director
import csv

class PizzaExistenteGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pizzas Existentes")

        self.director = Director()
        self.create_widgets()

    def create_widgets(self):
        # Lista de pizzas existentes
        opciones_pizzas = ["Barbacoa", "Cuatro Quesos", "Hawaiana", "Jamón y Queso", "Margarita", "Vegetariana"]
        self.pizza_seleccionada = tk.StringVar(self.root)
        self.pizza_seleccionada.set(opciones_pizzas[0])  # Por defecto, seleccionar la primera pizza

        tk.Label(self.root, text="Selecciona una pizza existente:").pack()
        pizza_menu = tk.OptionMenu(self.root, self.pizza_seleccionada, *opciones_pizzas)
        pizza_menu.pack()

        # Botón para seleccionar la pizza existente
        tk.Button(self.root, text="Seleccionar Pizza", command=self.seleccionar_pizza_existente).pack()

    def seleccionar_pizza_existente(self):
        pizza_seleccionada = self.pizza_seleccionada.get()

        # Construir la pizza seleccionada
        if pizza_seleccionada == "Barbacoa":
            builder = BarbacoaBuilder()
        elif pizza_seleccionada == "Cuatro Quesos":
            builder = CuatroQuesosBuilder()
        elif pizza_seleccionada == "Hawaiana":
            builder = HawaianaBuilder()
        elif pizza_seleccionada == "Jamón y Queso":
            builder = JamonyQuesoBuilder()
        elif pizza_seleccionada == "Margarita":
            builder = MargaritaBuilder()
        elif pizza_seleccionada == "Vegetariana":
            builder = VegetarianaBuilder()
        else:
            messagebox.showerror("Error", "Pizza no reconocida")
            return

        self.director.builder = builder
        self.director.build_full_featured_product()

        pizza_existente = builder.pizza
        pizza_existente.list_parts()

        # Guardar la pizza existente en un CSV (puedes ajustar la ruta)
        with open('Ejercicio2/CSV/pizzas_existentes.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pizza_existente.parts)

        messagebox.showinfo("Pizza Existente", f"Pizza {pizza_seleccionada} seleccionada y guardada en pizzas_existentes.csv")


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaExistenteGUI(root)
    root.mainloop()
