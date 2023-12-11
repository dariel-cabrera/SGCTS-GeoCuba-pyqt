from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox 

class EditarCalculo():
    def __init__(self):
        self.editar=uic.loadUi("gui/EditarCalculo.ui")
        #self.iniGUI()
        self.editar.show()