from PyQt6 import uic
from .mensaje import Mensaje
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 
from PyQt6 import QtWidgets, QtGui
from data.tla import TLAData
from PyQt6 import QtCore,QtWidgets
from model.validarcampos import ValidarCampos
from data.municipio import MunicipioData
from data.ubicacion import UbicacionData
from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from data.K import KData
from data.G import GData


class NuevoCalculo():
    def __init__(self):
        self.nuevocalculo=uic.loadUi("gui/nuevoCalculo.ui")
        self.iniGUI()

        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()

       
    
    def iniGUI(self):
        self.municipio= MunicipioData()
        self.ubicaciondata= UbicacionData()

        self.nuevocalculo.label_Error.setText("")
        self.nuevocalculo.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)
        self.nuevocalculo.butCancelarNuevoCalculo.clicked.connect(self.boton_Cancelar_NuevoCalculo)
        self.MostrarMunicipio()
        self.nuevocalculo.but_SeleccionarMunCalculo.clicked.connect(self.Seleccionar)
        self.K= KData()
        self.G=GData()
        self.nuevocalculo.show()
 
    def Mensaje(self):
        self.mensaje=Mensaje()

    
    def recibirUsuario(self,usuario,id):
        self.nombreUsuario=usuario
        self.idUsuario=id

    def limpiarCamposNuevoCalculo(self):
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_densidadArena.setText("")
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_CoeficientePorocidad.setText("")
        self.nuevocalculo.lineEdit_altura.setText("")
        self.nuevocalculo.lineEdit_AnguloRompiente.setText("")
        self.nuevocalculo.lineEdit_IndiceRompiente.setText("")
        self.nuevocalculo.comboBoxUbicCalculo.clear()
    
    def MostrarMunicipio(self):
        datos=self.municipio.listaMunicipio()
        for item in datos:
            self.nuevocalculo.comboBox.addItem(item[1])
    
    def MostrarUbicacion(self):
        datos1= self.ubicaciondata.listaUbicaciones(self.nuevocalculo.comboBox.currentText())
        print(datos1)
        for item in datos1:
            self.nuevocalculo.comboBoxUbicCalculo.addItem(item[1])  

    def Seleccionar(self):
        if self.nuevocalculo.comboBox.currentText()=="Seleccione un Municipio" :
            self.Mensaje()
            self.mensaje.label("Seleccione un Municipio")
            self.mensaje.button()
        else:
            self.nuevocalculo.comboBoxUbicCalculo.clear()
            self.MostrarUbicacion()


    def validandocamposNuevoCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()
        
      
        DensidadArena=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_IndiceRompiente.text())
        ubicacion=self.nuevocalculo.comboBoxUbicCalculo.currentText()

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

        elif  ubicacion =="Seleccione una Ubicación":
            self.nuevocalculo.comboBoxUbicCalculo.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.comboBoxUbicCalculo.setFocus()
            self.nuevocalculo.comboBoxUbicCalculo.clear()
            self.nuevocalculo.label_Error.setText("Seleccione una Ubicación ")
        else:
           validando= True 
        return validando
    
    def EntrarNuevoCalculo(self):
        validando= self.validandocamposNuevoCalculo()
        if validando==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos Verifíquelos")
            self.mensaje.button()

            datoError= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoError)
            self.trazadata.insertarTraza(self.trazas)

        else:
            DensidadArena= float(self.nuevocalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.nuevocalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.nuevocalculo.lineEdit_altura.text())
            angulo=float(self.nuevocalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.nuevocalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.nuevocalculo.comboBoxUbicCalculo.currentText()
            datos= self.K.mostrarK()
            datos1=self.G.mostrarG()

            K=[]
            for x in datos:
                K.append([float(i) for i in x])
            

            g=[]
            for x in datos1:
                g.append([float(i) for i in x])

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo,K[0][0],g[0][0])

            if resultado== False:
                self.Mensaje()
                self.mensaje.label("Verifíque los Datos la División por 0 no esta Permitida")
                self.mensaje.button()

                datoError= self.eventos.divisionporCero()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoError)
                self.trazadata.insertarTraza(self.trazas)

            else:
                self.tla= TLAData()
                if self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado,self.idUsuario,K[0][0],g[0][0]): 
                    self.Mensaje()
                    self.mensaje.label("Datos Guardados con Éxito Q="+ str(resultado))
                    self.mensaje.button()
                    self.nuevocalculo.hide()
                    self.limpiarCamposNuevoCalculo()  

                    editarCalculo= self.eventos.crearNuevoCalculo()
                    self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= editarCalculo)
                    self.trazadata.insertarTraza(self.trazas)       
                else:
                    pass
                    self.Mensaje()
                    self.mensaje.label("Los Datos NO se Guardaron")
                    self.mensaje.button()
                
    
    def boton_Cancelar_NuevoCalculo(self):
        self.nuevocalculo.close()
        self.limpiarCamposNuevoCalculo()
    
    def boton_guardar(self):
        return self.nuevocalculo.but_GuardarNuevoCalculo
    
    