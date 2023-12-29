import sys
#Donde estan todas las fotos
from .nimgC import *
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView 
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve 
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import loadUi
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
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

from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData
from data.K import KData
from data.G import GData

class Principal(QMainWindow):
    def __init__(self):
        #Iniciando
        super(Principal,self).__init__()
        loadUi("gui/principal.ui",self)

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

        # Mover ventana
        #self.frame_superior.mouseMoveEvent= self.mover_ventana

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Usuario))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))
        self.button_MiPerfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_MiPerfil))

        #Ancho de columna adaptable
        #header=self.tableUsuarios.horizontalHeader()
        #header.setSectionResizeMode(0,QHeaderView.Stretch)
        #self.table_Calculos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.table_Trazas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #Llamando a la Funcion iniGUi()
        self.iniGUI()

        #Mostrando La Ventana a Normal
        self.showNormal()

    def resizeEvent(self,event):
        rect=self.rect()
        self.grip.move(rect.right()-self.gripSize,rect.bottom()-self.gripSize)

    def recibirUsuario(self,usuario,id):
        self.idUsuario=id
        self.nombreUsuario= usuario

    def recibirInicio(self,inicio):
        self.inicio= inicio
    
    def cerrarSesion(self):
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

        # Municipio
        self.municipio=MunicipioData()
        # Ubicacion
        self.ubicaciondata=UbicacionData()
        # Validar Campos
        self.validar= ValidarCampos()

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
        self.K.insertarK()
        self.G.insertarG()
        self.button_Ajustes.clicked.connect(self.GUIAjustes)

        ### MI PERFIL ############
        self.button_MiPerfil.clicked.connect(self.miPerfil)
    
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
        self.tla= TLAData()
        self.mostrar_datos_tablaCalculos()
        self.button_NuevoCalculo.clicked.connect(self.btnuevocalculo)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        self.MostrarComboMunCalculo()
        self.button_BuscarCalculos_2.clicked.connect(self.Seleccionar)
        self.button_BuscarCalculos.clicked.connect(self.BucarCalculoUbiacionFecha)
        self.comboBoxUbicacion.clear()

    def mostrar_datos_tablaCalculos(self):
        self.mostrar= TLAData()
        datos=self.mostrar.mostrar_datos_tla()
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
            mBox= QMessageBox()
            mBox.setText("Debe seleccionar una Fila de la Tabla para eliminar")
            mBox.exec()

        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.table_Calculos.item(i,0).text()
                self.table_Calculos.removeRow(i)
                self.tla.eliminar_datos_tla(id)
            
            eliminado= self.eventos.eliminarCalculo()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)
        

    def EditarCalculo(self):
        rows=self.table_Calculos.selectionModel().selectedRows()
        
        if len(rows)==0:
            mBox= QMessageBox()
            mBox.setText("Debe seleccionar una Fila de la Tabla para editar")
            mBox.exec()
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
            
    def MostrarComboMunCalculo(self):
        datos=self.municipio.listaMunicipio()
        for item in datos:
            self.comboBoxMunCalculo.addItem(item[1])
    
    def MostrarComboUbicCalculo(self):
        datos1= self.ubicaciondata.listaUbicaciones(self.comboBoxMunCalculo.currentText())
        for item in datos1:
            self.comboBoxUbicacion.addItem(item[1])

    def Seleccionar(self):
        if self.comboBoxMunCalculo.currentText()=="Seleccione un Municipio":
            mBox= QMessageBox()
            mBox.setText("Seleccione un Municipio")
            mBox.exec()
        else:
            self.comboBoxUbicacion.clear()
            self.MostrarComboUbicCalculo()


    def BucarCalculoUbiacionFecha(self):
        ubicacion= self.comboBoxUbicacion.currentText()
        fechaDesde=self.dateDesdeCalculo.date().toPyDate()
        fechaHasta=self.dateHastaCalculo.date().toPyDate()
        if ubicacion=="":
            datos= self.tla.buscarPorFechaAdmin(fechaDesde,fechaHasta)
            self.Buscar(datos)
        else:
            datos= self.tla.buscarCalculoAdministrador(ubicacion,fechaDesde,fechaHasta)
            self.Buscar(datos)
            
    
    def Buscar(self,datos):
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

    ################# Nuevo  Calculo ##########        
    def btnuevocalculo(self):
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
        self.editarcalculo.recibirUsuario(self.nombreUsuario)
