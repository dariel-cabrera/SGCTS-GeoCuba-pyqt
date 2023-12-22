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
from data.usuario import UsuarioData
from .editarusuario import EditarUsuario
from data.municipio import MunicipioData
from model.validarcampos import ValidarCampos

from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData


class Principal(QMainWindow):
    def __init__(self):
        #Iniciando
        super(Principal,self).__init__()
        loadUi("gui/principal.ui",self)

        #Mostrando La Ventana a Maximizada
        self.show()
        #Llamando a la Funcion iniGUi()
        self.iniGUI()
        
        miFecha= QDate(2023,1,1)
        self.dateEditTrazaDesde.setDate(miFecha)
        self.dateEditTrazaHasta.setDate(miFecha)

        #Llamando a la funcion Mover Menu
        self.but_mover.clicked.connect(self.mover_menu)

        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()

        self.municipio=MunicipioData()
        self.validar= ValidarCampos()

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Usuario))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))


        #Eliminar barra de titulos
        #self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        #self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize=10
        self.grip=QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize,self.gripSize)

        #Ancho de columna adaptable
        #self.tableUsuarios.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.table_Calculos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #Mover ventana
        #self.frame_superior.mouseMoveEvent= self.mover_ventana

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
        self.button_Calculo.clicked.connect(self.mostrar_datos_tablaCalculos)
        #####  Pagina Calculo ############
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        self.button_CerrarS.clicked.connect(self.cerrarSesion)
        
       
       ##### PAGINA USUARIO #############
        self.buttonNuevoUsuario.clicked.connect(self.nuevoUsuario)
        self.usuarioData=UsuarioData()
        self.mostrar_datos_tablaUsuarios()
        self.buttonEliminarUsuario.clicked.connect(self.EliminarUsuario)
        self.buttonEditarUsuario.clicked.connect(self.botonEditarUsuario)

        #### PAGINA TRAZAS #######
        self.button_Trazas.clicked.connect(self.mostrar_datos_tablaTraza)
        self.Button_EliminarTraza.clicked.connect(self.EliminarTraza)
        self.ButtonBuscarTraza.clicked.connect(self.BuscarTraza)

        ### PAGINA AJUSTES ######
        self.button_Ajustes.clicked.connect(self.GUIAjustes)

    #def mover_ventana(self,event):
        #if self.isMaximized()==False:
            #if event.buttons()==QtCore.Qt.LeftButton:
                #self.move(self.pos()+ event.globalPos()-self.click_position)
                #self.click_position=event.globalPos()
                #event.accept()
            #if event.globalPos().y()<=10:
                #self.showMaximized()
                #self.Button_Maximizar.hide()
                #self.Button_Minimizar.show()
            #else:
                #self.showNormal()
                #self.Button_Minimizar.hide()
                #self.Button_Maximizar.show()
    
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
            self.table_Calculos.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[8]))
            self.table_Calculos.setItem(tablerow,9,QtWidgets.QTableWidgetItem(row[9]))
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
                self.tla= TLAData()
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
            
    
    ################# Nuevo  Calculo ##########        
    def nuevocalculo(self):
        #Llamando a la ventana NuevoCalculo
        self.nuevocalculo=NuevoCalculo()
        self.nuevocalculo.recibirUsuario(self.nombreUsuario)
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
    
    ############# TRAZAS ##################
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
        

    
    ################ AJUSTES  #########
    def GUIAjustes(self):
        self.Button_AnadirMun.clicked.connect(self.AnadirMunicipio)
        self.MostrarMunicipio()
        self.Button_EditarMun.clicked.connect(self.editarMunicipio)

    def AnadirMunicipio(self):
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())
        
        if validando== False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()

        else:
            self.municipio.insertarMunicipio(self.lineEdit_AddMunicipio.text())
            mBox= QMessageBox()
            mBox.setText("Municipio Añadido con Éxito")
            mBox.exec()
    
    def MostrarMunicipio(self):
        datos=self.municipio.listaMunicipio()
        for item in datos:
            self.comboBoxMunicipio.addItem(item[1])
            item + 1 
    
    def editarMunicipio(self):
        validando= self.validar.validarCamposNombre(self.lineEdit_AddMunicipio.text())
        self.lineEdit_AddMunicipio.setText(self.comboBoxMunicipio.currentText())

        if self.comboBoxMunicipio.currentText()=="Seleccione de la lista" :
            mBox= QMessageBox()
            mBox.setText("Seleccione de la lista")
            mBox.exec()
        elif validando== False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos")
            mBox.exec()
        else:
            nombreanterior= self.comboBoxMunicipio.currentText()
            nombre=self.lineEdit_AddMunicipio.text()
            a= self.municipio.editarMunicipio(nombre,nombreanterior)
            if a:
                mBox= QMessageBox()
                mBox.setText("Municipio Editado con Éxito")
                mBox.exec()
            else:
                mBox= QMessageBox()
                mBox.setText("No se Editó")
                mBox.exec()





            
            

   





            
        


    
    
    

    

