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
from .nuevousuario import NuevoUsuario
from data.usuario import UsuarioData
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
        #Conectando el Boton Nuevo Calculo con la ventana Nuevo Calculo
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.nuevocalculo= uic.loadUi("gui/nuevoCalculo.ui")
        self.button_Calculo.clicked.connect(self.mostrar_datos_tablaCalculos)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        self.editarcalculo= uic.loadUi("gui/EditarCalculo.ui")
        self.buttonNuevoUsuario.clicked.connect(self.nuevoUsuario)
        self.usuarioData=UsuarioData()
        self.mostrar_datos_tablaUsuarios()
       
        
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
    
    
    def mostrar_datos_tablaCalculos(self):
        self.mostrar= TLAData()
        datos=self.mostrar.mostrar_datos_tla()
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        print(a)
        
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
    
    def nuevocalculo(self):
        #Llamando a la ventana NuevoCalculo
        self.nuevocalculo.label_Error.setText("")
        self.nuevocalculo.but_GuardarNuevoCalculo.clicked.connect(self.EntrarNuevoCalculo)
        self.nuevocalculo.butCancelarNuevoCalculo.clicked.connect(self.boton_Cancelar_NuevoCalculo)
        self.nuevocalculo.show()
    
    def editarcalculoGUI(self):
        self.editarcalculo.label_Error.setText("")
        self.editarcalculo.butCancelarEditar.clicked.connect(self.boton_Cancelar_EditarCalculo)
        self.editarcalculo.but_ActualizarEditar.clicked.connect(self.entrarEditarCalculo)
        self.editarcalculo.but_NuevoEditar.clicked.connect(self.entrarNuevoEditarCalculo)
        self.editarcalculo.show()
    
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
            
            self.mostrarDatosEditar()
            

