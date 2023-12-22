from model.usuario import Usuario
from model.conexion import Conexion


class UsuarioData():
    def crearTablas(self):
        self.db=Conexion().conectar()
        cur=self.db.cursor()
        sql_create_table1= """CREATE TABLE IF NOT EXISTS usuarios
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE TEXT,
        USUARIO TEXT UNIQUE, 
        CLAVE TEXT,
        PRIMERAPELLIDO TEXT,
        SEGUNDOAPELLIDO TEXT,
        CI TEXT UNIQUE,
        CORREO TEXT,
        TIPOTRABAJADOR TEXT,
        SEXO TEXT,
        ) """
        cur.execute(sql_create_table1)
        cur.close()
        self.db.close()
        
        
    
    def crearAdmin(self):
        self.db=Conexion().conectar()
        try:
            sql_insert= """INSERT INTO usuarios values(
            '{}','{}','{}') """.format("Administrador","Admin","admin2023.")
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo el usuario",ex)
        cur.close()
        self.db.close()
        
        
    
    def crearUsuario(self,usuario:Usuario):
        self.db=Conexion().conectar()
        try:
            sql_insert= """INSERT INTO usuarios(NOMBRE,USUARIO,CLAVE,PRIMERAPELLIDO,SEGUNDOAPELLIDO,CI,CORREO,TIPOTRABAJADOR,SEXO) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}') """.format(usuario._nombre,usuario._usuario,usuario._clave,usuario._primerApellido,usuario._segundoApellido,usuario._ci,usuario._correo,usuario._tipotrabajador,usuario._sexo)
            cur= self.db.cursor()
            cur.execute(sql_insert)
            self.db.commit()
        except Exception as ex:
            print ("Ya se Creo el usuario",ex)
        if cur.rowcount == 1:
            cur.close()
            self.db.close()
            return True 
        else:
            cur.close()
            self.db.close()
            return  False
        
        


    def login(self, usuario: Usuario):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        res= self.cursor.execute("SELECT * FROM usuarios WHERE USUARIO='{}' AND CLAVE='{}' " .format(usuario._usuario,usuario._clave))
        fila= res.fetchone()
        if fila:
           usuario=Usuario(nombre=fila[0],usuario=fila[2])
           self.cursor.close()
           self.db.close()
           return usuario
        else:
            self.cursor.close()
            self.db.close()
            return None 
        

    def mostrarUsuario(self):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        mostrar="SELECT * FROM usuarios"
        self.cursor.execute(mostrar)
        registro=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return registro 
    
    def eliminarUsuario(self,id):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        eliminar=""" DELETE FROM usuarios WHERE ID={} """ .format(id)
        self.cursor.execute(eliminar)
        self.db.commit()
        self.cursor.close()
        self.db.close()
        
    
    def buscarusuarioID (self,id):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        buscar=""" SELECT * FROM usuarios WHERE ID={} """ .format(id)
        self.cursor.execute(buscar)
        iDX= self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return iDX
    
    def buscarusuarinombre (self,nombre):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        buscar=""" SELECT * FROM usuarios WHERE USUARIO={} """.format(nombre)
        self.cursor.execute(buscar)
        iDX=self.cursor.fetchall()
        self.cursor.close()
        self.db.close()
        return iDX
        
            
    def actualizarUsuario(self,usuario:Usuario,ID):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        actualizar= """ UPDATE  usuarios SET NOMBRE= '{}',USUARIO= '{}',CLAVE='{}',PRIMERAPELLIDO = '{}' ,SEGUNDOAPELLIDO= '{}',CI='{}',CORREO='{}',TIPOTRABAJADOR = '{}',SEXO='{}' WHERE ID= '{}'  """    .format(usuario._nombre,usuario._usuario,usuario._clave,usuario._primerApellido,usuario._segundoApellido,usuario._ci,usuario._correo,usuario._tipotrabajador,usuario._sexo,ID)
        self.cursor.execute(actualizar)
        a= self.cursor.rowcount
        self.db.commit()
        self.cursor.close()
        self.db.close()
        return a
 
            