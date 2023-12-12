import sys
#Donde estan todas las fotos
from .nimg import *
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve 
from PyQt6 import QtCore,QtWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox

class Principal():
    def __init__(self):
        self.principal=uic.loadUi("gui/principal.ui")
        #self.iniGUI()
        self.principal.showMaximized()


