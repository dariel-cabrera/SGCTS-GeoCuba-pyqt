import sqlite3
import pathlib

class Conexion ():
    def __init__(self):
        mod_path = pathlib.Path(__file__).parent
        self.conexion=sqlite3.connect(mod_path/'tla.db')
    def conectar(self):
        return self.conexion   
    
   