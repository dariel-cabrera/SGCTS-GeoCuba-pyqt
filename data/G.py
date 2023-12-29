from model.conexion import Conexion


class GData():

    def insertarG(self):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO G(G) VALUES('{}') """.format("9.8")
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
    
    def actualizarG (self,g,ganterior):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  G SET G='{}' WHERE G= '{}'  """    .format (g,ganterior)
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a