from PyQt6.QtWidgets import QApplication,QMainWindow,QHeaderView
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

from model.traza import Traza
from model.eventos import Evento 
from data.Trazas import TrazaData

class PrincipalUsuario(QMainWindow):
    def __init__(self):
        #Iniciando
        super(PrincipalUsuario,self).__init__()
        loadUi("gui/PrincipalUsuario.ui",self)
        self.iniGUI()

        self.show()
        self.mostrar= TLAData()
        #Trazas
        self.eventos=Evento()
        self.trazadata= TrazaData()

        self.usuarioData=UsuarioData()

        #Conexion de Botones 
        self.button_Inicio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageInicio))
        self.button_Calculo.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageCalculo))
        self.button_Perfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageMiPerfil))

    
    def iniGUI(self):
        
        self.button_Calculo.clicked.connect(self.mostrar_datos_tablaCalculos)

        #####  Pagina Calculo ############
        self.button_NuevoCalculo.clicked.connect(self.nuevocalculo)
        self.button_EliminarCalculo.clicked.connect(self.EliminarCalculo)
        self.button_EditarCalculo.clicked.connect(self.EditarCalculo)
        self.button_CerrarS.clicked.connect(self.cerrarSesion)
        self.button_Perfil.clicked.connect(self.MiPerfil)
        self.buttonCambiarContrasena.clicked.connect(self.CambiarContrasena)
        miFecha= QDate(2023,12,1)
        self.dateEdit.setDate(miFecha) 
        self.Button_Buscar.clicked.connect(self.buscarCalculo)
    
   
    
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
        self.mostrar= TLAData()
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
    
    ######## BUSCAR CALCULO ##################
    def buscarCalculo(self):
        self.mostrar= TLAData()
        fechadesde= self.dateEdit.date().toPyDate()
        fechahasta=self.dateEditHasta.date().toPyDate()
        print(fechadesde)
        datos=self.mostrar.buscarPorFechaUsuario(fechadesde,fechahasta, self.idUsuario)
        print(datos)
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
    
    def CambiarContrasena(self):
        if self.lineEditContActual.text() == "" :
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()
        elif self.lineEditContNueva.text()== "" :
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()

        elif self.lineEditConfContr.text()=="":
            mBox= QMessageBox()
            mBox.setText("Debe llenar Los Campos Vacios")
            mBox.exec()

        elif self.lineEditContActual.text() != self.usuario[0][3]:
            mBox= QMessageBox()
            mBox.setText("Contraseña  Actual es Incorrecta")
            mBox.exec()
        elif self.lineEditContNueva.text() != self.lineEditConfContr.text():
            mBox= QMessageBox()
            mBox.setText("La Contraseña Nueva No Coincide con la Confirmada")
            mBox.exec()
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

            mBox= QMessageBox()
            mBox.setText("La Contraseña Actualizada con Éxito")
            mBox.exec()

            eliminado= self.eventos.CambioContrasena()
            self.trazas=Traza(nombreUsuario=self.nombreUsuario,evento= eliminado)
            self.trazadata.insertarTraza(self.trazas)




