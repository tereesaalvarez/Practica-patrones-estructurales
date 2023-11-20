from InterfacesGUI.InterfazQT import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PizzaGUI()
    gui.show()
    sys.exit(app.exec_())