########################## Nuevo Calculo #########################
    def validandocamposNuevoCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()
        
      
        DensidadArena=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.nuevocalculo.lineEdit_IndiceRompiente.text())
        ubicacion=self.validarcampo.validarCamposNombre(self.nuevocalculo.lineEdit_Ubicacion.text())

        if DensidadArena==False:
            self.nuevocalculo.lineEdit_densidadArena.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_densidadArena.setFocus()
            self.nuevocalculo.lineEdit_densidadArena.setText("0")
            self.nuevocalculo.label_Error.setText("En la Densidad de Arena sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        
        elif DensidadMar ==False:
            self.nuevocalculo.lineEdit_DensidadMar.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_DensidadMar.setFocus()
            self.nuevocalculo.lineEdit_DensidadMar.setText("0")
            self.nuevocalculo.label_Error.setText("En la Densidad del Mar sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        
        elif CoeficienteP ==False:
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setFocus()
            self.nuevocalculo.lineEdit_CoeficientePorocidad.setText("0")
            self.nuevocalculo.label_Error.setText("En el Coeficiente sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif altura ==False:
            self.nuevocalculo.lineEdit_altura.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_altura.setFocus()
            self.nuevocalculo.lineEdit_altura.setText("0")
            self.nuevocalculo.label_Error.setText("En la Altura sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif angulo ==False:
            self.nuevocalculo.lineEdit_AnguloRompiente.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_AnguloRompiente.setFocus()
            self.nuevocalculo.lineEdit_AnguloRompiente.setText("0")
            self.nuevocalculo.label_Error.setText("En el Ángulo sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif  indice ==False:
            self.nuevocalculo.lineEdit_IndiceRompiente.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_IndiceRompiente.setFocus()
            self.nuevocalculo.lineEdit_IndiceRompiente.setText("0")
            self.nuevocalculo.label_Error.setText("En el Índice sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")

        elif  ubicacion ==False:
            self.nuevocalculo.lineEdit_Ubicacion.setStyleSheet("border: 1px solid red;")
            self.nuevocalculo.lineEdit_Ubicacion.setFocus()
            self.nuevocalculo.lineEdit_Ubicacion.setText("")
            self.nuevocalculo.label_Error.setText("En la Ubicación sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        else:
           validando= True 
        return validando

    def EntrarNuevoCalculo(self):
        validando= self.validandocamposNuevoCalculo()
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()

        else:
            DensidadArena= float(self.nuevocalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.nuevocalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.nuevocalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.nuevocalculo.lineEdit_altura.text())
            angulo=float(self.nuevocalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.nuevocalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.nuevocalculo.lineEdit_Ubicacion.text()
           

            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                mBox= QMessageBox()
                if self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado):
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado))  
                    self.mostrar_datos_tablaCalculos()
                    self.nuevocalculo.hide()
                    self.limpiarCamposNuevoCalculo()
                    
                else:
                    mBox.setText("Los Datos NO se Guardaron")
                mBox.exec()
    

    def limpiarCamposNuevoCalculo(self):
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_densidadArena.setText("")
        self.nuevocalculo.lineEdit_DensidadMar.setText("")
        self.nuevocalculo.lineEdit_CoeficientePorocidad.setText("")
        self.nuevocalculo.lineEdit_altura.setText("")
        self.nuevocalculo.lineEdit_AnguloRompiente.setText("")
        self.nuevocalculo.lineEdit_IndiceRompiente.setText("")
        self.nuevocalculo.lineEdit_Ubicacion.setText("")
    
    def boton_Cancelar_NuevoCalculo(self):
        self.nuevocalculo.hide()
        self.limpiarCamposNuevoCalculo()
    
    ################ Editar Calculo ###########
    def mostrarDatosEditar(self):
        datos= self.idx
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        self.idEditar= a[0][0]
        self.editarcalculo.lineEdit_Ubicacion.setText(a[0][1])
        self.editarcalculo.lineEdit_densidadArena.setText(a[0][3])
        self.editarcalculo.lineEdit_DensidadMar.setText(a[0][2])
        self.editarcalculo.lineEdit_CoeficientePorocidad.setText(a[0][4])
        self.editarcalculo.lineEdit_altura.setText(a[0][5])
        self.editarcalculo.lineEdit_AnguloRompiente.setText(a[0][6])
        self.editarcalculo.lineEdit_IndiceRompiente.setText(a[0][7])
    
    def limpiarCamposEditarCalculo(self):
        self.editarcalculo.lineEdit_DensidadMar.setText("")
        self.editarcalculo.lineEdit_densidadArena.setText("")
        self.editarcalculo.lineEdit_DensidadMar.setText("")
        self.editarcalculo.lineEdit_CoeficientePorocidad.setText("")
        self.editarcalculo.lineEdit_altura.setText("")
        self.editarcalculo.lineEdit_AnguloRompiente.setText("")
        self.editarcalculo.lineEdit_IndiceRompiente.setText("")
        self.editarcalculo.lineEdit_Ubicacion.setText("")
    
    def boton_Cancelar_EditarCalculo(self):
        self.editarcalculo.hide()
        self.limpiarCamposEditarCalculo()
   
    def validandocamposEditarCalculo(self):
        validando= False
        self.validarcampo=ValidarCampos()

        DensidadArena=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_densidadArena.text())
        DensidadMar=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_DensidadMar.text())
        CoeficienteP=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
        altura=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_altura.text())
        angulo=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_AnguloRompiente.text())
        indice=self.validarcampo.validarCamposfloat(self.editarcalculo.lineEdit_IndiceRompiente.text())
        ubicacion=self.validarcampo.validarCamposNombre(self.editarcalculo.lineEdit_Ubicacion.text())
        
        if DensidadArena==False:
            self.editarcalculo.lineEdit_densidadArena.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_densidadArena.setFocus()
            self.editarcalculo.lineEdit_densidadArena.setText("0")
            self.editarcalculo.label_Error.setText("En la Densidad de Arena sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif DensidadMar ==False:
            self.editarcalculo.lineEdit_DensidadMar.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_DensidadMar.setFocus()
            self.editarcalculo.lineEdit_DensidadMar.setText("0")
            self.editarcalculo.label_Error.setText("En la Densidad del Mar sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif CoeficienteP ==False:
            self.editarcalculo.lineEdit_CoeficientePorocidad.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_CoeficientePorocidad.setFocus()
            self.editarcalculo.lineEdit_CoeficientePorocidad.setText("0")
            self.editarcalculo.label_Error.setText("En el Coeficiente sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif altura ==False:
            self.editarcalculo.lineEdit_altura.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_altura.setFocus()
            self.editarcalculo.lineEdit_altura.setText("0")
            self.editarcalculo.label_Error.setText("En la Altura sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif angulo ==False:
            self.editarcalculo.lineEdit_AnguloRompiente.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_AnguloRompiente.setFocus()
            self.editarcalculo.lineEdit_AnguloRompiente.setText("0")
            self.editarcalculo.label_Error.setText("En el Ángulo sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif indice ==False:
            self.editarcalculo.lineEdit_IndiceRompiente.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_IndiceRompiente.setFocus()
            self.editarcalculo.lineEdit_IndiceRompiente.setText("0")
            self.editarcalculo.label_Error.setText("En el Índice sólo puede entrar números, valores mayores que 0 y no puede entrar campos vacios")
        elif ubicacion ==False:
            self.editarcalculo.lineEdit_Ubicacion.setStyleSheet("border: 1px solid red;")
            self.editarcalculo.lineEdit_Ubicacion.setFocus()
            self.editarcalculo.lineEdit_Ubicacion.setText("")
            self.editarcalculo.label_Error.setText("En la Ubicación sólo puede entrar letras, texto mayor a 2 Caracteres y no puede entrar campos vacios")
        else:
            validando=True
        return validando

    def entrarEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()
        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.editarcalculo.lineEdit_Ubicacion.text()
            
           
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                actualizar=self.tla.actualizar_datos_tla(self.idEditar,ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado)

                if actualizar==1:
                    mBox= QMessageBox()
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado))  
                    self.mostrar_datos_tablaCalculos()
                    self.editarcalculo.close()
                    mBox.exec()
                else:
                    mBox= QMessageBox()
                    mBox.setText("Los Datos NO se Guardaron")
                    mBox.exec()
    
    def entrarNuevoEditarCalculo(self):
        validando= self.validandocamposEditarCalculo()
        
        if validando==False:
            mBox= QMessageBox()
            mBox.setText("Datos Incorrectos Verfíquelos ")
            mBox.exec()
        else:
            DensidadArena= float(self.editarcalculo.lineEdit_densidadArena.text())
            DensidadMar=  float(self.editarcalculo.lineEdit_DensidadMar.text())
            CoeficienteP=float(self.editarcalculo.lineEdit_CoeficientePorocidad.text())
            altura=float(self.editarcalculo.lineEdit_altura.text())
            angulo=float(self.editarcalculo.lineEdit_AnguloRompiente.text())
            indice=float(self.editarcalculo.lineEdit_IndiceRompiente.text())
            ubicacion=self.editarcalculo.lineEdit_Ubicacion.text()
            
           
            resultado= transporte_logitudinal_arena(DensidadMar,indice,DensidadArena,CoeficienteP,altura,angulo)
            
            if resultado== False:
                mBox= QMessageBox()
                mBox.setText(" Verfíque los Datos la Division por 0 no esta Permitida ")
                mBox.exec()
            else:
                self.tla= TLAData()
                actualizar=self.tla.insertar_datos_tla(ubicacion,DensidadMar,DensidadArena,CoeficienteP,altura,angulo,indice,resultado)

                if actualizar==1:
                    mBox= QMessageBox()
                    mBox.setText("Datos Guardados con Éxito Q="+ str(resultado))  
                    self.mostrar_datos_tablaCalculos()
                    self.editarcalculo.close()
                    mBox.exec()
                else:
                    mBox= QMessageBox()
                    mBox.setText("Los Datos NO se Guardaron")
                    mBox.exec()
    
##################### Usuarios ##############################
    def nuevoUsuario(self):
        self.nuevousuario= NuevoUsuario()
    
    def mostrar_datos_tablaUsuarios(self):
        datos=self.usuarioData.mostrarUsuario()
        a=[]
        for x in datos:
            a.append([str(i) for i in x])
        print(a)
        
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
    
   





            
        


    
    
    

    

