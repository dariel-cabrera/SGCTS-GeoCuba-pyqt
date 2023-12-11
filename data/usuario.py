from model.usuario import Usuario
from  model.conexion import Conexion


class UsuarioData():
    
    def login(self, usuario: Usuario):
        self.db=Conexion().conectar()
        self.cursor=self.db.cursor()
        res= self.cursor.execute("SELECT * FROM usuarios WHERE usuario='{}' AND clave='{}' " .format(usuario._usuario,usuario._clave))
        fila= res.fetchone()
        if fila:
           usuario=Usuario(nombre=fila[1],usuario=[2])
           self.cursor.close()
           self.db.close()
           return usuario
        else:
            return None 
            
        

