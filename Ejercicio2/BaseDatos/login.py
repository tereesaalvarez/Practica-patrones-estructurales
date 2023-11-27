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

    def obtener_nombre_usuario(self, nombre_usuario, contraseña):
        self.cursor.execute('''
            SELECT nombre_usuario FROM usuarios_log
            WHERE nombre_usuario = ? AND contraseña = ?
        ''', (nombre_usuario, contraseña))
        result = self.cursor.fetchone()
        return result[0] if result else None

    
