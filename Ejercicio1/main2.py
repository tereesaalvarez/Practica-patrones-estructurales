from PyQt5.QtWidgets import QApplication
from InterfacesGUI.pantallaprincipal import *

if __name__ == '__main__':
    app = QApplication([])
    ventana = PantallaPrincipal()
    ventana.show()
    app.exec_()