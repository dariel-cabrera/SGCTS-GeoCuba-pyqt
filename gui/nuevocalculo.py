from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 
from PyQt6 import QtWidgets, QtGui
from data.tla import TLAData
from PyQt6 import QtCore,QtWidgets
from model.validarcampos import ValidarCampos


class NuevoCalculo():
    def __init__(self):
        self.nuevocalculo=uic.loadUi("gui/nuevoCalculo.ui")
        self.iniGUI()
    
    def iniGUI(self):
        self.nuevocalculo.label_Error.setText("")
        self.nuevocalculo.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)
        self.nuevocalculo.butCancelarNuevoCalculo.clicked.connect(self.boton_Cancelar_NuevoCalculo)
        self.nuevocalculo.show()
    

    def limpiarCamposNuevoCalculo(self):
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_densidadArena.setText("")
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_CoeficientePorocidad.setText("")
        self.nuevocalculo.lineEdit_altura.setText("")
        self.nuevocalculo.lineEdit_AnguloRompiente.setText("")
        self.nuevocalculo.lineEdit_IndiceRompiente.setText("")
        self.nuevocalculo.lineEdit_Ubicacion.setText("")

    def validandocamposNuevoCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()
        
      
        DensidadArena=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_IndiceRompiente.text())
        ubicacion=self.validarcampo.validarCamposNombre(self.nuevocalculo.lineEdit_Ubicacion.text())

        if DensidadArena==False:
            self.nuevocalculo.lineEdit_densidadArena.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_densidadArena.setFocus()
            self.nuevocalculo.lineEdit_densidadArena.setText("0")
            self.nuevocalculo.label_Error.setText("En la Densidad de Arena sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        
        elif DensidadMar ==False:
            self.nuevocalculo.lineEdit_DensidadMar.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_DensidadMar.setFocus()
            self.nuevocalculo.lineEdit_DensidadMar.setText("0")
            self.nuevocalculo.label_Error.setText("En la Densidad del Mar sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        
        elif CoeficienteP ==False:
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setFocus()
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setText("0")
            self.nuevocalculo.label_Error.setText("En el Coeficiente sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif altura ==False:
            self.nuevocalculo.lineEdit_altura.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_altura.setFocus()
            self.nuevocalculo.lineEdit_altura.setText("0")
            self.nuevocalculo.label_Error.setText("En la Altura sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif angulo ==False:
            self.nuevocalculo.lineEdit_AnguloRompiente.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_AnguloRompiente.setFocus()
            self.nuevocalculo.lineEdit_AnguloRompiente.setText("0")
            self.nuevocalculo.label_Error.setText("En el Ángulo sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif  indice ==False:
            self.nuevocalculo.lineEdit_IndiceRompiente.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_IndiceRompiente.setFocus()
            self.nuevocalculo.lineEdit_IndiceRompiente.setText("0")
            self.nuevocalculo.label_Error.setText("En el Índice sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif  ubicacion ==False:
            self.nuevocalculo.lineEdit_Ubicacion.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_Ubicacion.setFocus()
            self.nuevocalculo.lineEdit_Ubicacion.setText("")
            self.nuevocalculo.label_Error.setText("En la Ubicación sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        else:
           validando= True 
        return validando
    
    def EntrarNuevoCalculo(self):
        validando= self.validandocamposNuevoCalculo()
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()

        else:
            DensidadArena= float(self.nuevocalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.nuevocalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.nuevocalculo.lineEdit_altura.text())
            angulo=float(self.nuevocalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.nuevocalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.nuevocalculo.lineEdit_Ubicacion.text()
           

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                mBox= QMessageBox()
                if self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado):
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado))  
                    self.nuevocalculo.hide()
                    self.limpiarCamposNuevoCalculo()         
                else:
                    mBox.setText("Los Datos NO se Guardaron")
                mBox.exec()
    
    def boton_Cancelar_NuevoCalculo(self):
        self.nuevocalculo.close()
        self.limpiarCamposNuevoCalculo()
    
    def boton_guardar(self):
        return self.nuevocalculo.but_GuardarNuevoCalculo
    
    