##################### PAGINA USUARIOS ##############################
    def guiUsuarios(self):
        self.usuarioData=UsuarioData()
        self.mostrar_datos_tablaUsuarios()
        self.lineEditBuscarUsuario.clear()
        self.buttonEliminarUsuario.clicked.connect(self.EliminarUsuario)
        self.buttonNuevoUsuario.clicked.connect(self.nuevoUsuario)
        self.buttonEditarUsuario.clicked.connect(self.botonEditarUsuario)
        self.buttonBuscarUsuario.clicked.connect(self.buscarUsuario)

    def nuevoUsuario(self):
        self.nuevousuario= NuevoUsuario()
        self.nuevousuario.recibirUsuario(self.nombreUsuario)
        crear=self.nuevousuario.buton_GuardarUsuario()
        crear.clicked.connect(self.mostrar_datos_tablaUsuarios)
    
    def mostrar_datos_tablaUsuarios(self):
        datos=self.usuarioData.mostrarUsuario()
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.tableUsuarios.setRowCount(i)
        tablerow=0

        for row in a:
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
        rows=self.tableUsuarios.selectionModel().selectedRows()
        
        if len(rows)==0:
            mBox= QMessageBox()
            mBox.setText("Debe seleccionar una Fila de la Tabla para eliminar")
            mBox.exec()

        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.tableUsuarios.item(i,0).text()
                self.tableUsuarios.removeRow(i)
                self.usuarioData.eliminarUsuario(id)
            
            eliminado= self.eventos.eliminoUsuario()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas) 
    
    def EditarUsuario(self):
        self.editarusuario= EditarUsuario()
        self.editarusuario.recibirUsuario(self.nombreUsuario)
        actualizar=self.editarusuario.bt_actualizar()
        actualizar.clicked.connect(self.mostrar_datos_tablaUsuarios)
    
    def botonEditarUsuario(self):
        rows=self.tableUsuarios.selectionModel().selectedRows()
        
        if len(rows)==0:
            mBox= QMessageBox()
            mBox.setText("Debe seleccionar una Fila de la Tabla para editar")
            mBox.exec()
        else:
            self.EditarUsuario()
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.tableUsuarios.item(i,0).text()
                self.idx=self.usuarioData.buscarusuarioID (id)
            
            self.editarusuario.mostrarDatos(self.idx)
    
    def buscarUsuario(self):
        verificar=self.validar.validarInt(self.lineEditBuscarUsuario.text())
        if verificar==False:
            mBox= QMessageBox()
            mBox.setText("Debe entrar un CI válido")
            mBox.exec()
        elif len(self.lineEditBuscarUsuario.text()) != 11:
            self.lineEditBuscarUsuario.setStyleSheet("border: 1px solid red;")
            self.lineEditBuscarUsuario.setFocus()
            mBox= QMessageBox()
            mBox.setText("Debe entrar un CI 11 dígitos")
            mBox.exec()
        else:
            listaCI= self.usuarioData.buscarusuarioCI(self.lineEditBuscarUsuario.text())
            a=[]
            for x in listaCI:
                a.append([str(i) for i in x])
       
                i=len(a)
                self.tableUsuarios.setRowCount(i)
                tablerow=0

                for row in a:
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

    
##################### TRAZAS ######################################
    def EliminarTraza(self):
        rows=self.table_Trazas.selectionModel().selectedRows()
        
        if len(rows)==0:
            mBox= QMessageBox()
            mBox.setText("Debe seleccionar una Fila de la Tabla para eliminar")
            mBox.exec()

        else:
            index=[]
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                id= self.table_Trazas.item(i,0).text()
                self.table_Trazas.removeRow(i)
                self.trazadata.eliminarTraza(id)
    
    def mostrar_datos_tablaTraza(self):
        datos=self.trazadata.mostrarTraza()
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Trazas.setRowCount(i)
        tablerow=0
    
        for row in a:
            self.table_Trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow += 1 
    
    def BuscarTraza(self):
        datos= self.trazadata.buscarPorFecha(self.dateEditTrazaDesde.date().toPyDate(),self.dateEditTrazaHasta.date().toPyDate())
    
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
       
        i=len(a)
        self.table_Trazas.setRowCount(i)
        tablerow=0
    
        for row in a:
            self.table_Trazas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.table_Trazas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.table_Trazas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.table_Trazas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            
            tablerow += 1 
        

    
