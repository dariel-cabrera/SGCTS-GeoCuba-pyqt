from model.conexion import Conexion

class UbicacionData():
    def __init__(self):
        try:
            self.crearTablas()
        except Exception as ex:
            print(ex)
    
    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS ubicaciones
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE TEXT,
        NOMBREMUNICIPIO TEXT, 
        LATITUD REAL,
        LONGITUD REAL,
        FOREIGN KEY("NOMBREMUNICIPIO") REFERENCES "municipio"("NOMBRE")
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()
    
    def insertarUbicacion(self,nombre,nombreM,latitud,longitud):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        try:
            sql_insert= """INSERT INTO ubicaciones (NOMBRE,NOMBREMUNICIPIO,LATITUD,LONGITUD) VALUES('{}','{}','{}','{}') """.format(nombre,nombreM,latitud,longitud)
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo la Ubicacion",ex)
        if cur.rowcount == 1:
            cur.close()
            self.db.close()
            return True 
        else:
            cur.close()
            self.db.close()
            return  False


    def listaUbicaciones (self,nombreM):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        res=self.cursor.execute(""" SELECT * FROM ubicaciones WHERE NOMBREMUNICIPIO ='{}' order by NOMBRE """  .format(nombreM))
        ubicaciones= res.fetchall()
        self.cursor.close()
        self.db.close()
        return ubicaciones
    
    def editarUbicacion(self,nombre,nombreM,latitud,longitud,nombreant):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        actual= """ UPDATE  ubicaciones SET NOMBRE= '{}', NOMBREMUNICIPIO='{}',LATITUD='{}',LONGITUD='{}' WHERE NOMBRE= '{}' """  .format(nombre,nombreM,latitud,longitud,nombreant) 
        self.cursor.execute(actual)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a
    
    def eliminarUbicacion(self,nombre):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        eliminar=""" DELETE FROM ubicaciones WHERE NOMBRE= '{}' """ .format(nombre)
        self.cursor.execute(eliminar)
        self.db.commit()
        self.cursor.close()
        self.db.close()
    
    def buscarUbicacion(self,nombre):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        buscar=""" SELECT * FROM ubicaciones WHERE NOMBRE= '{}' """.format(nombre)
        self.cursor.execute(buscar)
        iDX= self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return iDX
 


