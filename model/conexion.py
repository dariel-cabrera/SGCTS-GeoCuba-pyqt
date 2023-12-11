import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.conexion=sqlite3.connect('database/tla.db')
            self.crearTablas()
            self.crearAdmin()
        except Exception as ex:
            print (ex)
    
    def crearTablas(self):
        sql_create_table1= """CREATE TABLE IF NOT EXISTS usuarios
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT,
        usuario TEXT UNIQUE, 
        clave TEXT) """
        cur= self.conexion.cursor()
        cur.execute(sql_create_table1)
        cur.close()
    
    def crearAdmin(self):
        try:
            sql_insert= """INSERT INTO usuarios values(null,
            '{}','{}','{}') """.format("Administrador","Admin","admin2023.")
            cur= self.conexion.cursor()
            cur.execute(sql_insert)
            self.conexion.commit()
        except Exception as ex:
            print ("Ya se Creo el usuario",ex)
    

    def conectar(self):
        return self.conexion
        




