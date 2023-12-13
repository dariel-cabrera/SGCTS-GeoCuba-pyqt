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

