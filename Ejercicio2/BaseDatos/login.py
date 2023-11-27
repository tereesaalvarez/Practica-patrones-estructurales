import sqlite3
from datetime import datetime

class AccederDatabase:
    def __init__(self):
        self.connection = sqlite3.connect('Ejercicio2/BaseDatos/basedatos.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario VARCHAR(50) UNIQUE,
                contraseña VARCHAR(50),
                fecha_creacion DATETIME
            )
        ''')
        self.connection.commit()

    def logear(self, usuario, contraseña):
        fecha = datetime.now()
        self.cursor.execute('''
            INSERT INTO usuarios_log VALUES (NULL, ?, ?, ?)
        ''', (usuario, contraseña, fecha))
        self.connection.commit()

    def cerrar(self):
        self.connection.cerrar()

    
