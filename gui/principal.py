import sys
#Donde estan todas las fotos
from .nimgC import *
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve 
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox
from .nuevocalculo import NuevoCalculo

class Principal(QMainWindow):
    def __init__(self):
        super(Principal,self).__init__()
        loadUi("gui/principal.ui",self)
        self.showMaximized()
        self.iniGUI()
        

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_usuarios))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))
    
    def iniGUI(self):
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
    
    def nuevocalculo(self):
        self.nuevocalculo= NuevoCalculo()

        


