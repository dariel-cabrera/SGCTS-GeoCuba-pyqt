import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView 
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve 
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import loadUi
from PyQt6 import uic
from PyQt6.QtCore import QDate
from data.tla import TLAData
from .nuevocalculo import NuevoCalculo
from .editarcalculo import EditarCalculo
from .nuevousuario import NuevoUsuario
from model.usuario import Usuario
from data.usuario import UsuarioData
from .editarusuario import EditarUsuario
from data.municipio import MunicipioData
from data.ubicacion import UbicacionData
from model.validarcampos import ValidarCampos
import ctypes

from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from data.K import KData
from data.G import GData
from .mensaje import Mensaje
import pathlib

class Principal(QMainWindow):
    def __init__(self):
        #Iniciando
        super(Principal,self).__init__()
        mod_path = pathlib.Path(__file__).parent
        loadUi(mod_path/"principal.ui",self)

        #Fecha Por Defecto
        miFecha= QDate(2023,1,1)
        self.dateEditTrazaDesde.setDate(miFecha)
        self.dateEditTrazaHasta.setDate(miFecha)
        self.dateDesdeCalculo.setDate(miFecha)
        self.dateHastaCalculo.setDate(miFecha)

        #Llamando a la funcion Mover Menu
        self.but_mover.clicked.connect(self.mover_menu)

        #SizeGrip
        self.gripSize=100
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        #Mover la ventana y centrarla en el escritorio
        resolucion= ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=int((resolucion_ancho/2)-(self.frameSize().width()/2))
        top= int((resolucion_alto/2)-(self.frameSize().height()/2))
        self.move(left,top)

        # Mover ventana
        #self.frame_superior.mouseMoveEvent= self.mover_ventana

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Usuario))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))
        self.button_MiPerfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_MiPerfil))

        

        #Llamando a la Funcion iniGUi()
        self.iniGUI()

        #Mostrando La Ventana a Normal
        self.showNormal()

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)
    
    #Funcion para recibir el nombre y el id del usuario que esta interactuando 
    def recibirUsuario(self,usuario,id):
        self.idUsuario=id
        self.nombreUsuario= usuario
    
    #Funcion para recibir un objeto de la Interfaz Inicio 
    def recibirInicio(self,inicio):
        self.inicio= inicio
    
    #Cerrar Sesion de la Ventana
    def cerrarSesion(self):
        #Traza
        cerrar= self.eventos.cerroSesion()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= cerrar)
        self.trazadata.insertarTraza(self.trazas)

        self.close()
        self.inicio.show()

        


 ######################  Principal ###########################   
    def iniGUI(self):
        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()

        
        
        # Ubicacion
        self.ubicaciondata=UbicacionData()
        # Validar Campos
        self.validar= ValidarCampos()
        #Usuarios
        self.usuarioData=UsuarioData()

        # Municipio
        self.municipio=MunicipioData()

        self.tla= TLAData()
        
        self.button_CerrarS.clicked.connect(self.cerrarSesion)
        
        #####  Pagina Calculo ############
        self.button_Calculo.clicked.connect(self.guiCalculos)
        
       ##### PAGINA USUARIO #############
        self.button_Usuarios.clicked.connect(self.guiUsuarios)

        #### PAGINA TRAZAS #######
        self.button_Trazas.clicked.connect(self.mostrar_datos_tablaTraza)
        self.Button_EliminarTraza.clicked.connect(self.EliminarTraza)
        self.ButtonBuscarTraza.clicked.connect(self.BuscarTraza)

        ### PAGINA AJUSTES ######
        self.K= KData()
        self.G= GData()
        self.button_Ajustes.clicked.connect(self.GUIAjustes)

        ### MI PERFIL ############
        self.button_MiPerfil.clicked.connect(self.miPerfil)
    
    #Inciando la Interfaz de Mensaje
    def Mensaje(self):
        self.mensaje=Mensaje()
    
    def mousePresEvent(self,event):
        self.click_position= event.globalPos()
    
    #def mover_ventana(self,event):
        #if self.isMaximized()==False:
            #if event.buttons()==QtCore.Qt.LeftButton:
                #self.move(self.pos()+ event.globalPos()-self.click_position)
                #self.click_position=event.globalPos()
                #event.accept()
            #if event.globalPos().y()<=10:
                #self.showMaximized()
            #else:
                #self.showNormal()
                
    
    # Mover Menu 
    def mover_menu(self):
        if True:
            width = self.frame_control.width()
            normal=0
            if width==0:
                extender=200
            else:
                extender=normal
            self.animacion= QPropertyAnimation(self.frame_control,b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            #self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
        
       
########################## PAGINA CALCULO #########################
    def guiCalculos(self):
        #LLamado de la Funcion mostrar_datos_tablaCalculos()
        self.mostrar_datos_tablaCalculos()
        # Boton Nuevo en Calculo
        self.button_NuevoCalculo.clicked.connect(self.btnuevocalculo)
        # Boton Eliminar en Calculo
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        # Boton Editar en Calculo
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        # Mostrar Combo de Municipio
        self.comboBoxMunCalculo.clear()
        self.MostrarComboMunCalculo()
        # Boton Seleccionar en Calculo
        self.button_BuscarCalculos_2.clicked.connect(self.Seleccionar)
        #Boton Buscar en Calculo
        self.button_BuscarCalculos.clicked.connect(self.BucarCalculoUbiacionFecha)
        #Limpiar el Combo Ubicacion
        self.comboBoxUbicacion.clear()

    def mostrar_datos_tablaCalculos(self):
        #Obteniendo Los Datos de la Base de Datos
        datos=self.tla.mostrar_datos_tla()
        
        #Obteniendo la lista y Convertiendola a Str 
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Calculos.setRowCount(i)
        tablerow=0

        for row in a:
            #Mostrando Los Datos en la Tabla Calculos
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
        # Selecciona un fila Para Eliminar
        rows=self.table_Calculos.selectionModel().selectedRows()
        
        # Si no selecciona una Fila
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para eliminar")
            self.mensaje.button()
        #En Caso Que Seleccione una Fila
        else: 
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                #Obteniendo el Id de la Fila Seleccionada
                id= self.table_Calculos.item(i,0).text()
                #Eliminando de la Tabla Calculo
                self.table_Calculos.removeRow(i)
                #Eliminando de la Base de Datos
                self.tla.eliminar_datos_tla(id)
            
            #Traza
            eliminado= self.eventos.eliminarCalculo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)
        

    def EditarCalculo(self):
        # Selecciona un fila Para Editar
        rows=self.table_Calculos.selectionModel().selectedRows()
        
        # Si no selecciona una Fila
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para editar")
            self.mensaje.button()
        #En Caso Que Seleccione una Fila
        else:
            #Mostrando la Interfaz de Editar Calculo
            self.editarcalculoGUI()
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.table_Calculos.item(i,0).text()
                self.idx=self.tla.buscar_datos_tla_DI(id)
            
            #Mostrando los Datos en Editar Calculo
            self.editarcalculo.mostrarDatosEditar(self.idx)
            
    def MostrarComboMunCalculo(self):
        #Obteniendo la Lista de Municipios de la Base de Datos
        datos=self.municipio.listaMunicipio()
        #Añadiendo los Municipios al ComboBox
        for item in datos:
            self.comboBoxMunCalculo.addItem(item[1])
    
    def MostrarComboUbicCalculo(self):
        #Obteniendo la Lista de Ubicaciones de la Base de Datos
        datos1= self.ubicaciondata.listaUbicaciones(self.comboBoxMunCalculo.currentText())
        #Añadiendo las Ubicaciones al ComboBox
        for item in datos1:
            self.comboBoxUbicacion.addItem(item[1])

    def Seleccionar(self):
        if self.comboBoxMunCalculo.currentText()=="Seleccione un Municipio":
            self.Mensaje()
            self.mensaje.label("Seleccione un Municipio")
            self.mensaje.button()
        else:
            #Limpando el Combo Ubicacion
            self.comboBoxUbicacion.clear()
            # LLamando a la Funcion MostrarComboUbicCalculo()
            self.MostrarComboUbicCalculo()


    def BucarCalculoUbiacionFecha(self):
        #Obteniendo el Municipio Seleccionado en el ComboBox
        ubicacion= self.comboBoxUbicacion.currentText()
        #Conviertiendo la fecha del dateEdit a formato Python 
        fechaDesde=self.dateDesdeCalculo.date().toPyDate()
        fechaHasta=self.dateHastaCalculo.date().toPyDate()
        #Si no Esta Seleccionado la Ubicacion Buscar por las Fechas
        if ubicacion=="":
            #Llamado de la Funcion buscarPorFechaAdmin de TLA()
            datos= self.tla.buscarPorFechaAdmin(fechaDesde,fechaHasta)
            #Llamado de la funcion Buscar()
            self.Buscar(datos)
        #Sino Buscar por la la Ubicacion y por la Fecha 
        else:
            #Llamado de la Funcion buscarCalculoAdministrador de TLA()
            datos= self.tla.buscarCalculoAdministrador(ubicacion,fechaDesde,fechaHasta)
            #Llamado de la funcion Buscar()
            self.Buscar(datos)
            
    
    def Buscar(self,datos):
       #Obteniendo la lista y Convertiendola a Str  
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Calculos.setRowCount(i)
        tablerow=0

        for row in a:
            #Mostrando Los Datos en la Tabla Calculos
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

    ################# Nuevo  Calculo ##########        
    def btnuevocalculo(self):
        #Llamando a la Interfaz NuevoCalculo
        self.nuevocalculo=NuevoCalculo()
        #Enviar el nombre de Usuario y el id que esta Interactuando 
        self.nuevocalculo.recibirUsuario(self.nombreUsuario,self.idUsuario)
        #Mostrar La Tabla Actualizada al Guardar Calculo 
        guardar=self.nuevocalculo.boton_guardar()
        guardar.clicked.connect(self.mostrar_datos_tablaCalculos)

    ################# Editar Calculo ##########
    def editarcalculoGUI(self):
        #Llamando a la Interfaz EditarCalculo
        self.editarcalculo=EditarCalculo()
        #Mostrar La Tabla Actualizada al Actualizar Calculo 
        actualizar=self.editarcalculo.boton_actualizar()
        actualizar.clicked.connect(self.mostrar_datos_tablaCalculos)
        #Mostrar La Tabla Actualizada al Crear Nuevo Calculo 
        nuevo=self.editarcalculo.boton_nuevo()
        nuevo.clicked.connect(self.mostrar_datos_tablaCalculos)
        #Enviar el nombre de Usuario y el id que esta Interactuando 
        self.editarcalculo.recibirUsuario(self.nombreUsuario,self.idUsuario)
