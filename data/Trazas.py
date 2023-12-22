from model.conexion import Conexion
from model.traza import Traza
from datetime import datetime 

class TrazaData():
    def __init__(self):
        
        self.fecha= datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    def insertarTraza(self,traza:Traza):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO Trazas(NOMBRE,FECHA,EVENTO) VALUES('{}','{}','{}') """.format(traza._nombreUsuario,traza._evento,self.fecha)
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
    
        
        
        