from  model.conexion import Conexion
from  model.variables import Variables
class ClaData():
    def __init__(self):
        try:
            self.db= Conexion().conectar()
            self.cursor=self.db.cursor()
            sql_create_tla= """CREATE TABLE IF NOT EXISTS cla
            (id_tla INTERGER,
            ubicacion VARCHAR(100),
            densidad_mar  REAL,
            densidad_arena REAL ,
            coeficiente_porocidad REAL,
            altura REAL,
            angulo_rompiente REAL,
            indice_rompiente REAL,
            fecha DATE,
            resultado REAL,  
            PRIMARY KEY(id_sgcts AUTOINCREMENT) """
            self.cursor().execute(sql_create_cla)
            self.cursor().close()
            self.db.close()
        except:
            print("Tabla Creada ")

    def guardarDatosNuevos(self, info: Variables):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        self.cursor.execute("""INSERT INTO values VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}')   """.format (info._ubicacion,info._densidadM,info._densidadA,info._coeficiente,info._altura,info._angulo,info._indice,info._fecha,info._resultado)
        )
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True 
        else:
            return  False
        
        