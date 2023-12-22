import sqlite3

class Conexion ():
    def __init__(self):
        self.conexion=sqlite3.connect('database/tla.db')
    def conectar(self):
        return self.conexion   
    
   