from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from data.usuario import UsuarioData
from model.usuario import Usuario
from .principal import Principal
from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from .principalusuario import PrincipalUsuario

class Login():
    def __init__(self):
        self.login=uic.loadUi("gui/login.ui")
        self.iniGUI()
        self.login.lbl_mensaje.setText("")
        self.login.show()
        self.eventos=Evento()
        self.trazadata= TrazaData()
    
    def LimpiarCampos(self):
        self.login.txtUsuario.setText("")
        self.login.txtContrasena.setText("")

    def ingresar(self):
        if len(self.login.txtUsuario.text())<2:
            self.login.lbl_mensaje.setText("Ingrese un usuario válido")
        elif len(self.login.txtContrasena.text())<3:
             self.login.lbl_mensaje.setText("Ingrese una contraseña válida")
        else:
            self.login.lbl_mensaje.setText("")
            usu=Usuario(usuario=self.login.txtUsuario.text(),clave=self.login.txtContrasena.text())
            self.usuData=UsuarioData()
            self.res= self.usuData.login(usu)
            self.trazas=Traza()
        
            if self.res:
                autenticado=self.eventos.autenticarse()
                self.trazas= Traza(nombreUsuario=self.login.txtUsuario.text(),evento=autenticado)
                self.trazadata.insertarTraza(self.trazas)
                if self.login.txtUsuario.text()== "Admin" :
                    self.principal= Principal()
                   
                    self.principal.recibirInicio(self.login)
                    self.principal.recibirUsuario(self.login.txtUsuario.text(),self.res._nombre)
                    
                    self.LimpiarCampos()
                    self.login.close()
                else:
                    self.principalusuario=PrincipalUsuario()
                    self.principalusuario.recibirInicio(self.login)
                    
        
                    self.principalusuario.recibirUsuario(self.login.txtUsuario.text(),self.res._nombre)
                    self.LimpiarCampos()
                    self.login.close()
                          
            else:
                self.login.lbl_mensaje.setText("Datos de acceso Incorrectos")
                autenticado=self.eventos.autenticacionError()
                self.trazas= Traza(nombreUsuario=self.login.txtUsuario.text(),evento=autenticado)
                self.trazadata.insertarTraza(self.trazas)
    
    def iniGUI(self):
        self.login.butEntrar.clicked.connect(self.ingresar) 
