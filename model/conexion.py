import sqlite3

class Conexion ():
    def __init__(self):
        try:
            self.conexion=sqlite3.connect('database/tla.db')
        except Exception as ex:
            print (ex)
        self.conectar()
    
    def conectar(self):
        return self.conexion
    
   