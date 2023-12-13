from model.conexion import Conexion

class TLA():
    def __init__(self):
        self.crear_tabla_tla()
        
    
    def crear_tabla_tla(self):
        self.conexion= Conexion().conectar()
        cursor=self.conexion.cursor()
        db= """CREATE TABLE IF NOT EXISTS tla
            (id_tla INTERGER,
            Ubicacion VARCHAR(100),
            Densidad_mar  REAL,
            Densidad_arena REAL ,
            Coeficiente_porocidad REAL,
            Altura REAL,
            Angulo_rompiente REAL,
            Indice_rompiente REAL,
            Fecha DATE,
            Resultado REAL,  
            PRIMARY KEY(id_sgcts AUTOINCREMENT) """
        cursor.execute(db)
        cursor.close()
    
    def insertar_datos_tla(self,ubicacion,dm,da,cp,hb,a,ir,fecha,result):
        self.conexion= Conexion().conectar()
        cursor=self.conexion.cursor()
        db= """ INSERT INTO tabla_datos VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}')   """   .format      (ubicacion,dm,da,cp,hb,a,ir,fecha,result)
        cursor.execute(db)
        self.conexion.commit()
        cursor.close()
    
    def mostrar_datos_tla(self):
        self.conexion= Conexion().conectar()
        cursor=self.conexion.cursor()
        db="SELECT * FROM tabla_datos"
        cursor.execute(db)
        registro=cursor.fetchall()
        return registro
    
    def buscar_datos_tla(self,fecha):
        self.conexion= Conexion().conectar()
        cursor=self.conexion.cursor()
        db=""" SELECT * FROM tabla_datos WHERE Fecha={} """ .format(fecha)
        cursor.execute(db)
        fechaX= cursor.fetchall()
        cursor.close()
        return fechaX
    
    def eliminar_datos_tla(self,id):
        self.conexion= Conexion().conectar()
        cursor=self.conexion.cursor()
        db=""" DELETE * FROM tabla_datos WHERE id_tla={} """ .format(id)
        cursor.execute(db)
        self.conexion.commit()
        cursor.close()
    
    def actualizar_datos_tla(self,id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result):
        cursor=self.conexion.cursor()
        db= """ UPDATE  tabla_datos VALUES(null,Ubicacion='{}',Densidad_mar ='{}',Densidad_arena='{}',Coeficiente_porocidad ='{}', Altura='{}',Angulo_rompiente='{}',Indice_rompiente ='{}',Fecha='{}',Resultado='{}')   """    .format (id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result)
        cursor.execute(db)
        a= cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return a
    

