from PyQt6.QtWidgets import QApplication
from gui.principal import Principal

class SGCTS():
    def __init__(self):
        self.app=QApplication([])
        self.principal=Principal()

        self.app.exec()


app = SGCTS () 