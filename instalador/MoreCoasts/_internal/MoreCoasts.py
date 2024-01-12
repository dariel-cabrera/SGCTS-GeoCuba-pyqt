from PyQt6.QtWidgets import QApplication
from gui.inicio import Login

class MoreCoasts():
    def __init__(self):
        self.app=QApplication([])
        self.inicio=Login()

        self.app.exec()


app = MoreCoasts() 