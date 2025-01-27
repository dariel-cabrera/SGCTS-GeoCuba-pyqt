import sqlite3 
from datetime import datetime 
from model.conexion import Conexion
class TLAData():  
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS calculo
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        UBICACION REAL,
        DENSIDAD_MAR REAL, 
        DENSIDAD_ARENA REAL,
        COEFICIENTE REAL,
        ALTURA REAL,
        ANGULO REAL,
        INDICE REAL,
        RESULTADO REAL,
        FECHA TEXT,
        IDUSUARIO INTEGER,
        K REAL,
        G REAL,
        P REAL,
        FOREIGN KEY("UBICACION") REFERENCES "ubicaciones"("NOMBRE"),
	    FOREIGN KEY("G") REFERENCES "G"("G"),
	    FOREIGN KEY("IDUSUARIO") REFERENCES "usuarios"("ID")
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()

    def insertar_datos_tla(self,Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado,IDUSUARIO,K,G,P):
        self.db= Conexion().conectar()
        fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor=self.db.cursor()
        res=(""" INSERT INTO calculo(UBICACION,DENSIDAD_MAR,DENSIDAD_ARENA,COEFICIENTE,ALTURA,ANGULO,INDICE,RESULTADO,FECHA,IDUSUARIO,K,G,P) values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')   """   
        .format(Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado,fecha,IDUSUARIO,K,G,P))
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
    
    def buscarPorFechaUsuario(self,fechaDesde,fechaHasta,id):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE IDUSUARIO='{}' and FECHA >='{}' and FECHA <= '{}' ".format(id,fechaDesde,fechaHasta)
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    
    def buscarPorFechaUbicUsuario(self,fechaDesde,fechaHasta,id,Ubicacion):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE IDUSUARIO='{}' and FECHA >='{}' and FECHA <= '{}' and UBICACION='{}' ".format(id,fechaDesde,fechaHasta,Ubicacion)
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    
    def buscarCalculoAdministrador(self,nombreUbicacion,fechaDesde,fechaHasta):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE  UBICACION='{}' and FECHA >='{}' and FECHA <= '{}' ".format(nombreUbicacion,fechaDesde,fechaHasta)
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    
    def buscarPorFechaAdmin(self,fechaDesde,fechaHasta):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE FECHA >='{}' and FECHA <= '{}' ".format(fechaDesde,fechaHasta)
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    

    
    def calculosUsuarioEspecifico(self,id):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM calculo WHERE IDUSUARIO='{}'  ".format(id)
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 

       
    
    def actualizar_datos_tla(self,id_tla,ubicacion,dm,da,cp,hb,angulo,ir,result,k,g,P):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  calculo SET UBICACION='{}',DENSIDAD_MAR ='{}',DENSIDAD_ARENA='{}',COEFICIENTE ='{}', ALTURA='{}',ANGULO='{}',INDICE ='{}',RESULTADO='{}',K='{}',G='{}',P= '{}' WHERE ID= '{}'  """    .format (ubicacion,dm,da,cp,hb,angulo,ir,result,k,g,P, id_tla)
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a
    