########################## AJUSTES  #########################
    def GUIAjustes(self):
        self.MostrarConstantes()
        self.ButtonCambiarVar.clicked.connect(self.Cambiar)
        self.Button_AnadirMun.clicked.connect(self.AnadirMunicipio)
        self.LimpiarCamposMunicipio()
        self.MostrarMunicipio()
        self.Button_SelecMun.clicked.connect(self.seleccionar)
        self.Button_EditarMun.clicked.connect(self.editarMunicipio)
        self.Button_EliminarMun.clicked.connect(self.EliminarMunicipio)
        self.Button_AnadirUbic.clicked.connect(self.NuevaUbicacion)
        self.Button_SelecUbic.clicked.connect(self.SeleccionarMunUbic)
        self.Button_SelecUbic_2.clicked.connect(self.SeleccionarUbicacion)
        self.Button_EditarUbic.clicked.connect(self.EditarUbicacion)
    
    def MostrarConstantes(self):
        datos=self.K.mostrarK()
        datos1=self.G.mostrarG()

        Kconstante=[]
        for x in datos:
            Kconstante.append([str(i) for i in x])

        gconstante=[]
        for x in datos1:
            gconstante.append([str(i) for i in x])
        
        self.lineEdit_K.setText(Kconstante[0][0])
        self.lineEdit_G.setText(gconstante[0][0])
        
        self.Kanterior=float(Kconstante[0][0])
        self.Ganterior=float(gconstante[0][0])
    
    def Cambiar(self):
        Kconstante=float(self.lineEdit_K.text())
        gconstante=float(self.lineEdit_G.text())

        self.K.actualizarK(Kconstante,self.Kanterior)
        self.G.actualizarG(gconstante,self.Ganterior)


    def AnadirMunicipio(self):
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())
        
        if validando== False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()

        else:
            a=self.municipio.insertarMunicipio(self.lineEdit_AddMunicipio.text().upper())
            if a:
                mBox= QMessageBox()
                mBox.setText("Municipio Añadido con Éxito")
                mBox.exec()
            else :
                mBox= QMessageBox()
                mBox.setText("El Municipio ya Existe")
                mBox.exec()

            self.LimpiarCamposMunicipio()
            self.MostrarMunicipio()
    
    def MostrarMunicipio(self):
        datos=self.municipio.listaMunicipio()
        for item in datos:
            self.comboBoxMunicipio.addItem(item[1])
        
        for item in datos:
            self.comboBoxMunUbic.addItem(item[1])
        
    
    def LimpiarCamposMunicipio(self):
        self.comboBoxMunicipio.clear()
        self.lineEdit_AddMunicipio.clear()
        self.comboBoxMunUbic.clear()

    def seleccionar(self):
        if self.comboBoxMunicipio.currentText()=="Seleccione de la lista" :
            mBox= QMessageBox()
            mBox.setText("Seleccione de la lista")
            mBox.exec()
        else:
            self.lineEdit_AddMunicipio.setText(self.comboBoxMunicipio.currentText())

    def editarMunicipio(self):
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())

        if  validando== False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()
        else:
            nombreanterior= self.comboBoxMunicipio.currentText()
            nombre=self.lineEdit_AddMunicipio.text().upper()
            a= self.municipio.editarMunicipio(nombre,nombreanterior)
            if a:
                mBox= QMessageBox()
                mBox.setText("Municipio Editado con Éxito")
                mBox.exec()
                self.LimpiarCamposMunicipio()
                self.MostrarMunicipio()
            else:
                mBox= QMessageBox()
                mBox.setText("No se Editó")
                mBox.exec()
    
    def EliminarMunicipio(self):
        if self.lineEdit_AddMunicipio.text()=="":
            mBox= QMessageBox()
            mBox.setText("Seleccione para Eliminar")
            mBox.exec()
        else:
            mun=self.lineEdit_AddMunicipio.text()
            self.municipio.eliminarMunicipio(mun)
            self.LimpiarCamposMunicipio()
            self.MostrarMunicipio()
    
    def SeleccionarMunUbic(self):
        if self.comboBoxMunUbic.currentText()=="Seleccione un Municipio":
            mBox= QMessageBox()
            mBox.setText("Seleccione un Municipio")
            mBox.exec()
        else:
            self.comboBoxUbic.clear()
            self.MostrarComboUbic()
    
    def SeleccionarUbicacion(self):
        if self.comboBoxUbic.currentText()== "Seleccione una Ubicación":
            mBox= QMessageBox()
            mBox.setText("Seleccione una Ubicación")
            mBox.exec()
        else:
            self.lineEdit_AddUbicacion.setText(self.comboBoxUbic.currentText())
            datos= self.ubicaciondata.buscarUbicacion(self.comboBoxUbic.currentText())
            self.lineEdit_Latitud.setText(str(datos[0][3]))
            self.lineEdit_Longitud.setText(str(datos[0][4]))
           
    def LimpiarCamposUbicacion(self):
        self.lineEdit_AddUbicacion.clear()
        self.lineEdit_Latitud.clear()
        self.lineEdit_Longitud.clear()
        self.comboBoxUbic.clear()

    def MostrarComboUbic(self):
        datos1= self.ubicaciondata.listaUbicaciones(self.comboBoxMunUbic.currentText())
        for item in datos1:
            self.comboBoxUbic.addItem(item[1])        
    
    def NuevaUbicacion(self):
        validando=self.validar.validarCamposNombre(self.lineEdit_AddUbicacion.text())
        validandoLatitud= self.validar.validarCamposNumEnteros(self.lineEdit_Latitud.text())
        validandoLongitud=self.validar.validarCamposNumEnteros(self.lineEdit_Longitud.text())
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()
        
        elif validandoLatitud==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos en la Latitud")
            mBox.exec()
        
        elif validandoLongitud==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos en la Longitud")
            mBox.exec()
        
        else:
            mun=self.comboBoxMunUbic.currentText()
            nombre=self.lineEdit_AddUbicacion.text().upper()
            latitud=self.lineEdit_Latitud.text()
            longitud=self.lineEdit_Longitud.text()
            a= self.ubicaciondata.insertarUbicacion(nombre,mun,latitud,longitud)
            if a==True:
                mBox= QMessageBox()
                mBox.setText("Ubicación Añadida Correctamente")
                mBox.exec()
                self.LimpiarCamposUbicacion()
                self.MostrarComboUbic()     
            else:
                mBox= QMessageBox()
                mBox.setText("No se guardó")
                mBox.exec()
    
    def EditarUbicacion(self):
        validando=self.validar.validarCamposNombre(self.lineEdit_AddUbicacion.text())
        validandoLatitud= self.validar.validarCamposNumEnteros(self.lineEdit_Latitud.text())
        validandoLongitud=self.validar.validarCamposNumEnteros(self.lineEdit_Longitud.text())

        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()
        
        elif validandoLatitud==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos en la Latitud")
            mBox.exec()
        
        elif validandoLongitud==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos en la Longitud")
            mBox.exec()
        
        else:
            mun=self.comboBoxMunUbic.currentText()
            nombreant=self.comboBoxUbic.currentText()
            nombre=self.lineEdit_AddUbicacion.text().upper()
            latitud=self.lineEdit_Latitud.text()
            longitud=self.lineEdit_Longitud.text()
            a= self.ubicaciondata.editarUbicacion(nombre,mun,latitud,longitud,nombreant)
            if a==True:
                mBox= QMessageBox()
                mBox.setText("Ubicación Editó Correctamente")
                mBox.exec()
                self.LimpiarCamposUbicacion()
                self.MostrarComboUbic()     
            else:
                mBox= QMessageBox()
                mBox.setText("No se Editó")
                mBox.exec()

    
