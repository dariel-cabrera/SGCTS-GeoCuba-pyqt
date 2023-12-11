from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from gui.nuevocalculo import Nuevo
from gui.editarCalculo import EditarCalculo
from model.ecuaciones import transporte_logitudinal_arena 
from model.variables import Variables 

class Principal():
    def __init__(self):
        self.principal=uic.loadUi("gui/principal.ui")
        self.iniGUI()
        self.principal.showMaximized()
        
    
    def iniGUI(self):
        self.principal.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.principal.button_EditarCalculo.clicked.connect(self.editarCalculo)
    
    def nuevocalculo(self):
        self.nuevocalculo= Nuevo()
    
    def editarCalculo(self):
        self.editarCalculo=EditarCalculo()
   
        

    
            
        
    
    
    
    
    
    
    
    
    
    