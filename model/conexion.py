import sqlite3

class Conexion ():
    def __init__(self):
        try:
            self.conexion=sqlite3.connect('database/tla.db')
            self.crearTablas()
            self.crearAdmin()
        except Exception as ex:
            print (ex)
            
    def conectar(self):
        return self.conexion   
    
   