from PyQt6 import uic
import pathlib

class Mensaje():
    def __init__(self):
        mod_path = pathlib.Path(__file__).parent
        self.mensaje=uic.loadUi(mod_path/"Mensaje.ui")
        self.mensaje.show()
        
    def label(self,mensaje):
        self.mensaje.label.clear()
        self.mensaje.label.setText(mensaje)
    
    def button(self):
        self.mensaje.pushButton.clicked.connect(self.mensaje.close)
    