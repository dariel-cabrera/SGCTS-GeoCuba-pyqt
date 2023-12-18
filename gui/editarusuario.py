from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
from PyQt6 import QtWidgets, QtGui
from PyQt6 import QtCore,QtWidgets
from model.usuario import Usuario
from data.usuario import UsuarioData
from model.validarcampos import ValidarCampos

class EditarUsuario():
    def __init__(self):
        self.editarusuario=uic.loadUi("gui/editarUsuario.ui")
        self.iniGUI()
    
    def iniGUI(self):
        self.editarusuario.show()
    
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
    

