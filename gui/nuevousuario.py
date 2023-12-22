from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore,QtWidgets
from model.usuario import Usuario
from data.usuario import UsuarioData
from model.validarcampos import ValidarCampos
from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData

class NuevoUsuario():
    def __init__(self):
        self. nuevousuario=uic.loadUi("gui/nuevoUsuario.ui")
        self.iniGUI()

        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()
       
    
    def iniGUI(self):
        self.nuevousuario.label_Error.setText("")
        self.nuevousuario.but_CrearrNuevoUsuario.clicked.connect(self.EntrarNuevoUsuario)
        self.nuevousuario.butCancelarNuevoUsuario.clicked.connect(self.bt_Cancelar)
        self.nuevousuario.show()
    
    def recibirUsuario(self,usuario):
        self.nombreUsuario=usuario
    

    def validandonuevousuario(self):
        validando=False
        self.validarcampo=ValidarCampos()

        nombre=self.validarcampo.validarCamposNombre(self.nuevousuario.lineEdit_Nombre.text())
        primerapellido=self.validarcampo.validarCamposNombre(self.nuevousuario.lineEdit_PrimerApellido.text())
        segundoapellido=self.validarcampo.validarCamposNombre(self.nuevousuario.lineEdit_SegundoApellido.text())
        CI=self.validarcampo.validarInt(self.nuevousuario.lineEdit_CI.text())
        sexo=self.nuevousuario.comboBox.currentText()
        tipo=self.validarcampo.validarCamposNombre(self.nuevousuario.lineEdit_TipoTrabajador.text())
        correo=self.validarcampo.validarEmail(self.nuevousuario.lineEdit_Correo.text())
        usuario=self.nuevousuario.lineEdit_NombreUsuario.text()
        contrasena=self.nuevousuario.lineEdit_Contrasena.text()
        confirmarContrasena=self.nuevousuario.lineEdit_ConfirmarConstrasena.text()

        if nombre== False:
            self.nuevousuario.lineEdit_Nombre.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_Nombre.setFocus()
            self.nuevousuario.lineEdit_Nombre.setText("")
            self.nuevousuario.label_Error.setText("En el Nombre sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif primerapellido==False:
            self.nuevousuario.lineEdit_PrimerApellido.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_PrimerApellido.setFocus()
            self.nuevousuario.lineEdit_PrimerApellido.setText("")
            self.nuevousuario.label_Error.setText("En el Primer Apellido sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif segundoapellido==False:
            self.nuevousuario.lineEdit_SegundoApellido.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_SegundoApellido.setFocus()
            self.nuevousuario.lineEdit_SegundoApellido.setText("")
            self.nuevousuario.label_Error.setText("En el Segundo Apellido sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif CI==False:
            self.nuevousuario.lineEdit_CI.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_CI.setFocus()
            self.nuevousuario.lineEdit_CI.setText("")
            self.nuevousuario.label_Error.setText("En el CI sólo puede entrar numeros, texto 11 digitos y no puede entrar campos vacios")
        elif len(self.nuevousuario.lineEdit_CI.text()) != 11:
            self.nuevousuario.lineEdit_CI.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_CI.setFocus()
            self.nuevousuario.lineEdit_CI.setText("")
            self.nuevousuario.label_Error.setText("En el CI sólo puede entrar numeros, texto 11 digitos y no puede entrar campos vacios")
        elif sexo=="Seleccione una opción":
            self.nuevousuario.comboBox.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.comboBox.setFocus()
            self.nuevousuario.label_Error.setText("En el sexo eliga una opción")
        elif tipo==False:
            self.nuevousuario.lineEdit_TipoTrabajador.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_TipoTrabajador.setFocus()
            self.nuevousuario.lineEdit_TipoTrabajador.setText("")
            self.nuevousuario.label_Error.setText("En el Tipo de Trabajador sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif correo==False:
            self.nuevousuario.lineEdit_Correo.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_Correo.setFocus()
            self.nuevousuario.lineEdit_Correo.setText("")
            self.nuevousuario.label_Error.setText("Debe entrar un correo válido y no puede entrar campos vacios")

        elif usuario=="":
            self.nuevousuario.lineEdit_NombreUsuario.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_NombreUsuario.setFocus()
            self.nuevousuario.lineEdit_NombreUsuario.setText("")
            self.nuevousuario.label_Error.setText("En el usuario no puede entrar campos vacios")
            
        elif contrasena=="" and confirmarContrasena=="":
            self.nuevousuario.lineEdit_Contrasena.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_ConfirmarConstrasena.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_Contrasena.setFocus()
            self.nuevousuario.label_Error.setText("Debe introduccir una contraseña y confirmarla")
        
        elif not contrasena== confirmarContrasena:
            self.nuevousuario.lineEdit_Contrasena.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_ConfirmarConstrasena.setStyleSheet("border: 1px solid red;")
            self.nuevousuario.lineEdit_Contrasena.setFocus()
            self.nuevousuario.lineEdit_Contrasena.setText("")
            self.nuevousuario.label_Error.setText("La Contraseñas no Coinciden")
        else:
            validando=True
        return validando
    
    def EntrarNuevoUsuario(self):
        validando=self.validandonuevousuario()
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()

            datoErroneo=self.eventos.datoErroneousuario()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoErroneo)
            self.trazadata.insertarTraza(self.trazas)
        else:
            nombre=self.nuevousuario.lineEdit_Nombre.text()
            primerapellido=self.nuevousuario.lineEdit_PrimerApellido.text()
            segundoapellido=self.nuevousuario.lineEdit_SegundoApellido.text()
            CI=self.nuevousuario.lineEdit_CI.text()
            sexo=self.nuevousuario.comboBox.currentText()
            tipo=self.nuevousuario.lineEdit_TipoTrabajador.text()
            correo=self.nuevousuario.lineEdit_Correo.text()
            usuario=self.nuevousuario.lineEdit_NombreUsuario.text()
            contrasena=self.nuevousuario.lineEdit_Contrasena.text()

            self.usu=Usuario(nombre,usuario,contrasena,primerapellido,segundoapellido,CI,correo,tipo,sexo)
            usuData=UsuarioData()
            print(self.usu)
            confirmar=usuData.crearUsuario(self.usu)
            print(confirmar)
            if confirmar==True:
                mBox= QMessageBox()
                mBox.setText("Datos Guardados con Éxitos")
                mBox.exec()
                self.limpiarlosCamposNuevoUsuario()
                self.nuevousuario.close()

                mostrar= self.eventos.CreoUsuario()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
                self.trazadata.insertarTraza(self.trazas)

            else:
                mBox= QMessageBox()
                mBox.setText("No se  Guardaron, El Nombre de Usuario o CI ya está Registrado ")
                mBox.exec()
    
    def limpiarlosCamposNuevoUsuario(self):
        nombre=self.nuevousuario.lineEdit_Nombre.clear()
        primerapellido=self.nuevousuario.lineEdit_PrimerApellido.clear()
        segundoapellido=self.nuevousuario.lineEdit_SegundoApellido.clear()
        CI=self.nuevousuario.lineEdit_CI.clear()
        sexo=self.nuevousuario.comboBox.currentText()
        tipo=self.nuevousuario.lineEdit_TipoTrabajador.clear()
        correo=self.nuevousuario.lineEdit_Correo.clear()
        usuario=self.nuevousuario.lineEdit_NombreUsuario.clear()
        contrasena=self.nuevousuario.lineEdit_Contrasena.clear()

    def bt_Cancelar(self):
        self.limpiarlosCamposNuevoUsuario()
        self.nuevousuario.close()
        mostrar= self.eventos.cancelarNuevoUsuario()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
        self.trazadata.insertarTraza(self.trazas)
    
    def buton_GuardarUsuario(self):
        return self.nuevousuario.but_CrearrNuevoUsuario