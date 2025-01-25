from model.conexion import Conexion
from model.traza import Traza
from datetime import datetime 

class TrazaData():
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)

        self.fecha= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS Trazas
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	    NOMBRE	TEXT,
	    FECHA	TEXT,
	    EVENTO	TEXT
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()
        
    def insertarTraza(self,traza:Traza):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO Trazas(NOMBRE,FECHA,EVENTO) VALUES('{}','{}','{}') """.format(traza._nombreUsuario,self.fecha,traza._evento,)
            self.cur= self.db.cursor()
            self.cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            self.cur.close()
            self.db.close()
            print ("Ya se Creo la traza",ex)
    
    def mostrarTraza(self):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM Trazas"
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 
    
    def eliminarTraza (self,id):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        eliminar=""" DELETE FROM Trazas WHERE ID={} """ .format(id)
        self.cursor.execute(eliminar)
        self.db.commit()
        self.cursor.close()
        self.db.close()
    
    def buscarPorFecha(self,fechaDesde,fechaHasta):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="""SELECT * FROM Trazas WHERE FECHA >= '{}' AND FECHA <='{}' """.format(fechaDesde,fechaHasta)
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    
    
        
        
        
        