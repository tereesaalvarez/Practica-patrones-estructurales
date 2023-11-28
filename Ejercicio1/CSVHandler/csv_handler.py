import csv
from PizzaBuilder.personalizada import *
from PizzaComposite.menu import *

def save_to_csv(file_path, data, header=None):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        if header:
            writer.writerow(header)
        writer.writerows(data)

def read_from_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def save_pizzas_to_csv(file_path, pizzas):
    data = []
    for pizza in pizzas:
        data.append(pizza.parts)  # Suponiendo que 'parts' es una lista de ingredientes en la pizza
    save_to_csv(file_path, data, header=['Ingredientes'])

def load_pizzas_from_csv(file_path):
    data = read_from_csv(file_path)
    pizzas = []
    for row in data:
        pizza = Personalizada()
        pizza.parts = row  # Ajustar según la estructura de tu CSV
        pizzas.append(pizza)
    return pizzas

def save_menus_to_csv(file_path, menus):
    data = []
    for menu in menus:
        data.append(menu.parts)  # Suponiendo que 'parts' es una lista de pizzas en el menú
    save_to_csv(file_path, data, header=['Pizzas'])

def load_menus_from_csv(file_path):
    data = read_from_csv(file_path)
    menus = []
    for row in data:
        menu = Menu()
        menu.parts = row  # Ajustar según la estructura de tu CSV
        menus.append(menu)
    return menus
