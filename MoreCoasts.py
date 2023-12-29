from PyQt6.QtWidgets import QApplication
from gui.inicio import Login

class SGCTS():
    def __init__(self):
        self.app=QApplication([])
        self.inicio=Login()

        self.app.exec()


app = SGCTS () 