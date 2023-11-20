# GUIpers.py
import tkinter as tk
from tkinter import messagebox
from PizzaBuilder.personalizada import PersonalizadaBuilder
from PizzaBuilder.Director import Director
import csv

class PizzaPersonalizadaGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Personalizada")

        self.builder = PersonalizadaBuilder()
        self.director = Director()
        self.director.builder = self.builder

        self.create_widgets()

    def create_widgets(self):
        # Masa
        tk.Label(self.root, text="Masa:").pack()
        self.masa_entry = tk.Entry(self.root)
        self.masa_entry.pack()

        # Salsa
        tk.Label(self.root, text="Salsa:").pack()
        self.salsa_entry = tk.Entry(self.root)
        self.salsa_entry.pack()

        # Ingredientes
        tk.Label(self.root, text="Ingredientes (separados por comas):").pack()
        self.ingredientes_entry = tk.Entry(self.root)
        self.ingredientes_entry.pack()

        # Coccion
        tk.Label(self.root, text="Coccion:").pack()
        self.coccion_entry = tk.Entry(self.root)
        self.coccion_entry.pack()

        # Presentacion
        tk.Label(self.root, text="Presentacion:").pack()
        self.presentacion_entry = tk.Entry(self.root)
        self.presentacion_entry.pack()

        # Maridaje
        tk.Label(self.root, text="Maridaje:").pack()
        self.maridaje_entry = tk.Entry(self.root)
        self.maridaje_entry.pack()

        # Extras
        tk.Label(self.root, text="Extras (separados por comas):").pack()
        self.extras_entry = tk.Entry(self.root)
        self.extras_entry.pack()

        # Botón para crear la pizza personalizada
        tk.Button(self.root, text="Crear Pizza Personalizada", command=self.crear_pizza_personalizada).pack()

    def crear_pizza_personalizada(self):
        masa = self.masa_entry.get()
        salsa = self.salsa_entry.get()
        ingredientes = self.ingredientes_entry.get().split(',')
        coccion = self.coccion_entry.get()
        presentacion = self.presentacion_entry.get()
        maridaje = self.maridaje_entry.get()
        extras = self.extras_entry.get().split()

        self.director.build_full_featured_product()
        self.builder.producir_masa(masa)
        self.builder.producir_salsa(salsa)
        self.builder.producir_ingredientes(ingredientes)
        self.builder.producir_coccion(coccion)
        self.builder.producir_presentacion(presentacion)
        self.builder.producir_maridaje(maridaje)
        self.builder.producir_extras(extras)

        pizza_personalizada = self.builder.pizza
        pizza_personalizada.list_parts()

        # Guardar la pizza personalizada en un CSV (puedes ajustar la ruta)
        with open('Ejercicio2/CSV/pizzas_personalizadas.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(pizza_personalizada.parts)

        messagebox.showinfo("Pizza Personalizada", "Pizza personalizada creada y guardada en pizzas_personalizadas.csv")


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPersonalizadaGUI(root)
    root.mainloop()
