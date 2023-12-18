from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 
from PyQt6 import QtWidgets, QtGui
from data.tla import TLAData
from PyQt6 import QtCore,QtWidgets
from model.validarcampos import ValidarCampos

class EditarCalculo():
    def __init__(self):
        self.editarcalculo=uic.loadUi("gui/EditarCalculo.ui")
        self.iniGUI()
    
    def iniGUI(self):
        self.editarcalculo.label_Error.setText("")
        self.editarcalculo.butCancelarEditar.clicked.connect(self.boton_Cancelar_EditarCalculo)
        self.editarcalculo.but_ActualizarEditar.clicked.connect(self.entrarEditarCalculo)
        self.editarcalculo.but_NuevoEditar.clicked.connect(self.entrarNuevoEditarCalculo)
        self.editarcalculo.show()

    def mostrarDatosEditar(self,idx):
        datos= idx
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        self.idEditar= a[0][0]
        self.editarcalculo.lineEdit_Ubicacion.setText(a[0][1])
        self.editarcalculo.lineEdit_densidadArena.setText(a[0][3])
        self.editarcalculo.lineEdit_DensidadMar.setText(a[0][2])
        self.editarcalculo.lineEdit_CoeficientePorocidad.setText(a[0][4])
        self.editarcalculo.lineEdit_altura.setText(a[0][5])
        self.editarcalculo.lineEdit_AnguloRompiente.setText(a[0][6])
        self.editarcalculo.lineEdit_IndiceRompiente.setText(a[0][7])
    
    def boton_Cancelar_EditarCalculo(self):
        self.editarcalculo.hide()
   
    def validandocamposEditarCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()

        DensidadArena=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_IndiceRompiente.text())
        ubicacion=self.validarcampo.validarCamposNombre(self.editarcalculo.lineEdit_Ubicacion.text())
        
        if DensidadArena==False:
            self.editarcalculo.lineEdit_densidadArena.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_densidadArena.setFocus()
            self.editarcalculo.lineEdit_densidadArena.setText("0")
            self.editarcalculo.label_Error.setText("En la Densidad de Arena sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif DensidadMar ==False:
            self.editarcalculo.lineEdit_DensidadMar.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_DensidadMar.setFocus()
            self.editarcalculo.lineEdit_DensidadMar.setText("0")
            self.editarcalculo.label_Error.setText("En la Densidad del Mar sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif CoeficienteP ==False:
            self.editarcalculo.lineEdit_CoeficientePorocidad.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_CoeficientePorocidad.setFocus()
            self.editarcalculo.lineEdit_CoeficientePorocidad.setText("0")
            self.editarcalculo.label_Error.setText("En el Coeficiente sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif altura ==False:
            self.editarcalculo.lineEdit_altura.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_altura.setFocus()
            self.editarcalculo.lineEdit_altura.setText("0")
            self.editarcalculo.label_Error.setText("En la Altura sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif angulo ==False:
            self.editarcalculo.lineEdit_AnguloRompiente.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_AnguloRompiente.setFocus()
            self.editarcalculo.lineEdit_AnguloRompiente.setText("0")
            self.editarcalculo.label_Error.setText("En el Ángulo sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif indice ==False:
            self.editarcalculo.lineEdit_IndiceRompiente.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_IndiceRompiente.setFocus()
            self.editarcalculo.lineEdit_IndiceRompiente.setText("0")
            self.editarcalculo.label_Error.setText("En el Índice sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif ubicacion ==False:
            self.editarcalculo.lineEdit_Ubicacion.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_Ubicacion.setFocus()
            self.editarcalculo.lineEdit_Ubicacion.setText("")
            self.editarcalculo.label_Error.setText("En la Ubicación sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        else:
            validando=True
        return validando

    def entrarEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()
        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.editarcalculo.lineEdit_Ubicacion.text()
            
           
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                actualizar=self.tla.actualizar_datos_tla(self.idEditar,ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado)

                if actualizar==1:
                    mBox= QMessageBox()
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado))  

                    self.editarcalculo.close()
                    mBox.exec()
                else:
                    mBox= QMessageBox()
                    mBox.setText("Los Datos NO se Guardaron")
                    mBox.exec()
        

    def entrarNuevoEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()
        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.editarcalculo.lineEdit_Ubicacion.text()
            
           
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                actualizar=self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado)

                if actualizar==1:
                    mBox= QMessageBox()
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado)) 
                    self.editarcalculo.close()
                    mBox.exec()
                else:
                    mBox= QMessageBox()
                    mBox.setText("Los Datos NO se Guardaron")
                    mBox.exec()
        
    def boton_actualizar(self):
        return self.editarcalculo.but_ActualizarEditar
    
    def boton_nuevo(self):
        return self.editarcalculo.but_NuevoEditar