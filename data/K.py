from model.conexion import Conexion


class KData():

    def insertarK(self):
        self.db= Conexion().conectar()
        try:
            sql_insert= """INSERT INTO K(K) VALUES('{}') """.format("0.77")
            self.cur= self.db.cursor()
            self.cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            self.cur.close()
            self.db.close()
            print ("Ya se Creo la traza",ex)
    
    def mostrarK(self):
        self.db= Conexion().conectar()
        cursor=self.db.cursor()
        mostrar="SELECT * FROM K"
        cursor.execute(mostrar)
        registro=cursor.fetchall()
        cursor.close()
        self.db.close()
        return registro 

    def actualizarK(self,k,kanterior):
        self.db= Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  K SET K='{}' WHERE K= '{}'  """    .format (k,kanterior)
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a

