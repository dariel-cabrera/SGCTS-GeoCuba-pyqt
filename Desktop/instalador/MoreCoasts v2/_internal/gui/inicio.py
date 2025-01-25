from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from data.usuario import UsuarioData
from model.usuario import Usuario
from .principal import Principal
from model.traza import Traza
from model.eventos import Evento
import pathlib
from data.Trazas import TrazaData
from .principalusuario import PrincipalUsuario

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        mod_path = pathlib.Path(__file__).parent
        loadUi(mod_path/"login.ui",self)
        self.iniGUI()
        self.lbl_mensaje.setText("")
        self.show()
        self.eventos=Evento()
        self.trazadata= TrazaData()
        self.usuData=UsuarioData()
    
    def LimpiarCampos(self):
        self.txtUsuario.setText("")
        self.txtContrasena.setText("")

    def ingresar(self):
        if len(self.txtUsuario.text())<2:
            self.lbl_mensaje.setText("Ingrese un usuario válido")
        elif len(self.txtContrasena.text())<3:
             self.lbl_mensaje.setText("Ingrese una contraseña válida")
        else:
            self.lbl_mensaje.setText("")
            usu=Usuario(usuario=self.txtUsuario.text(),clave=self.txtContrasena.text())
            self.res= self.usuData.login(usu)
            self.trazas=Traza()
        
            if self.res:
                autenticado=self.eventos.autenticarse()
                self.trazas= Traza(nombreUsuario=self.txtUsuario.text(),evento=autenticado)
                self.trazadata.insertarTraza(self.trazas)
                if self.txtUsuario.text()== "Admin" :
                    self.principal= Principal()
                   
                    self.principal.recibirInicio(self)
                    self.principal.recibirUsuario(self.txtUsuario.text(),self.res._nombre)
                    
                    self.LimpiarCampos()
                    self.close()
                else:
                    self.principalusuario=PrincipalUsuario()
                    self.principalusuario.recibirInicio(self)
                    
        
                    self.principalusuario.recibirUsuario(self.txtUsuario.text(),self.res._nombre)
                    self.LimpiarCampos()
                    self.close()
                          
            else:
                self.lbl_mensaje.setText("Datos de acceso Incorrectos")
                autenticado=self.eventos.autenticacionError()
                self.trazas= Traza(nombreUsuario=self.txtUsuario.text(),evento=autenticado)
                self.trazadata.insertarTraza(self.trazas)
    
    def iniGUI(self):
        self.butEntrar.clicked.connect(self.ingresar) 