################# MI Perfil ########################
    def miPerfil(self):
        self.buttonCambiarContrasena.clicked.connect(self.CambiarContrasena)
    def LimpiarCamposMiPerfil(self):
        self.lineEditContrasenaActual.clear()
        self.lineEditNuevaContrasena.clear()
        self.lineEditConfirmContrsena.clear()

    def CambiarContrasena(self):
        self.usuario=self.usuarioData.buscarusuarioID(self.idUsuario)
        
        if self.lineEditContrasenaActual.text() == "" :
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()
        elif self.lineEditNuevaContrasena.text()== "" :
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()

        elif self.lineEditConfirmContrsena.text()=="":
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()

        elif self.lineEditContrasenaActual.text() != self.usuario[0][3]:
            mBox= QMessageBox()
            mBox.setText("Contraseña  Actual es Incorrecta")
            mBox.exec()
        elif self.lineEditNuevaContrasena.text() != self.lineEditConfirmContrsena.text():
            mBox= QMessageBox()
            mBox.setText("La Contraseña Nueva No Coincide con la Confirmada")
            mBox.exec()
        else:
            nombre=self.usuario[0][1]
            usuario=self.usuario[0][2]
            clave=self.lineEditNuevaContrasena.text()
            PApellido=self.usuario[0][4]
            SApellido=self.usuario[0][5]
            CI=self.usuario[0][6]
            correo=self.usuario[0][7]
            tipo=self.usuario[0][8]
            sexo=self.usuario[0][9]
            usuario=Usuario(nombre,usuario,clave,PApellido,SApellido,CI,correo,tipo,sexo)
            self.usuarioData.actualizarUsuario(usuario,self.idUsuario)

            mBox= QMessageBox()
            mBox.setText("La Contraseña Actualizada con Éxito")
            mBox.exec()

            self.LimpiarCamposMiPerfil()

            eliminado= self.eventos.CambioContrasena()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)








            
            

   





            
        


    
    
    

    