##################### PAGINA USUARIOS ##############################
    def guiUsuarios(self):
        #Iniciando un Objeto de UsuarioData()
        self.usuarioData=UsuarioData()
        #LLamado de la Funcion mostrar_datos_tablaUsuarios()
        self.mostrar_datos_tablaUsuarios()
        #Limpiar el lineEdit de Buscar Usuario
        self.lineEditBuscarUsuario.clear()
        # Boton Eliminar en Usuario
        self.buttonEliminarUsuario.clicked.connect(self.EliminarUsuario)
        # Boton Nuevo en Usuario
        self.buttonNuevoUsuario.clicked.connect(self.nuevoUsuario)
        # Boton Editar en Usuario
        self.buttonEditarUsuario.clicked.connect(self.botonEditarUsuario)
        # Boton Buscar en Usuario
        self.buttonBuscarUsuario.clicked.connect(self.buscarUsuario)

    def nuevoUsuario(self):
        #Llamando a la Interfaz NuevoUsuario
        self.nuevousuario= NuevoUsuario()
        #Enviar el nombre de Usuario y el id que esta Interactuando 
        self.nuevousuario.recibirUsuario(self.nombreUsuario)
        #Mostrar La Tabla Actualizada al Crear Usuario
        crear=self.nuevousuario.buton_GuardarUsuario()
        crear.clicked.connect(self.mostrar_datos_tablaUsuarios)
    
    def mostrar_datos_tablaUsuarios(self):
        #Obteniendo Los Datos de la Base de Datos
        datos=self.usuarioData.mostrarUsuario()
        
        #Obteniendo la lista y Convertiendola a Str 
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.tableUsuarios.setRowCount(i)
        tablerow=0

        for row in a:
            #Mostrando Los Datos en la Tabla Usuarios
            self.tableUsuarios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableUsuarios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[6]))
            self.tableUsuarios.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableUsuarios.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[1]))
            self.tableUsuarios.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.tableUsuarios.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            self.tableUsuarios.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
            self.tableUsuarios.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
            self.tableUsuarios.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
            tablerow += 1 
    
    def EliminarUsuario(self):
        # Selecciona un fila Para Eliminar
        rows=self.tableUsuarios.selectionModel().selectedRows()
        # Si no selecciona una Fila
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para eliminar")
            self.mensaje.button()
        #En Caso Que Seleccione una Fila
        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                #Obteniendo el Id de la Fila Seleccionada
                id= self.tableUsuarios.item(i,0).text()
                #Eliminando de la Tabla Usuario
                self.tableUsuarios.removeRow(i)
                #Eliminando de la Base de Datos
                self.usuarioData.eliminarUsuario(id)
            
            #Traza
            eliminado= self.eventos.eliminoUsuario()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas) 
    
    def EditarUsuario(self):
        #Llamando a la Interfaz EditarUsuario
        self.editarusuario= EditarUsuario()
        #Enviar el nombre de Usuario y el id que esta Interactuando 
        self.editarusuario.recibirUsuario(self.nombreUsuario)
        #Mostrar La Tabla Actualizada al Editar Usuario
        actualizar=self.editarusuario.bt_actualizar()
        actualizar.clicked.connect(self.mostrar_datos_tablaUsuarios)
    
    def botonEditarUsuario(self):
        # Selecciona un fila Para Editar
        rows=self.tableUsuarios.selectionModel().selectedRows()
        # Si no selecciona una Fila
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para Editar")
            self.mensaje.button()
        #En Caso Que Seleccione una Fila
        else:
            self.EditarUsuario()
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                #Obteniendo el Id de la Fila Seleccionada
                id= self.tableUsuarios.item(i,0).text()
                #Buscando en la Base de Datos del ID
                self.idx=self.usuarioData.buscarusuarioID (id)
            #Mostrado en los Datos en la Interfaz EditarUsuario
            self.editarusuario.mostrarDatos(self.idx)
    
    def buscarUsuario(self):
        #Verficar que el Campo CI de Busqueda es Valido
        verificar=self.validar.validarInt(self.lineEditBuscarUsuario.text())
        #Si No es Valido
        if verificar==False:
            self.Mensaje()
            self.mensaje.label("Debe Entrar un CI válido")
            self.mensaje.button()
            #Traza
            datoCI= self.eventos.datoCI()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoCI)
            self.trazadata.insertarTraza(self.trazas) 
        # Si el Campo no es de 11 Digitos
        elif len(self.lineEditBuscarUsuario.text()) != 11:
            self.lineEditBuscarUsuario.setStyleSheet("border: 1px solid red;")
            self.lineEditBuscarUsuario.setFocus()
            self.Mensaje()
            self.mensaje.label("Debe Entrar un CI de 11 dígitos")
            self.mensaje.button()
            #Traza
            datoCI= self.eventos.datoCI()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= datoCI)
            self.trazadata.insertarTraza(self.trazas) 
        # En caso de ser Valido
        else:
            #Buscar el CI en la Base de Datos
            listaCI= self.usuarioData.buscarusuarioCI(self.lineEditBuscarUsuario.text())
            
            #Obteniendo la lista y Convertiendola a Str 
            a=[]
            for x in listaCI:
                a.append([str(i) for i in x])
       
                i=len(a)
                self.tableUsuarios.setRowCount(i)
                tablerow=0

                for row in a:
                    #Mostrando los Datos en la Tabla Usuario
                    self.tableUsuarios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tableUsuarios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[6]))
                    self.tableUsuarios.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableUsuarios.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableUsuarios.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                    self.tableUsuarios.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
                    self.tableUsuarios.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[7]))
                    self.tableUsuarios.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[8]))
                    self.tableUsuarios.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[9]))
                    tablerow += 1 
                
                #Traza
                buscarUsuario= self.eventos.buscarUsuario()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= buscarUsuario)
                self.trazadata.insertarTraza(self.trazas) 

    
