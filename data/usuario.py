from model.usuario import Usuario
from  model.conexion import Conexion


class UsuarioData():
    def __init__(self):
        self.db=Conexion().conectar()

    def crearTablas(self):
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE TEXT,
        USUARIO TEXT UNIQUE, 
        CLAVE TEXT,
        PRIMERAPELLIDO TEXT,
        SEGUNDOAPELLIDO TEXT,
        CI TEXT,
        CORREO TEXT,
        TIPOTRABAJADOR TEXT,
        SEXO TEXT,
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()
    
    def crearAdmin(self):
        try:
            sql_insert= """INSERT INTO usuarios values(null,
            '{}','{}','{}') """.format("Administrador","Admin","admin2023.")
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo el usuario",ex)
        cur.close()
        self.db.close()
    
    def crearUsuario(self,usuario:Usuario):
        
        try:
            sql_insert= """INSERT INTO usuarios(NOMBRE,USUARIO,CLAVE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,CI,CORREO,TIPOTRABAJADOR,SEXO) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}') """.format(usuario._nombre,usuario._usuario,usuario._clave,usuario._primerApellido,usuario._segundoApellido,usuario._ci,usuario._correo,usuario._tipotrabajador,usuario._sexo)
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo el usuario",ex)
        if cur.rowcount == 1:
            return True 
        else:
            return  False
        cur.close()
        self.db.close()

    def login(self, usuario: Usuario):
        self.cursor=self.db.cursor()
        res= self.cursor.execute("SELECT * FROM usuarios WHERE USUARIO='{}' AND CLAVE='{}' " .format(usuario._usuario,usuario._clave))
        fila= res.fetchone()
        if fila:
           usuario=Usuario(nombre=fila[1],usuario=[2])
           self.cursor.close()
           self.db.close()
           return usuario
        else:
            return None 
    


    def mostrarUsuario(self):
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM usuarios"
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        return registro 
    
 
            