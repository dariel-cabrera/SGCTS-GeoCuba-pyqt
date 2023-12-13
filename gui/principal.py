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
        #Iniciando
        super(Principal,self).__init__()
        loadUi("gui/principal.ui",self)
        #Mostrando La Ventana a Maximizada
        self.showMaximized()
        #Llamando a la Funcion iniGUi()
        self.iniGUI()
        

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_usuarios))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

        #Control de Barra de Titulo
        self.button_MinimizarVentana.clicked.connect(self.control_bt_minimizar)
        self.Button_Minimizar.clicked.connect(self.control_bt_normal)
        self.Button_Maximizar.clicked.connect(self.control_bt_maximizar)
        self.Button_Cerrar.clicked.connect(lambda: self.close())
    
    def iniGUI(self):
        #Conectando el Boton Nuevo Calculo con la ventana Nuevo Calculo
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
    
    def nuevocalculo(self):
        #Llamando a la ventana NuevoCalculo
        self.nuevocalculo= NuevoCalculo()
    
    def control_bt_minimizar(self):
        self.showMinimized()
    
    def control_bt_normal(self):
        self.showNormal()
        self.Button_Minimizar.hide()
        self.Button_Maximizar.show()
    
    def control_bt_maximizar(self):
        self.showMaximized()
        self.Button_Maximizar.hide()
        self.Button_Minimizar.show()



        