##################### TRAZAS ######################################
    def EliminarTraza(self):
        # Selecciona un fila Para Eliminar
        rows=self.table_Trazas.selectionModel().selectedRows()
        # Si no selecciona una Fila
        if len(rows)==0:
            self.Mensaje()
            self.mensaje.label("Debe seleccionar una Fila de la Tabla para eliminar")
            self.mensaje.button()
        #En Caso Que Seleccione una Fila
        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                #Obteniendo el Id de la Fila Seleccionada
                id= self.table_Trazas.item(i,0).text()
                #Eliminando de la Tabla Traza
                self.table_Trazas.removeRow(i)
                #Eliminando de la Base de Datos
                self.trazadata.eliminarTraza(id)
    
    def mostrar_datos_tablaTraza(self):
        #Obteniendo Los Datos de la Base de Datos
        datos=self.trazadata.mostrarTraza()
        #Obteniendo la lista y Convertiendola a Str 
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Trazas.setRowCount(i)
        tablerow=0
    
        for row in a:
            #Mostrando Los Datos en la Tabla Traza
            self.table_Trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow += 1 
    
    def BuscarTraza(self):
        # Buscar por la Fecha las Trazas
        datos= self.trazadata.buscarPorFecha(self.dateEditTrazaDesde.date().toPyDate(),self.dateEditTrazaHasta.date().toPyDate())
        #Obteniendo la lista y Convertiendola a Str 
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Trazas.setRowCount(i)
        tablerow=0
    
        for row in a:
            #Mostrando Los Datos en la Tabla Traza
            self.table_Trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow += 1 
        

    
