from PyQt6 import uic

class Mensaje():
    def __init__(self):
        self.mensaje=uic.loadUi("gui/Mensaje.ui")
        self.mensaje.label.clear()
        self.mensaje.show()
        
    def label(self,mensaje):
        self.mensaje.label.setText(mensaje)
    
    def button(self):
        self.mensaje.pushButton.clicked.connect(self.mensaje.close)
    