from PyQt6.QtWidgets import QMessageBox
import re

class ValidarCampos():
    

    def validarCamposfloat(self,campo):
        validando=False
        validarcampo=re.match('^[0-9\.]+$',campo,re.I)
        if campo=="":
           return validando
        elif not  validarcampo:
            return validando
        elif float(campo)<=0:
            return validando
        else:
            validando=True

        return validando

    def validarCamposNombre(self,campo):
        validarNombre=re.match('^[a-z A-Z\sÀÈÌÒÙáéíóúàèìòùäëïüöÑñ]+$',campo,re.I)
        if campo=="":
           return False
        
        elif not validarNombre:
            return False
        
        elif len(campo)<=2:
            return False
        else:
            return True
    
    def validarInt(self,campo):
        validando=False
        validarcampo=re.match('^[0-9]+$',campo,re.I)
        if campo=="":
           return validando
        elif not  validarcampo:
            return validando
        elif float(campo)<=0:
            return validando
        else:
            validando=True
        return validando
    
    def validarEmail(self,campo):
        validando=False
        validarcampo=re.match(r"[^@]+@[^@]+\.[^@]+",campo,re.I)
        if campo=="":
            return validando
        elif not validarcampo:
            return validando
        else:
            validando=True
        return validando
