
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import *
from data.usuario import UsuarioData
from model.usuario import Usuario
from .principal import Principal

class Login():
    def __init__(self):
        self.login=uic.loadUi("gui/login.ui")
        self.iniGUI()
        self.login.lbl_mensaje.setText("")
        self.login.show()
    
    def ingresar(self):
        if len(self.login.txtUsuario.text())<2:
            self.login.lbl_mensaje.setText("Ingrese un usuario válido")
        elif len(self.login.txtContrasena.text())<3:
             self.login.lbl_mensaje.setText("Ingrese una contraseña válida")
        else:
            self.login.lbl_mensaje.setText("")
            usu=Usuario(usuario=self.login.txtUsuario.text(),clave=self.login.txtContrasena.text())
            usuData=UsuarioData()
            res= usuData.login(usu)
            if res:
                 self.principal= Principal()
                 self.login.hide()
            else:
                self.login.lbl_mensaje.setText("Datos de acceso Incorrectos")
    
    def iniGUI(self):
        self.login.butEntrar.clicked.connect(self.ingresar) 
