from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 

class NuevoCalculo(QMainWindow):
    def __init__(self):
        super(NuevoCalculo,self).__init__()
        loadUi("gui/nuevoCalculo.ui",self)
        self.show()
        
        self.iniGUI()
    
    def iniGUI(self):
        self.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)

            
    
    def EntrarNuevoCalculo(self):
        #Validando que no entre campos vacios
        if self.lineEdit_densidadArena.text()=="" or float(self.lineEdit_densidadArena.text())<=0:
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Densidad de Arena Válido")
            mBox.exec()
            self.lineEdit_densidadArena.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.lineEdit_densidadArena.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Densidad Arena")
            mBox.exec()
            self.lineEdit_densidadArena.setFocus()

        #Validando que no entre campos vacios
        elif self.lineEdit_DensidadMar.text()== ""  or float(self.lineEdit_DensidadMar.text())<=0  :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Densidad de Mar Válido")
            mBox.exec()
            self.lineEdit_DensidadMar.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.lineEdit_DensidadMar.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Densidad Mar")
            mBox.exec()
            self.lineEdit_DensidadMar.setFocus()
        
         #Validando que no entre campos vacios 
        elif self.lineEdit_CoeficientePorocidad.text()== "" or float(self.lineEdit_CoeficientePorocidad.text())<=0   :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Coeficiente Porocidad Válido")
            mBox.exec()
            self.lineEdit_CoeficientePorocidad.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.lineEdit_CoeficientePorocidad.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Coeficiente Porocidad")
            mBox.exec()
            self.lineEdit_CoeficientePorocidad.setFocus()
            self.lineEdit_IndiceRompiente.setText("0")

        #Validando que no entre campos vacios
        elif self.lineEdit_altura.text()=="" or float(self.lineEdit_altura.text())<=0  :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Altura Válido")
            mBox.exec()
            self.lineEdit_altura.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.lineEdit_altura.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en altura")
            mBox.exec()
            self.lineEdit_altura.setFocus()
        
        #Validando que no entre campos vacios
        elif  self.lineEdit_AnguloRompiente.text()=="" or  float(self.lineEdit_AnguloRompiente.text())<=0 :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Angulo Rompiente Válido")
            mBox.exec()
            self.lineEdit_AnguloRompiente.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.lineEdit_AnguloRompiente.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Angulo Rompiente")
            mBox.exec()
            self.lineEdit_AnguloRompiente.setFocus()
        
        #Validando que no entre campos vacios
        elif self.lineEdit_IndiceRompiente.text()== "" or  float(self.lineEdit_IndiceRompiente.text())<=0 :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Indice Rompiente Válido")
            mBox.exec()
            self.lineEdit_IndiceRompiente.setFocus()
        
        elif not self.lineEdit_IndiceRompiente.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Indice Rompiente")
            mBox.exec()
            self.lineEdit_IndiceRompiente.setFocus()
        
        #Validando que no entre campos vacios
        elif self.lineEdit_Ubicacion.text()== "":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Ubicacion Válido")
            mBox.exec()
            self.lineEdit_Ubicacion.setFocus()
        else:
            DensidadArena= float(self.lineEdit_densidadArena.text())
            DensidadMar=  float(self.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.lineEdit_CoeficientePorocidad.text())
            altura=float(self.lineEdit_altura.text())
            angulo=float(self.lineEdit_AnguloRompiente.text())
            indice=float(self.lineEdit_IndiceRompiente.text())
            ubicacion=self.lineEdit_Ubicacion.text()
            fecha=self.dateEdit_Fecha.text()

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            mBox= QMessageBox()
            mBox.setText("Datos Guardados con Exito Q="+ str(resultado))
            mBox.exec()
