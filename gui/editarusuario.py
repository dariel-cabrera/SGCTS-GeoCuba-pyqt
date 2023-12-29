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

class EditarUsuario():
    def __init__(self):
        self.editarusuario=uic.loadUi("gui/editarUsuario.ui")
        self.iniGUI()

        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()
    
    def iniGUI(self):
        self.usuariodata=UsuarioData()
        self.editarusuario.label_Error.setText("")
        self.editarusuario.but_actualizarUsuario.clicked.connect(self.actualizarUsuario)
        self.editarusuario.butCancelarEditarUsuario.clicked.connect(self.bt_Cancelar)
        self.editarusuario.show()
    
    def recibirUsuario(self,usuario):
        self.nombreUsuario= usuario
    
    def mostrarDatos(self,idx):
        datos=idx
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        self.idUsuario= a[0][0]
        self.CI=a[0][6]
        self.editarusuario.lineEdit_NombreUsuario.setText(a[0][2])
        self.editarusuario.lineEdit_Nombre.setText(a[0][1])
        self.clave=a[0][3]
        self.editarusuario.lineEdit_PrimerApellido.setText(a[0][4])
        self.editarusuario.lineEdit_SegundoApellido.setText(a[0][5])
        self.editarusuario.lineEdit_Correo.setText(a[0][7])
        self.editarusuario.lineEdit_TipoTrabajador.setText(a[0][8])
        self.sexo=a[0][9]

        mostrar= self.eventos.mostrarDatosUsuario()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
        self.trazadata.insertarTraza(self.trazas)


    
    def validandoeditarusuario(self):
        validando=False
        self.validarcampo=ValidarCampos()

        nombre=self.validarcampo.validarCamposNombre(self.editarusuario.lineEdit_Nombre.text())
        primerapellido=self.validarcampo.validarCamposNombre(self.editarusuario.lineEdit_PrimerApellido.text())
        segundoapellido=self.validarcampo.validarCamposNombre(self.editarusuario.lineEdit_SegundoApellido.text())
        tipo=self.validarcampo.validarCamposNombre(self.editarusuario.lineEdit_TipoTrabajador.text())
        correo=self.validarcampo.validarEmail(self.editarusuario.lineEdit_Correo.text())
        usuario=self.editarusuario.lineEdit_NombreUsuario.text()
        contrasena=self.editarusuario.lineEdit_Contrasena.text()
        confirmarContrasena=self.editarusuario.lineEdit_ConfirmarConstrasena.text()

        if nombre== False:
            self.editarusuario.lineEdit_Nombre.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_Nombre.setFocus()
            self.editarusuario.lineEdit_Nombre.setText("")
            self.editarusuario.label_Error.setText("En el Nombre sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif primerapellido==False:
            self.editarusuario.lineEdit_PrimerApellido.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_PrimerApellido.setFocus()
            self.editarusuario.lineEdit_PrimerApellido.setText("")
            self.editarusuario.label_Error.setText("En el Primer Apellido sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif segundoapellido==False:
            self.editarusuario.lineEdit_SegundoApellido.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_SegundoApellido.setFocus()
            self.editarusuario.lineEdit_SegundoApellido.setText("")
            self.editarusuario.label_Error.setText("En el Segundo Apellido sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        
        elif tipo==False:
            self.editarusuario.lineEdit_TipoTrabajador.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_TipoTrabajador.setFocus()
            self.editarusuario.lineEdit_TipoTrabajador.setText("")
            self.editarusuario.label_Error.setText("En el Tipo de Trabajador sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        elif correo==False:
            self.editarusuario.lineEdit_Correo.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_Correo.setFocus()
            self.editarusuario.lineEdit_Correo.setText("")
            self.editarusuario.label_Error.setText("Debe entrar un correo válido y no puede entrar campos vacios")

        elif usuario=="":
            self.editarusuario.lineEdit_NombreUsuario.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_NombreUsuario.setFocus()
            self.editarusuario.lineEdit_NombreUsuario.setText("")
            self.editarusuario.label_Error.setText("En el usuario no puede entrar campos vacios")
            
        elif contrasena=="" and confirmarContrasena=="":
            self.editarusuario.lineEdit_Contrasena.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_ConfirmarConstrasena.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_Contrasena.setFocus()
            self.editarusuario.label_Error.setText("Debe introduccir una contraseña y confirmarla")
        
        elif not contrasena== confirmarContrasena:
            self.editarusuario.lineEdit_Contrasena.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_ConfirmarConstrasena.setStyleSheet("border: 1px solid red;")
            self.editarusuario.lineEdit_Contrasena.setFocus()
            self.editarusuario.lineEdit_Contrasena.setText("")
            self.editarusuario.label_Error.setText("La Contraseñas no Coinciden")
        else:
            validando=True
        return validando
    
    def actualizarUsuario(self):
        validando=self.validandoeditarusuario()
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verifíquelos ")
            mBox.exec()

            datoErroneo=self.eventos.datoErroneousuario()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoErroneo)
            self.trazadata.insertarTraza(self.trazas)

        else:
            nombre=self.editarusuario.lineEdit_Nombre.text()
            primerapellido=self.editarusuario.lineEdit_PrimerApellido.text()
            segundoapellido=self.editarusuario.lineEdit_SegundoApellido.text()
            CI=self.CI
            sexo=self.sexo
            tipo=self.editarusuario.lineEdit_TipoTrabajador.text()
            correo=self.editarusuario.lineEdit_Correo.text()
            usuario=self.editarusuario.lineEdit_NombreUsuario.text()
            contrasena=self.editarusuario.lineEdit_Contrasena.text()

            self.usu=Usuario(nombre,usuario,contrasena,primerapellido,segundoapellido,CI,correo,tipo,sexo)
            confirmar= self.usuariodata.actualizarUsuario(self.usu,self.idUsuario)
            
            if confirmar==True:
                mBox= QMessageBox()
                mBox.setText("Datos Guardados con Éxitos")
                mBox.exec()
                self.editarusuario.close()

                mostrar= self.eventos.actualizarUsuario()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
                self.trazadata.insertarTraza(self.trazas)

            else:
                mBox= QMessageBox()
                mBox.setText("No se  Guardaron, El Nombre de Usuario ya está en el Sistema ")
                mBox.exec()
    
    def bt_Cancelar(self):
        self.editarusuario.close()
        mostrar= self.eventos.cancelarEditarUsuario()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= mostrar)
        self.trazadata.insertarTraza(self.trazas)
    
    def bt_actualizar(self):
        return  self.editarusuario.but_actualizarUsuario
    
