from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtWidgets import QHeaderView
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import loadUi
from .nuevocalculo import NuevoCalculo
from .editarcalculo import EditarCalculo
from PyQt6 import QtCore,QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate
from data.tla import TLAData
from data.usuario import UsuarioData
from model.usuario import Usuario
from data.municipio import MunicipioData
from data.ubicacion import UbicacionData
from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from .mensaje import Mensaje
import ctypes
import pathlib

class PrincipalUsuario(QMainWindow):
    def __init__(self):
        #Iniciando Interfaz
        super(PrincipalUsuario,self).__init__()
        mod_path = pathlib.Path(__file__).parent
        loadUi(mod_path/"PrincipalUsuario.ui",self)
        
        #Calculos
        self.mostrar= TLAData()
        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()
        #Usuarios
        self.usuarioData=UsuarioData()
        #Municipio
        self.municipio= MunicipioData()
        #Ubicacion
        self.ubicaciondata=UbicacionData()

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageInicio))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageCalculo))
        self.button_Perfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageMiPerfil))

        #Mover la ventana y centrarla en el escritorio
        resolucion= ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=int((resolucion_ancho/2)-(self.frameSize().width()/2))
        top= int((resolucion_alto/2)-(self.frameSize().height()/2))
        self.move(left,top)

        #self.table_Calculos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.iniGUI()

        self.show()

    
    def iniGUI(self):
        self.button_Calculo.clicked.connect(self.mostrar_datos_tablaCalculos)
        self.button_Calculo.clicked.connect(self.LimpiarCamposBuscar)
        self.Button_SeleccionarMun.clicked.connect(self.Seleccionar)
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        self.button_CerrarS.clicked.connect(self.cerrarSesion)
        self.button_Perfil.clicked.connect(self.MiPerfil)
        self.buttonCambiarContrasena.clicked.connect(self.CambiarContrasena)
        miFecha= QDate(2023,12,1)
        self.dateEdit.setDate(miFecha) 
        self.dateEditHasta.setDate(miFecha) 
        self.Button_Buscar.clicked.connect(self.buscarCalculo)
    
    #Inciando la Interfaz de Mensaje
    def Mensaje(self):
        self.mensaje=Mensaje()

    def recibirInicio(self,inicio):
        self.inicio= inicio
    
    def recibirUsuario(self,usuario,id):
        self.idUsuario=id
        self.nombreUsuario= usuario
    
    def cerrarSesion(self):
        cerrar= self.eventos.cerroSesion()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= cerrar)
        self.trazadata.insertarTraza(self.trazas)

        self.close()
        self.inicio.show()
         
    def mostrar_datos_tablaCalculos(self):
        datos=self.mostrar.calculosUsuarioEspecifico(self.idUsuario)
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Calculos.setRowCount(i)
        tablerow=0

        for row in a:
            self.table_Calculos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Calculos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Calculos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Calculos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.table_Calculos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.table_Calculos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            self.table_Calculos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
            self.table_Calculos.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
            self.table_Calculos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[11]))
            self.table_Calculos.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[12]))
            self.table_Calculos.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[8]))
            self.table_Calculos.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[9]))
            tablerow += 1 
    
    def EliminarCalculo(self):
        rows=self.table_Calculos.selectionModel().selectedRows()
        
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para eliminar")
            self.mensaje.button()
        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.table_Calculos.item(i,0).text()
                self.table_Calculos.removeRow(i)
                self.tla= TLAData()
                self.tla.eliminar_datos_tla(id)
            
            eliminado= self.eventos.eliminarCalculo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)
    
    def EditarCalculo(self):
        self.mostrar= TLAData()
        rows=self.table_Calculos.selectionModel().selectedRows()
        
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para editar")
            self.mensaje.button()
        else:
            self.editarcalculoGUI()
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.table_Calculos.item(i,0).text()
                self.idx=self.mostrar.buscar_datos_tla_DI(id)
            
            print(self.idx)
            self.editarcalculo.mostrarDatosEditar(self.idx)
    
    ################# Nuevo  Calculo ##########        
    def nuevocalculo(self):
        #Llamando a la ventana NuevoCalculo
        self.nuevocalculo=NuevoCalculo()
        self.nuevocalculo.recibirUsuario(self.nombreUsuario,self.idUsuario)
        guardar=self.nuevocalculo.boton_guardar()
        guardar.clicked.connect(self.mostrar_datos_tablaCalculos)

    ################# Editar Calculo ##########
    def editarcalculoGUI(self):
        self.editarcalculo=EditarCalculo()
        actualizar=self.editarcalculo.boton_actualizar()
        actualizar.clicked.connect(self.mostrar_datos_tablaCalculos)
        nuevo=self.editarcalculo.boton_nuevo()
        nuevo.clicked.connect(self.mostrar_datos_tablaCalculos)
        self.editarcalculo.recibirUsuario(self.nombreUsuario,self.idUsuario)
    
    ######## BUSCAR CALCULO ##################
    def buscarCalculo(self):
        self.mostrar= TLAData()
        fechadesde= self.dateEdit.date().toPyDate()
        fechahasta=self.dateEditHasta.date().toPyDate()
        ubicacion= self.comboBox_2.currentText()
        
        if ubicacion== "":
            datos=self.mostrar.buscarPorFechaUsuario(fechadesde,fechahasta, self.idUsuario)
            self.Mostrar(datos)
        else:
            datos=self.mostrar.buscarPorFechaUbicUsuario(fechadesde,fechahasta, self.idUsuario,ubicacion)
            self.Mostrar(datos)
    
    def MostrarComboMunCalculo(self):
        datos=self.municipio.listaMunicipio()
        for item in datos:
            self.comboBox.addItem(item[1])
    
    def MostrarComboUbicCalculo(self):
        datos1= self.ubicaciondata.listaUbicaciones(self.comboBox.currentText())
        for item in datos1:
            self.comboBox_2.addItem(item[1])
    
    def LimpiarCamposBuscar(self):
        self.comboBox.clear()
        self.MostrarComboMunCalculo()
        self.comboBox_2.clear()


    def Seleccionar(self):
        if self.comboBox.currentText()=="Seleccione un Municipio":
            self.Mensaje()
            self.mensaje.label("Seleccione un Municipio")
            self.mensaje.button()
        else:
            self.comboBox_2.clear()
            self.MostrarComboUbicCalculo()



    
    def Mostrar(self,datos):
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Calculos.setRowCount(i)
        tablerow=0

        for row in a:
            self.table_Calculos.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Calculos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Calculos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Calculos.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.table_Calculos.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.table_Calculos.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            self.table_Calculos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
            self.table_Calculos.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
            self.table_Calculos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[11]))
            self.table_Calculos.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[12]))
            self.table_Calculos.setItem(tablerow,10,QtWidgets.QTableWidgetItem(row[8]))
            self.table_Calculos.setItem(tablerow,11,QtWidgets.QTableWidgetItem(row[9]))
            tablerow += 1 
       

    
    ################ MI PERFIL #############3
    def MiPerfil(self):
        self.label_MiPerfil.setText("")
        self.label_Nombre.setText("")
        self.label_PApellido.setText("")
        self.label_SApellido.setText("")
        
        self.usuario=self.usuarioData.buscarusuarioID(self.idUsuario)
        self.label_Nombre.setText(self.usuario[0][1])
        self.label_MiPerfil.setText(self.usuario[0][2])
        self.label_PApellido.setText(self.usuario[0][4])
        self.label_SApellido.setText(self.usuario[0][5])
        self.LimpiarCampos()
    
    def LimpiarCampos(self):
        self.lineEditContActual.clear()
        self.lineEditContNueva.clear()
        self.lineEditConfContr.clear()
    
    def CambiarContrasena(self):
        if self.lineEditContActual.text() == "" :
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()
        elif self.lineEditContNueva.text()== "" :
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()
        elif self.lineEditConfContr.text()=="":
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()

        elif self.lineEditContActual.text() != self.usuario[0][3]:
            self.Mensaje()
            self.mensaje.label("Contraseña  Actual es Incorrecta")
            self.mensaje.button()
        elif self.lineEditContNueva.text() != self.lineEditConfContr.text():
            self.Mensaje()
            self.mensaje.label("La Contraseña Nueva No Coincide con la Confirmada")
            self.mensaje.button()
        else:
            nombre=self.usuario[0][1]
            usuario=self.usuario[0][2]
            clave=self.lineEditContNueva.text()
            PApellido=self.usuario[0][4]
            SApellido=self.usuario[0][5]
            CI=self.usuario[0][6]
            correo=self.usuario[0][7]
            tipo=self.usuario[0][8]
            sexo=self.usuario[0][9]
            usuario=Usuario(nombre,usuario,clave,PApellido,SApellido,CI,correo,tipo,sexo)
            self.usuarioData.actualizarUsuario(usuario,self.idUsuario)

            self.Mensaje()
            self.mensaje.label("La Contraseña Actualizada con Éxito")
            self.mensaje.button()

            self.LimpiarCampos()
            eliminado= self.eventos.CambioContrasena()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)