########################## AJUSTES  #########################
    def GUIAjustes(self):
        #Llamado de la funcion MostrarConstantes()
        self.MostrarConstantes()
        #Boton Cambiar Variables  en Ajustes
        self.ButtonCambiarVar.clicked.connect(self.Cambiar)
        # Llamado de la Funcion LimpiarCamposMunicipio()
        self.LimpiarCamposMunicipio()
        # MOstrando los Municipios en el ComboBOx
        self.MostrarMunicipio()
        # Boton Añadir Municipio en Ajustes
        self.Button_AnadirMun.clicked.connect(self.AnadirMunicipio)
        # Boton Seleccionar Municipio en Ajustes 
        self.Button_SelecMun.clicked.connect(self.seleccionar)
        #Boton Editar Municipio en Ajustes 
        self.Button_EditarMun.clicked.connect(self.editarMunicipio)
        #Boton Eliminar Municipio en Ajustes 
        self.Button_EliminarMun.clicked.connect(self.EliminarMunicipio)
        #Boton Añadir Ubicacion en Ajustes
        self.Button_AnadirUbic.clicked.connect(self.NuevaUbicacion)
        #Boton Seleccionar Municipio een Ajustes 
        self.Button_SelecUbic.clicked.connect(self.SeleccionarMunUbic)
        #Boton Seleccionar Ubicacion en Ajustes 
        self.Button_SelecUbic_2.clicked.connect(self.SeleccionarUbicacion)
        #Boton Editar Ubicacion en Ajustes 
        self.Button_EditarUbic.clicked.connect(self.EditarUbicacion)
        #Boton Eliminar Ubicacion
        self.Button_EliminarUbic.clicked.connect(self.eliminarUbicacion)
    
    def MostrarConstantes(self):
        #Obteniendo las Constante de la Base de Datos
        datos=self.K.mostrarK()
        datos1=self.G.mostrarG()
        
        #Convirtiendo a str
        Kconstante=[]
        for x in datos:
            Kconstante.append([str(i) for i in x])

        gconstante=[]
        for x in datos1:
            gconstante.append([str(i) for i in x])
        
        #Mostrando en las COnstantes en el lineEdit
        self.lineEdit_K.setText(Kconstante[0][1])
        self.lineEdit_G.setText(gconstante[0][1])
        #Guardando los datos anterior en una Variable
        
    
    def Cambiar(self):
        #Convirtiendo a float 
        Kconstante=float(self.lineEdit_K.text())
        gconstante=float(self.lineEdit_G.text())
        #Actualizar los Datos de la Constante de la BD
        a= self.K.actualizarK(Kconstante)
        b= self.G.actualizarG(gconstante)
        
        self.Mensaje()
        self.mensaje.label("Datos Actualizado")
        self.mensaje.button()

        #Traza 
        CambioConstantes= self.eventos.CambioConstantes()
        self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= CambioConstantes)
        self.trazadata.insertarTraza(self.trazas) 


        

    def AnadirMunicipio(self):
        #Validando los Datos 
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())
        
        #Si no es Valido
        if validando== False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si es valido
        else:
            #Añadir el Municipio en la Base de Datos en Mayuscula
            a=self.municipio.insertarMunicipio(self.lineEdit_AddMunicipio.text().upper())
            #Si es True
            if a:
                self.Mensaje()
                self.mensaje.label("Municipio Añadido con Éxito")
                self.mensaje.button()

                #Traza 
                AnadioMunicipio= self.eventos.AnadioMunicipio()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= AnadioMunicipio)
                self.trazadata.insertarTraza(self.trazas) 
            #Si es False
            else :
                self.Mensaje()
                self.mensaje.label(" El Municipio ya Éxiste")
                self.mensaje.button()

                #Traza 
                AnadioMunicipioExiste= self.eventos.AnadioMunicipioExiste()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= AnadioMunicipioExiste)
                self.trazadata.insertarTraza(self.trazas) 
            #Llamando a la Funcion LimpiarCamposMunicipio()
            self.LimpiarCamposMunicipio()
            #Llamando a la Funcion MostrarMunicipio()
            self.MostrarMunicipio()
    
    def MostrarMunicipio(self):
        #Obteniendo los Municipio de la Base de Datos
        datos=self.municipio.listaMunicipio()
        #Añadiendo Los Muncipios al ComboBox
        for item in datos:
            self.comboBoxMunicipio.addItem(item[1])
        #Añadiendo Los Muncipios al ComboBox
        for item in datos:
            self.comboBoxMunUbic.addItem(item[1])
        
    
    def LimpiarCamposMunicipio(self):
        self.comboBoxMunicipio.clear()
        self.lineEdit_AddMunicipio.clear()
        self.comboBoxMunUbic.clear()

    def seleccionar(self):
        if self.comboBoxMunicipio.currentText()=="Seleccione de la lista" :
            self.Mensaje()
            self.mensaje.label("Seleccione de la Lista")
            self.mensaje.button()
        else:
            #Mostrando en el lineEdit el Municipio Seleccionado
            self.lineEdit_AddMunicipio.setText(self.comboBoxMunicipio.currentText())

    def editarMunicipio(self):
        # Validando los Datos 
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())
        #Si no es Valido
        if  validando== False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        else:
            nombreanterior= self.comboBoxMunicipio.currentText()
            nombre=self.lineEdit_AddMunicipio.text().upper()
            a= self.municipio.editarMunicipio(nombre,nombreanterior)
            if a:
                self.Mensaje()
                self.mensaje.label("Municipio Editado con Éxito")
                self.mensaje.button()
            
                #Traza 
                EditoMunicipio= self.eventos.EditoMunicipio()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=EditoMunicipio)
                self.trazadata.insertarTraza(self.trazas) 

                #Llamado a la Funcion LimpiarCamposMunicipio()
                self.LimpiarCamposMunicipio()
                #LLamando a la FUncion MostrarMunicipio()
                self.MostrarMunicipio()
            else:
                self.Mensaje()
                self.mensaje.label("No se Editó")
                self.mensaje.button()

                #Traza 
                NoSeEditoMunicipio= self.eventos.NoSeEditoMunicipio()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=NoSeEditoMunicipio)
                self.trazadata.insertarTraza(self.trazas) 

    def EliminarMunicipio(self):
        if self.lineEdit_AddMunicipio.text()=="":
            self.Mensaje()
            self.mensaje.label("Seleccione para Eliminar")
            self.mensaje.button()
        else:
            #Obteniendo Muncipio del lineEdit
            mun=self.lineEdit_AddMunicipio.text()
            #Elimando Municipio de la Base de Datos
            self.municipio.eliminarMunicipio(mun)
            #Llamado a la Funcion LimpiarCamposMunicipio()
            self.LimpiarCamposMunicipio()
            #LLamando a la FUncion MostrarMunicipio()
            self.MostrarMunicipio()

            self.Mensaje()
            self.mensaje.label("Municipio Eliminado con Éxito")
            self.mensaje.button()

            #Traza 
            EliminoMunicipio= self.eventos.EliminoMunicipio()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=EliminoMunicipio)
            self.trazadata.insertarTraza(self.trazas) 
    
    def SeleccionarMunUbic(self):
        if self.comboBoxMunUbic.currentText()=="Seleccione un Municipio":
            self.Mensaje()
            self.mensaje.label("Seleccione un Municipio")
            self.mensaje.button()
        else:
            #Limpiando ComboBox
            self.comboBoxUbic.clear()
            #Mostrando Ubicaciones en el Municipio Seleccionado
            self.MostrarComboUbic()
    
    def SeleccionarUbicacion(self):
        if self.comboBoxUbic.currentText()== "Seleccione una Ubicación":
            self.Mensaje()
            self.mensaje.label("Seleccione una Ubicación")
            self.mensaje.button()
        else:
            #Mostrando la Ubicacion Seleccionada
            self.lineEdit_AddUbicacion.setText(self.comboBoxUbic.currentText())
            #Obteniendo los Datos de la Ubicacion Seleccionada
            datos= self.ubicaciondata.buscarUbicacion(self.comboBoxUbic.currentText())
            #Mostrando la Latitud de la Ubicacion Seleccionada
            self.lineEdit_Latitud.setText(str(datos[0][3]))
            #Mostrando la Longitud de la Ubicacion Seleccionada
            self.lineEdit_Longitud.setText(str(datos[0][4]))
           
    def LimpiarCamposUbicacion(self):
        self.lineEdit_AddUbicacion.clear()
        self.lineEdit_Latitud.clear()
        self.lineEdit_Longitud.clear()
        self.comboBoxUbic.clear()

    def MostrarComboUbic(self):
        #Obteniendo la Lista de Ubicaciones de un Municipio 
        datos1= self.ubicaciondata.listaUbicaciones(self.comboBoxMunUbic.currentText())
        for item in datos1:
            self.comboBoxUbic.addItem(item[1])        
    
    def NuevaUbicacion(self):
        #Validar Datos
        validando=self.validar.validarCamposNombre(self.lineEdit_AddUbicacion.text())
        validandoLatitud= self.validar.validarCamposNumEnteros(self.lineEdit_Latitud.text())
        validandoLongitud=self.validar.validarCamposNumEnteros(self.lineEdit_Longitud.text())
        #Si no es Valido el Nombre
        if validando==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos")
            self.mensaje.button()
            
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si no es Valida la Latitud
        elif validandoLatitud==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos en la Latitud")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si no es Valida la Longitud 
        elif validandoLongitud==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos en la Longitud")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si son Validos
        else:
            mun=self.comboBoxMunUbic.currentText()
            nombre=self.lineEdit_AddUbicacion.text().upper()
            latitud=self.lineEdit_Latitud.text()
            longitud=self.lineEdit_Longitud.text()
            #Insertando la Ubicacion en la Base de Datos
            a= self.ubicaciondata.insertarUbicacion(nombre,mun,latitud,longitud)
            #Si es la Ubicacion se Añadio
            if a==True:
                self.Mensaje()
                self.mensaje.label("Ubicación Añadida Correctamente")
                self.mensaje.button()
                #Llamando a la Funcion LimpiarCamposUbicacion()
                self.LimpiarCamposUbicacion()
                #Llamando a la Funcion MostrarComboUbic() 
                self.MostrarComboUbic()     
            else:
                self.Mensaje()
                self.mensaje.label("No se guardó")
                self.mensaje.button()
    
    def EditarUbicacion(self):
        # Validando Datos
        validando=self.validar.validarCamposNombre(self.lineEdit_AddUbicacion.text())
        validandoLatitud= self.validar.validarCamposNumEnteros(self.lineEdit_Latitud.text())
        validandoLongitud=self.validar.validarCamposNumEnteros(self.lineEdit_Longitud.text())
        #Si no es Valido el Nombre
        if validando==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si no es Valida la Latitud
        elif validandoLatitud==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos en la Latitud")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas) 
        #Si no es Valida la Longitud 
        elif validandoLongitud==False:
            self.Mensaje()
            self.mensaje.label("Datos Incorrectos en la Longitud")
            self.mensaje.button()
            #Traza 
            datoErroneo= self.eventos.datoErroneo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=datoErroneo)
            self.trazadata.insertarTraza(self.trazas)
        #Si son Validos
        else:
            mun=self.comboBoxMunUbic.currentText()
            nombreant=self.comboBoxUbic.currentText()
            nombre=self.lineEdit_AddUbicacion.text().upper()
            latitud=self.lineEdit_Latitud.text()
            longitud=self.lineEdit_Longitud.text()
            #Actualizando la Ubicacion en la Base de Datos
            a= self.ubicaciondata.editarUbicacion(nombre,mun,latitud,longitud,nombreant)
            #Si es la Ubicacion se Actualizo
            if a==True:
                self.Mensaje()
                self.mensaje.label("Ubicación se Editó Correctamente")
                self.mensaje.button()
                #Traza 
                EditoUbicacion= self.eventos.EditoUbicacion()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=EditoUbicacion)
                self.trazadata.insertarTraza(self.trazas) 
        
                #Llamando a la Funcion LimpiarCamposUbicacion()
                self.LimpiarCamposUbicacion()
                #Llamando a la Funcion MostrarComboUbic() 
                self.MostrarComboUbic()   
            else:
                self.Mensaje()
                self.mensaje.label("No se Editó")
                self.mensaje.button()

                #Traza 
                NoSeEdito= self.eventos.NoSeEdito()
                self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=NoSeEdito)
                self.trazadata.insertarTraza(self.trazas) 
    
    def eliminarUbicacion(self):
        if self.lineEdit_AddUbicacion.text()=="":
            self.Mensaje()
            self.mensaje.label("Seleccione para Eliminar")
            self.mensaje.button()
        else:
            #Obteniendo Muncipio del lineEdit
            ubic=self.lineEdit_AddUbicacion.text()
            #Elimando Ubicacion de la Base de Datos
            self.ubicaciondata.eliminarUbicacion(ubic)
            #Llamado a la Funcion LimpiarCamposMunicipio()
            #Llamando a la Funcion LimpiarCamposUbicacion()
            self.LimpiarCamposUbicacion()
            #Llamando a la Funcion MostrarComboUbic() 
            self.MostrarComboUbic()   

            #Traza 
            EliminoMunicipio= self.eventos.EliminoUbicacion()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento=EliminoMunicipio)
            self.trazadata.insertarTraza(self.trazas) 

