from PyQt6.QtWidgets import QApplication
from gui.inicio_sesion import Login

class SGCTS():
    def __init__(self):
        self.app=QApplication([])
        self.login=Login()

        self.app.exec()