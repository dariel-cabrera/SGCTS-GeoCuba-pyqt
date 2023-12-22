
class Evento():
    def __init__(self):
        pass

    def autenticarse(self):
        self.autenticado= "Se autenticó "
        return self.autenticado
    
    def autenticacionError(self):
        self.autenticacionError="Autenticacion Erronea"
        return self.autenticacionError
    
    def crearNuevoCalculo(self):
        self.crearcalculo="Creó un Nuevo Calculo"
        return self.crearcalculo
    
    def CancelarNuevoCalculo(self):
        self.Cancelar= "Canceló Nuevo Cálculo"
        return self.Cancelar

    def editarCalculo(self):
        self.editarCalculo="Editó un cálculo"
        return self.editarCalculo
    
    def mostrarEditar(self):
        self.mostrarEditar="Se mostró los datos para Editar"
        return self.mostrarEditar
    
    def crearEditarCalculo(self):
        self.editarCalculo="Creó un Cálculo con Editar "
        return self.editarCalculo
    
    def CancelarEditar(self):
        self.cancelar="Canceló la Edición"
        return self.cancelar
    
    
    def eliminarCalculo(self):
        self.eliminarCalculo="Eliminó un Cálculo"
        return self.eliminarCalculo
    
    def datoErroneo(self):
        self.datoErroneo="Entró un dato Erroneo"
        return self.datoErroneo
    
    def datosNoGuardados(self):
        self.datosNoGuardados="Los Datos no se Guardaron"
        return self.datosNoGuardados
    
    def  divisionporCero(self):
        self.divisionporCero="Intentó dividir por 0"
        return self.divisionporCero
    
    
    def eliminoUsuario(self):
        self.eliminoUsuario="Eliminó un Usuario"
        return self.eliminoUsuario
    
    def mostrarDatosUsuario(self):
        self.mostrarDatosUsuario="Mostró Datos de Usuario"
        return self.mostrarDatosUsuario

    def datoErroneousuario(self):
        self.datoErroneo="Entró un dato Erroneo al entrar Usuario"
        return self.datoErroneo
    
    def CreoUsuario(self):
        self.creoUsuario="Creó Usuario"
        return self.creoUsuario
    
    def cancelarNuevoUsuario(self):
        self.cancelar="Canceló Nuevo Usuario"
        return self.cancelar

    def actualizarUsuario(self):
        self.actualizarUsuario="Actualizó Usuario"
        return self.actualizarUsuario
    
    def cancelarEditarUsuario(self):
        self.cancelar="Canceló Editar Usuario"
        return self.cancelar
    
    def CambioContrasena(self):
        self.cambiocontrasena="Cambió Contraseña"
        return self.cambiocontrasena


    def cerroSesion(self):
        self.cerroSesion= "Cerró Sesión"
        return self.cerroSesion
        