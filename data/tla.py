import sqlite3 

class TLAData():
    def __init__(self):
        self.db=sqlite3.connect('database/tla.db')
        try:
            cursor=self.db.cursor()
            sql_create_tla= """CREATE TABLE IF NOT EXISTS tla
                (id_tla INTERGER,
                Ubicacion TEXT,
                Densidad_mar  REAL,
                Densidad_arena REAL ,
                Coeficiente_porocidad REAL,
                Altura REAL,
                Angulo_rompiente REAL,
                Indice_rompiente REAL,
                Resultado REAL,  
                PRIMARY KEY(id_tla AUTOINCREMENT) """
            self.cursor().execute(sql_create_tla)
            self.db.commit()
            self.cursor().close()
            self.db.close()
            print("Tabla Creada ",ex)
        except  Exception as ex:
            print("Tabla Creada Ok ",ex)
    
    def insertar_datos_tla(self,Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado):
        self.cursor=self.db.cursor()
        self.cursor().execute(""" INSERT INTO tla values(null,'{}','{}','{}','{}','{}','{}','{}','{}')   """   
        .format(Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado))
        self.db.commit()
        
        if self.cursor.rowcount == 1:
            return True 
        else:
            return  False
        
        self.cursor().close()
        self.db.close()
    
    
    #def mostrar_datos_tla(self):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        #db="SELECT * FROM tabla_datos"
        #self.cursor().execute(db)
        #registro=cursor.fetchall()
        #return registro
    
    
    #def buscar_datos_tla(self,fecha):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        
        # db=""" SELECT * FROM tabla_datos WHERE Fecha={} """ .format(fecha)
        #cursor.execute(db)
        #fechaX= cursor.fetchall()
        #self.cursor().close()
        #return fechaX
    
    #def eliminar_datos_tla(self,id):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        #db=""" DELETE * FROM tabla_datos WHERE id_tla={} """ .format(id)
        #self.cursor().execute(db)
        #self.conexion.commit()
        #self.cursor().close()
    
    #def actualizar_datos_tla(self,id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result):
        #self.cursor=self.conexion.cursor()
        #db= """ UPDATE  tabla_datos VALUES(null,Ubicacion='{}',Densidad_mar ='{}',Densidad_arena='{}',Coeficiente_porocidad ='{}', Altura='{}',Angulo_rompiente='{}',Indice_rompiente ='{}',Fecha='{}',Resultado='{}')   """    .format (id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result)
        #self.cursor().execute(db)
        #a= self.cursor().rowcount
        #self.conexion.commit()
        #self.cursor().close()
        #return a
    

