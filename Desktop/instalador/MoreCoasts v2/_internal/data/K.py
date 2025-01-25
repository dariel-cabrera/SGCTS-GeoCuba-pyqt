from model.conexion import Conexion


class KData():
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS K
        ( ID INTEGER PRIMARY KEY AUTOINCREMENT,
        K REAL 
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.insertarK()
        self.db.close()        

    def insertarK(self):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO K(ID,K) VALUES('{}','{}') """.format("1","0.77")
            self.cur= self.db.cursor()
            self.cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            self.cur.close()
            self.db.close()
            print ("Ya se Creo la K",ex)
    
    def mostrarK(self):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM K"
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 

    def actualizarK(self,k):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
    
        actualizar= """ UPDATE  K SET K='{}' WHERE ID= '{}'  """    .format (k,"1")
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a
        