################# MI Perfil ########################
    def miPerfil(self):
        self.buttonCambiarContrasena.clicked.connect(self.CambiarContrasena)
    def LimpiarCamposMiPerfil(self):
        self.lineEditContrasenaActual.clear()
        self.lineEditNuevaContrasena.clear()
        self.lineEditConfirmContrsena.clear()

    def CambiarContrasena(self):
        self.usuario=self.usuarioData.buscarusuarioID(self.idUsuario)
        #Si el Entra un Campo Vacio
        if self.lineEditContrasenaActual.text() == "" :
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()
        #Si el Entra un Campo Vacio
        elif self.lineEditNuevaContrasena.text()== "" :
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()
        #Si el Entra un Campo Vacio
        elif self.lineEditConfirmContrsena.text()=="":
            self.Mensaje()
            self.mensaje.label("Debe llenar Los Campos Vacios")
            self.mensaje.button()
        #Si la COntraseña entrada no Coincide con la de la BD
        elif self.lineEditContrasenaActual.text() != self.usuario[0][3]:
            self.Mensaje()
            self.mensaje.label("Contraseña  Actual es Incorrecta")
            self.mensaje.button()
        #Si la Nueva Contraseña no COincide con la Confirmada
        elif self.lineEditNuevaContrasena.text() != self.lineEditConfirmContrsena.text():
            self.Mensaje()
            self.mensaje.label("La Contraseña Nueva No Coincide con la Confirmada")
            self.mensaje.button()
            
        else:
            #Obteniendo los Datos del Usuario
            nombre=self.usuario[0][1]
            usuario=self.usuario[0][2]
            clave=self.lineEditNuevaContrasena.text()
            PApellido=self.usuario[0][4]
            SApellido=self.usuario[0][5]
            CI=self.usuario[0][6]
            correo=self.usuario[0][7]
            tipo=self.usuario[0][8]
            sexo=self.usuario[0][9]
            #Creando un Usuario
            usuario=Usuario(nombre,usuario,clave,PApellido,SApellido,CI,correo,tipo,sexo)
            #Actualizando el Usuario 
            self.usuarioData.actualizarUsuario(usuario,self.idUsuario)
            
            self.Mensaje()
            self.mensaje.label("La Contraseña Actualizada con Éxito")
            self.mensaje.button()
            #Llamado de la Funcion LimpiarCamposMiPerfil()
            self.LimpiarCamposMiPerfil()

            #Traza
            eliminado= self.eventos.CambioContrasena()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)








            
            

   





            
        


    
    
    

    

