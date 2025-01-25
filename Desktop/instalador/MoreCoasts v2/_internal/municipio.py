from model.conexion import Conexion

class MunicipioData():
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS municipio
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE TEXT UNIQUE
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()        
    
    def insertarMunicipio(self,nombre):
        self.db=Conexion().conectar()
        try:
            sql_insert= """INSERT INTO municipio (NOMBRE) VALUES('{}') """.format(nombre)
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo el Municipio ",ex)
        if cur.rowcount == 1:
            cur.close()
            self.db.close()
            return True 
        else:
            cur.close()
            self.db.close()
            return  False


    def listaMunicipio (self):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        res=self.cursor.execute(""" SELECT * FROM municipio  order by NOMBRE """ ) 
        ubicaciones= res.fetchall()
        self.cursor.close()
        self.db.close()
        return ubicaciones
    
    def editarMunicipio(self,nombre,nombreant):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        actual= """ UPDATE  municipio SET NOMBRE= '{}' WHERE NOMBRE= '{}' """  .format(nombre,nombreant) 
        self.cursor.execute(actual)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a

    def eliminarMunicipio(self,nombre):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        eliminar=""" DELETE FROM municipio WHERE NOMBRE= '{}' """ .format(nombre)
        self.cursor.execute(eliminar)
        self.db.commit()
        self.cursor.close()
        self.db.close()