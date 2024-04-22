from model.conexion import Conexion


class GData():
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS G
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        G REAL
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.insertarG()
        self.db.close() 

    def insertarG(self):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO G(ID,G) VALUES('{}','{}') """.format("1","9.8")
            self.cur= self.db.cursor()
            self.cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            self.cur.close()
            self.db.close()
            print ("Ya se Creo G",ex)
    
    def mostrarG(self):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM G"
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 
    
    def actualizarG (self,g):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  G SET G='{}' WHERE ID= '{}'  """    .format (g,"1")
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.cursor.close()
        self.db.close()
        return a
            