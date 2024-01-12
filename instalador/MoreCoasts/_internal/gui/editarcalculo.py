from PyQt6 import uic
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from model.ecuaciones import transporte_logitudinal_arena 
from PyQt6 import QtWidgets, QtGui
from data.tla import TLAData
from .mensaje import Mensaje
from PyQt6 import QtCore,QtWidgets
from model.validarcampos import ValidarCampos
from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from data.K import KData
from data.G import GData
import pathlib

class EditarCalculo():
    def __init__(self):
        mod_path = pathlib.Path(__file__).parent
        self.editarcalculo=uic.loadUi(mod_path/"EditarCalculo.ui")
        self.iniGUI()

        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()
    
    def Mensaje(self):
        self.mensaje=Mensaje()

    def iniGUI(self):
        self.editarcalculo.label_Error.setText("")
        self.editarcalculo.butCancelarEditar.clicked.connect(self.boton_Cancelar_EditarCalculo)
        self.editarcalculo.but_ActualizarEditar.clicked.connect(self.entrarEditarCalculo)
        self.editarcalculo.but_NuevoEditar.clicked.connect(self.entrarNuevoEditarCalculo)
        self.K= KData()
        self.G= GData()
        self.editarcalculo.show()
    
    def recibirUsuario(self,usuario,id):
        self.nombreUsuario=usuario
        self.idUsuario=id

    def mostrarDatosEditar(self,idx):
        datos= idx
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        
        print(a)
        self.idEditar= a[0][0]
        self.ubicacion=a[0][1]
        self.editarcalculo.lineEdit_densidadArena.setText(a[0][3])
        self.editarcalculo.lineEdit_DensidadMar.setText(a[0][2])
        self.editarcalculo.lineEdit_CoeficientePorocidad.setText(a[0][4])
        self.editarcalculo.lineEdit_altura.setText(a[0][5])
        self.editarcalculo.lineEdit_AnguloRompiente.setText(a[0][6])
        self.editarcalculo.lineEdit_IndiceRompiente.setText(a[0][7])

        mostrar= self.eventos.mostrarEditar()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
        self.trazadata.insertarTraza(self.trazas)
    
    def boton_Cancelar_EditarCalculo(self):
        self.editarcalculo.hide()
        cancelar= self.eventos.CancelarEditar()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= cancelar)
        self.trazadata.insertarTraza(self.trazas)
   
    def validandocamposEditarCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()

        DensidadArena=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_IndiceRompiente.text())
        
        
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
        else:
            validando=True
        return validando

    def entrarEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos Verifíquelos")
            self.mensaje.button()

            datoError= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoError)
            self.trazadata.insertarTraza(self.trazas)
        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            datos= self.K.mostrarK()
            datos1=self.G.mostrarG()

            self.K=[]
            for x in datos:
                self.K.append([float(i) for i in x])
            

            self.g=[]
            for x in datos1:
                self.g.append([float(i) for i in x])
            
        
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo,self.K[0][0],self.g[0][0])
            
            if resultado== False:
                self.Mensaje()
                self.mensaje.label("Verifíque los Datos la División por 0 no esta Permitida")
                self.mensaje.button()

                datoError= self.eventos.divisionporCero()
                self.trazas=Trazas(nombreUsuario=self.nombreUsuario,evento= datoError)
                self.trazadata.insertarTraza(self.trazas)
            else:
                self.tla= TLAData()
                actualizar=self.tla.actualizar_datos_tla(self.idEditar,self.ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado,self.K[0][0],self.g[0][0])

                if actualizar==1:
                    self.Mensaje()
                    self.mensaje.label("Datos Guardados con Éxito Q="+ str(resultado))
                    self.mensaje.button()

                    self.editarcalculo.close()
    

                    editarCalculo= self.eventos.editarCalculo()
                    self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= editarCalculo)
                    self.trazadata.insertarTraza(self.trazas)

                else:
                    self.Mensaje()
                    self.mensaje.label("Los Datos NO se Guardaron")
                    self.mensaje.button()

                    noguardado= self.eventos.datosNoGuardados()
                    self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= noguardado)
                    self.trazadata.insertarTraza(self.trazas)
        

    def entrarNuevoEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos Verifíquelos")
            self.mensaje.button()

            datoError= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoError)
            self.trazadata.insertarTraza(self.trazas)

        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            datos= self.K.mostrarK()
            datos1=self.G.mostrarG()

            self.K=[]
            for x in datos:
                self.K.append([float(i) for i in x])
            

            self.g=[]
            for x in datos1:
                self.g.append([float(i) for i in x])
            
        
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo,self.K[0][0],self.g[0][0])
            
            if resultado== False:
                self.Mensaje()
                self.mensaje.label("Verifíque los Datos la División por 0 no esta Permitida")
                self.mensaje.button()

                datoError= self.eventos.divisionporCero()
                self.trazas=Trazas(nombreUsuario=self.nombreUsuario,evento= datoError)
                self.trazadata.insertarTraza(self.trazas)
            else:
                self.tla= TLAData()
                actualizar=self.tla.insertar_datos_tla(self.ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado,self.idUsuario,self.K[0][0],self.g[0][0])

                if actualizar==1:
                    self.Mensaje()
                    self.mensaje.label("Datos Guardados con Éxito Q="+ str(resultado))
                    self.mensaje.button()
                    self.editarcalculo.close()
                    

                    editarCalculo= self.eventos.crearEditarCalculo()
                    self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= editarCalculo)
                    self.trazadata.insertarTraza(self.trazas)
        
                else:
                    self.Mensaje()
                    self.mensaje.label("Los Datos NO se Guardaron")
                    self.mensaje.button()

                    noguardado= self.eventos.datosNoGuardados()
                    self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= noguardado)
                    self.trazadata.insertarTraza(self.trazas)

                  
    def boton_actualizar(self):
        return self.editarcalculo.but_ActualizarEditar
    
    def boton_nuevo(self):
        return self.editarcalculo.but_NuevoEditar
    
   