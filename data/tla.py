import sqlite3 
from datetime import datetime 
from model.conexion import Conexion
class TLAData():  
    def insertar_datos_tla(self,Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado,IDUSUARIO):
        self.db= Conexion().conectar()
        fecha= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.cursor=self.db.cursor()
        res=(""" INSERT INTO calculo(UBICACION,DENSIDAD_MAR,DENSIDAD_ARENA,COEFICIENTE,ALTURA,ANGULO,INDICE,RESULTADO,FECHA,IDUSUARIO) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')   """   
        .format(Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado,fecha,IDUSUARIO))
        self.cursor.execute(res)
        self.db.commit()
        if self.cursor.rowcount == 1:
            self.cursor.close()
            self.db.close()
            return True
        else:
            self.cursor.close()
            self.db.close()
            return  False

       
        
        
    def mostrar_datos_tla(self):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo"
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 
    
    
    #def buscar_datos_tla(self,fecha):
        #self.cursor=self.db.cursor()
        
        #buscar=""" SELECT * FROM calculo WHERE Fecha={} """ .format(fecha)
        #cursor.execute(buscar)
        #fechaX= cursor.fetchall()
        #self.cursor.close()
        #return fechaX
    
    def buscar_datos_tla_DI(self,id):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        
        buscar=""" SELECT * FROM calculo WHERE ID={} """ .format(id)
        self.cursor.execute(buscar)
        iDX= self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return iDX
    
    def eliminar_datos_tla(self,id):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        eliminar=""" DELETE FROM calculo WHERE ID={} """ .format(id)
        self.cursor.execute(eliminar)
        self.db.commit()
        self.cursor.close()
        self.db.close()
    
    def calculosUsuarioEspecifico(self,id):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE IDUSUARIO='{}' ".format(id)
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 

       
    
    def actualizar_datos_tla(self,id_tla,ubicacion,dm,da,cp,hb,angulo,ir,result):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  calculo SET UBICACION='{}',DENSIDAD_MAR ='{}',DENSIDAD_ARENA='{}',COEFICIENTE ='{}', ALTURA='{}',ANGULO='{}',INDICE ='{}',RESULTADO='{}' WHERE ID= '{}'  """    .format (ubicacion,dm,da,cp,hb,angulo,ir,result,id_tla)
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a
    

