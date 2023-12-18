import sys
#Donde estan todas las fotos
from .nimgC import *
from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView 
from PyQt6.QtCore import QPropertyAnimation,QEasingCurve 
from PyQt6 import QtCore,QtWidgets
from PyQt6.uic import loadUi
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox
from data.tla import TLAData
from model.ecuaciones import transporte_logitudinal_arena 
import re
from model.validarcampos import ValidarCampos
from .nuevocalculo import NuevoCalculo
from .editarcalculo import EditarCalculo
from .nuevousuario import NuevoUsuario
from data.usuario import UsuarioData
from .editarusuario import EditarUsuario


class Principal(QMainWindow):
    def __init__(self):
        #Iniciando
        super(Principal,self).__init__()
        loadUi("gui/principal.ui",self)
        #Mostrando La Ventana a Maximizada
        self.showMaximized()
        #Llamando a la Funcion iniGUi()
        self.iniGUI()
        #Llamando a la funcion Mover Menu
        self.but_mover.clicked.connect(self.mover_menu)
        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_inicio))
        self.button_Usuarios.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_usuarios))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_calculo))
        self.button_Trazas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_trazas))
        self.button_Ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))

        #Control de Barra de Titulo
        self.button_MinimizarVentana.clicked.connect(self.control_bt_minimizar)
        self.Button_Minimizar.clicked.connect(self.control_bt_normal)
        self.Button_Maximizar.clicked.connect(self.control_bt_maximizar)
        self.Button_Cerrar.clicked.connect(lambda: self.close())

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

 ######################  Principal ###########################   
    def iniGUI(self):
        self.button_Calculo.clicked.connect(self.mostrar_datos_tablaCalculos)
        #####  Pagina Calculo ############
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        
       
       ##### PAGINA USUARIO #############
        self.buttonNuevoUsuario.clicked.connect(self.nuevoUsuario)
        self.usuarioData=UsuarioData()
        self.mostrar_datos_tablaUsuarios()
        self.buttonEliminarUsuario.clicked.connect(self.EliminarUsuario)
        self.buttonEditarUsuario.clicked.connect(self.botonEditarUsuario)
       
        
    def control_bt_minimizar(self):
        self.showMinimized()
    
    
    def control_bt_normal(self):
        self.showNormal()
        self.Button_Minimizar.hide()
        self.Button_Maximizar.show()
    
    def control_bt_maximizar(self):
        self.showMaximized()
        self.Button_Maximizar.hide()
        self.Button_Minimizar.show()

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
                self.tla= TLAData()
                self.idx=self.tla.buscar_datos_tla_DI(id)
            
            self.editarcalculo.mostrarDatosEditar(self.idx)
            self.mostrar_datos_tablaCalculos()
    
    ################# Nuevo  Calculo ##########        
    def nuevocalculo(self):
        #Llamando a la ventana NuevoCalculo
        self.nuevocalculo=NuevoCalculo()
        guardar=self.nuevocalculo.boton_guardar()
        guardar.clicked.connect(self.mostrar_datos_tablaCalculos)

    ################# Editar Calculo ##########
    def editarcalculoGUI(self):
        self.editarcalculo=EditarCalculo()
        actualizar=self.editarcalculo.boton_actualizar()
        actualizar.clicked.connect(self.mostrar_datos_tablaCalculos)
        nuevo=self.editarcalculo.boton_nuevo()
        nuevo.clicked.connect(self.mostrar_datos_tablaCalculos)
##################### Usuarios ##############################
    def nuevoUsuario(self):
        self.nuevousuario= NuevoUsuario()
    
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
    
    def EditarUsuario(self):
        self.editarusuario= EditarUsuario()
    
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
   





            
        


    
    
    

    

