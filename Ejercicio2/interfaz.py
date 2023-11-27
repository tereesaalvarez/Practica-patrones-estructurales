import sys
from PyQt5.QtWidgets import QApplication,QInputDialog, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTreeWidget, QTreeWidgetItem, QMessageBox
from PyQt5.QtCore import Qt

#importar todas las clases de las carpetas
from Proxy.proxy import *
from Proxy.subject import *
from Composite.carpeta import *
from Composite.leaf import *
from Composite.link import *
from Composite.component import *
from Composite.document import * 
from BaseDatos.login import *
from BaseDatos.usuario import *



class PaginaInicio(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("SAMUR-Protección Civil Document Management System")
        self.setGeometry(100, 100, 400, 200)

        self.boton_registro = QPushButton("Registro")
        self.boton_login = QPushButton("Login")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Bienvenido"))
        layout.addWidget(self.boton_registro)
        layout.addWidget(self.boton_login)

        self.setLayout(layout)
        self.login_button.clicked.connect(self.iniciar_sesion)

class PaginaRegistro(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 200)

        self.label_usuario = QLabel("Usuario:")
        self.input_usuario = QLineEdit()
        self.label_contraseña = QLabel("Contraseña:")
        self.input_contraseña = QLineEdit()
        self.boton_continuar = QPushButton("Continuar")

        layout = QVBoxLayout()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(self.boton_continuar)

        self.setLayout(layout)

class PaginaInicioSesion(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Inicio de Sesión")
        self.setGeometry(100, 100, 400, 200)

        self.label_usuario = QLabel("Usuario:")
        self.input_usuario = QLineEdit()
        self.label_contraseña = QLabel("Contraseña:")
        self.input_contraseña = QLineEdit()
        self.boton_continuar = QPushButton("Continuar")

        layout = QVBoxLayout()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.input_contraseña)
        layout.addWidget(self.boton_continuar)

        self.setLayout(layout)

class PaginaPrincipal(QWidget):
    def __init__(self, usuario, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Bienvenido, {usuario}")
        self.setGeometry(100, 100, 800, 600)

        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(["Elemento"])
        self.boton_modificar = QPushButton("Modificar")
        self.boton_eliminar = QPushButton("Eliminar")
        self.boton_desconectar = QPushButton("Desconectar")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Estructura de documentos"))
        layout.addWidget(self.tree_widget)
        layout.addWidget(self.boton_modificar)
        layout.addWidget(self.boton_eliminar)
        layout.addWidget(self.boton_desconectar)

        self.setLayout(layout)

        # Ejemplo de estructura de documentos
        self.documento1 = Documento("Informe1", "Texto", 15)
        self.documento2 = Documento("Foto1", "Imagen", 25)
        self.link1 = Link("Enlace a Carpeta1")
        self.carpeta1 = Carpeta("Carpeta1")
        self.carpeta1.add(self.documento1)
        self.carpeta1.add(self.documento2)
        self.carpeta1.add(self.link1)
        self.root_folder = Carpeta("Root")
        self.root_folder.add(self.carpeta1)

        # Rellenar el QTreeWidget con la estructura de documentos
        self.populate_tree(self.root_folder)

        # Conectar señales y slots
        self.boton_modificar.clicked.connect(self.modificar_elemento)
        self.boton_eliminar.clicked.connect(self.eliminar_elemento)
        self.boton_desconectar.clicked.connect(self.desconectar_usuario)
        self.tree_widget.itemClicked.connect(self.handle_tree_item_click)

    def populate_tree(self, component, tree_item=None):
        if tree_item is None:
            tree_item = QTreeWidgetItem(self.tree_widget, [component.nombre])
            tree_item.data = component

        for child in component.get_children():
            child_item = QTreeWidgetItem(tree_item, [child.nombre])
            child_item.data = child
            if isinstance(child, Carpeta):
                self.populate_tree(child, child_item)
            elif isinstance(child, Link):
                linked_item = QTreeWidgetItem(child_item, [child.link])
                linked_item.data = child.link

    def handle_tree_item_click(self, item):
        if hasattr(item, "data"):
            component = item.data
            QMessageBox.information(self, "Elemento Seleccionado", f"Elemento seleccionado: {component.nombre}")

    def modificar_elemento(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item and hasattr(selected_item, "data"):
            component = selected_item.data
            response = QMessageBox.question(
                self, "Modificar Elemento",
                "¿Qué desea realizar?",
                QMessageBox.Yes | QMessageBox.No
            )

            if response == QMessageBox.Yes:
                self.modificar_nombre_elemento(component)

    def modificar_nombre_elemento(self, element):
        nuevo_nombre, ok = QInputDialog.getText(self, "Modificar Nombre", "Nuevo nombre:")
        if ok:
            element.nombre = nuevo_nombre
            self.populate_tree(self.root_folder)  # Actualizar la visualización

    def eliminar_elemento(self):
        selected_item = self.tree_widget.currentItem()
        if selected_item and hasattr(selected_item, "data"):
            component = selected_item.data
            response = QMessageBox.question(
                self, "Eliminar Elemento",
                "¿Está seguro de que desea eliminar?",
                QMessageBox.Yes | QMessageBox.No
            )

            if response == QMessageBox.Yes:
                parent_item = selected_item.parent()
                parent_component = parent_item.data if parent_item else self.root_folder
                parent_component.remove(component)
                self.populate_tree(self.root_folder)  # Actualizar la visualización
                self.registrar_accion(f"Eliminado {component.nombre} ")

    def desconectar_usuario(self):
        # Lógica para desconectar al usuario y cerrar la sesión
        self.registrar_accion("Desconexión")
        self.close()

    def registrar_accion(self, accion, usuario):
        # Lógica para registrar la acción en la base de datos registros.db
        log_db = AccederDatabase()
        log_db.logear(usuario, accion)
        log_db.cerrar()

class InterfazApp:
    def __init__(self):
        self.app = QApplication([])
        self.usuario_db = UsuarioDatabase()
        self.login_db = AccederDatabase()
        self.usuario_actual = None

    def mostrar_pagina_inicio(self):
        self.pagina_inicio = PaginaInicio()
        self.pagina_inicio.boton_registro.clicked.connect(self.mostrar_pagina_registro)
        self.pagina_inicio.boton_login.clicked.connect(self.mostrar_pagina_inicio_sesion)
        self.pagina_inicio.show()
        self.app.exec_()

    def mostrar_pagina_registro(self):
        self.pagina_registro = PaginaRegistro()
        self.pagina_registro.boton_continuar.clicked.connect(self.registrar_usuario)
        self.pagina_registro.show()

    def registrar_usuario(self):
        nombre_usuario = self.pagina_registro.input_usuario.text()
        contraseña = self.pagina_registro.input_contraseña.text()

        # Verificar que no exista el usuario
        if self.usuario_db.encontrar_usuario(nombre_usuario, contraseña):
            QMessageBox.warning(self.pagina_registro, "Error", "El usuario ya existe. Por favor, elige otro.")
            return

        # Añadir el usuario a la base de datos
        nuevo_usuario = Usuario(nombre_usuario, contraseña)
        self.usuario_db.añadir_usuario(nuevo_usuario)
        self.login_db.logear(nombre_usuario, contraseña)

        # Volver a la página de inicio
        self.pagina_registro.close()
        self.mostrar_pagina_inicio()

    def mostrar_pagina_inicio_sesion(self):
        self.pagina_inicio_sesion = PaginaInicioSesion()
        self.pagina_inicio_sesion.boton_continuar.clicked.connect(self.iniciar_sesion)
        self.pagina_inicio_sesion.show()

    def iniciar_sesion(self):
        nombre_usuario = self.user_input.text()
        contraseña = self.password_input.text()

        db = AccederDatabase()
        usuario_valido = db.encontrar_usuario(nombre_usuario, contraseña)

        if usuario_valido:
            # Obtener el nombre de usuario al iniciar sesión
            self.nombre_de_usuario_actual = db.obtener_nombre_usuario(nombre_usuario, contraseña)
            self.show_main_page()
        else:
            QMessageBox.warning(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos")

        db.cerrar()

        
    def mostrar_pagina_principal(self):
        self.pagina_principal = PaginaPrincipal(self.usuario_actual)
        self.pagina_principal.boton_desconectar.clicked.connect(self.desconectar_usuario)
        self.pagina_principal.show()
        self.app.exec_()

    def desconectar_usuario(self):
        # Lógica para desconectar al usuario y cerrar la sesión
        self.usuario_actual = None
        self.pagina_principal.close()
        self.mostrar_pagina_inicio()

if __name__ == "__main__":
    app_interfaz = InterfazApp()
    app_interfaz.mostrar_pagina_inicio()
