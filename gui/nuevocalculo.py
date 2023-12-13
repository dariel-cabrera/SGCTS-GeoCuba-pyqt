from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView

class NuevoCalculo(QMainWindow):
     def __init__(self):
        super(NuevoCalculo,self).__init__()
        loadUi("gui/nuevoCalculo.ui",self)
        self.show()
