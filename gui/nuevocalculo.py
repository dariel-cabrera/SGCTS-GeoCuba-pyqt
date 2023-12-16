from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 
from PyQt6 import QtWidgets, QtGui
from data.tla import TLAData
from PyQt6 import QtCore,QtWidgets
#from .principal import mostrar_datos_tablaCalculos


class NuevoCalculo(QMainWindow):
    def __init__(self):
        super(NuevoCalculo,self).__init__()
        loadUi("gui/nuevoCalculo.ui",self)
        self.show()
        
        self.iniGUI()
    
    def iniGUI(self):
        self.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)
        
    
    

    def EntrarNuevoCalculo(self):
        if self.lineEdit_densidadArena.text()=="" or self.lineEdit_DensidadMar.text()=="" or self.      lineEdit_CoeficientePorocidad.text()=="" or self.lineEdit_altura.text()=="" or self.lineEdit_AnguloRompiente.text()=="" or self.lineEdit_IndiceRompiente.text()=="" or self.lineEdit_Ubicacion.text()=="":
            mBox= QMessageBox()
            mBox.setText("No se pueden entrar campos Vacios")
            mBox.exec()

        else:
            DensidadArena= float(self.lineEdit_densidadArena.text())
            DensidadMar=  float(self.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.lineEdit_CoeficientePorocidad.text())
            altura=float(self.lineEdit_altura.text())
            angulo=float(self.lineEdit_AnguloRompiente.text())
            indice=float(self.lineEdit_IndiceRompiente.text())
            ubicacion=self.lineEdit_Ubicacion.text()
           

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            
            self.tla= TLAData()
            mBox= QMessageBox()
            #self.mostrar= mostrar_datos_tablaCalculos()
            if self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado):
                mBox.setText("Datos Guardados con Exito Q="+ str(resultado))  
                #self.but_GuardarNuevoCalculo.clicked.connect(self.mostrar) 
                self.hide()
            else:
                mBox.setText("Los Datos NO se Guardados")
            mBox.exec()
    
    