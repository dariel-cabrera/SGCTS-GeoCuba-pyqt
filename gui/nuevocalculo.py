from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox 

class Nuevo():
    def __init__(self):
        self.nuevocalculo=uic.loadUi("gui/nuevoC.ui")
        self.iniGUI()
        self.nuevocalculo.show()
    
    def iniGUI(self):
        self.nuevocalculo.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)
    
    def EntrarNuevoCalculo(self):
        #Validando que no entre campos vacios
        if float(self.nuevocalculo.lineEdit_densidadArena.text())<=0 or self.nuevocalculo.lineEdit_densidadArena.text()=="":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Densidad de Arena Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_densidadArena.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.nuevocalculo.lineEdit_densidadArena.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Densidad Arena")
            mBox.exec()
            self.nuevocalculo.lineEdit_densidadArena.setFocus()

        #Validando que no entre campos vacios
        elif float(self.nuevocalculo.lineEdit_DensidadMar.text())<=0 or self.nuevocalculo.lineEdit_DensidadMar.text()== "":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Densidad de Mar Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_DensidadMar.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.nuevocalculo.lineEdit_DensidadMar.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Densidad Mar")
            mBox.exec()
            self.nuevocalculo.lineEdit_DensidadMar.setFocus()
        
         #Validando que no entre campos vacios 
        elif float(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())<=0 or self.nuevocalculo.lineEdit_CoeficientePorocidad.text()== "" :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Coeficiente Porocidad Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.nuevocalculo.lineEdit_CoeficientePorocidad.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Coeficiente Porocidad")
            mBox.exec()
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setFocus()
            self.nuevocalculo.lineEdit_IndiceRompiente.setText("0")

        #Validando que no entre campos vacios
        elif float(self.nuevocalculo.lineEdit_altura.text())<=0 or self.nuevocalculo.lineEdit_altura.text()=="":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Altura Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_altura.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.nuevocalculo.lineEdit_altura.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en altura")
            mBox.exec()
            self.nuevocalculo.lineEdit_altura.setFocus()
        
        #Validando que no entre campos vacios
        elif float(self.nuevocalculo.lineEdit_AnguloRompiente.text())<=0 or self.nuevocalculo.lineEdit_AnguloRompiente.text()=="" :
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Angulo Rompiente Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_AnguloRompiente.setFocus()
        
        #Validando que solo entre Numeros
        elif not self.nuevocalculo.lineEdit_AnguloRompiente.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Angulo Rompiente")
            mBox.exec()
            self.nuevocalculo.lineEdit_AnguloRompiente.setFocus()
        
        #Validando que no entre campos vacios
        elif float(self.nuevocalculo.lineEdit_IndiceRompiente.text())<=0 or self.nuevocalculo.lineEdit_IndiceRompiente.text()== "":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Indice Rompiente Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_IndiceRompiente.setFocus()
        
        elif not self.nuevocalculo.lineEdit_IndiceRompiente.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Solo puede entrar numeros en Indice Rompiente")
            mBox.exec()
            self.nuevocalculo.lineEdit_IndiceRompiente.setFocus()
        
        #Validando que no entre campos vacios
        elif self.nuevocalculo.lineEdit_Ubicacion.text()== "":
            mBox= QMessageBox()
            mBox.setText("Debe ingresar un dato de Ubicacion Válido")
            mBox.exec()
            self.nuevocalculo.lineEdit_Ubicacion.setFocus()
        else:
            DensidadArena= float(self.nuevocalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.nuevocalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.nuevocalculo.lineEdit_altura.text())
            angulo=float(self.nuevocalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.nuevocalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.nuevocalculo.lineEdit_Ubicacion.text()
            fecha=self.nuevocalculo.dateEdit_Fecha.text()

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)

            variables=Variables(DensidadArena,DensidadArena,CoeficienteP,altura,angulo,indice,ubicacion,fecha,resultado)
            mBox= QMessageBox()
            mBox.setText("Datos Guardados con Exito Q="+ str(resultado))
            mBox.exec()
        
        
        
        



    
