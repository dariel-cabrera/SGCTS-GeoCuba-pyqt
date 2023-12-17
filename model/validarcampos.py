from PyQt6.QtWidgets import QMessageBox
import re

class ValidarCampos():
    

    def validarCamposfloat(self,campo):
        validarcampo=re.match('^[0-9\.]+$',campo,re.I)
        if campo=="":
            mBox= QMessageBox()
            mBox.setText("No se pueden entrar campos Vacios")
            mBox.exec()
            return False
        
        elif not  validarcampo:
            mBox= QMessageBox()
            mBox.setText("Sólo Puede Entrar Numeros")
            mBox.exec()
            return False
        
        elif float(campo)<=0:
            mBox= QMessageBox()
            mBox.setText("Debe entrar un Dato Mayor a 0 ")
            mBox.exec()
            return False
        else:
            return True

    def validarCamposNombre(self,campo):
        validarNombre=re.match('^[a-z A-Z\sÀÈÌÒÙáéíóúàèìòùäëïüö]+$',campo,re.I)
        if campo=="":
            mBox= QMessageBox()
            mBox.setText("No se pueden entrar campos Vacios")
            mBox.exec()
            return False
        
        elif not validarNombre:
            mBox= QMessageBox()
            mBox.setText("Sólo Puede Entrar Letras")
            mBox.exec()
            return False
        
        elif len(campo)<=2:
            mBox= QMessageBox()
            mBox.setText("Debe entrar un nombre con texto mayor a 2 ")
            mBox.exec()
            return False
        else:
            return True
