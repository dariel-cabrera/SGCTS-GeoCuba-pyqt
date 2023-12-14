import sqlite3 

class TLAData():
    def __init__(self):
        self.db=sqlite3.connect('database/tla.db')
    
        
    def insertar_datos_tla(self,Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado):
        self.cursor=self.db.cursor()
        res=(""" INSERT INTO calculo(UBICACION,DENSIDAD_MAR,DENSIDAD_ARENA,COEFICIENTE,ALTURA,ANGULO,INDICE,RESULTADO) values('{}','{}','{}','{}','{}','{}','{}','{}')   """   
        .format(Ubicacion,Densidad_mar,Densidad_arena,Coeficiente_porocidad,Altura,Angulo_rompiente,Indice_rompiente,Resultado))
        self.cursor.execute(res)
        self.db.commit()
        
        if self.cursor.rowcount == 1:
            return True 
        else:
            return  False
        
        self.cursor().close()
        self.db.close()
    
    
    #def mostrar_datos_tla(self):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        #db="SELECT * FROM tabla_datos"
        #self.cursor().execute(db)
        #registro=cursor.fetchall()
        #return registro
    
    
    #def buscar_datos_tla(self,fecha):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        
        # db=""" SELECT * FROM tabla_datos WHERE Fecha={} """ .format(fecha)
        #cursor.execute(db)
        #fechaX= cursor.fetchall()
        #self.cursor().close()
        #return fechaX
    
    #def eliminar_datos_tla(self,id):
        #self.conexion= Conexion().conectar()
        #self.cursor=self.conexion.cursor()
        #db=""" DELETE * FROM tabla_datos WHERE id_tla={} """ .format(id)
        #self.cursor().execute(db)
        #self.conexion.commit()
        #self.cursor().close()
    
    #def actualizar_datos_tla(self,id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result):
        #self.cursor=self.conexion.cursor()
        #db= """ UPDATE  tabla_datos VALUES(null,Ubicacion='{}',Densidad_mar ='{}',Densidad_arena='{}',Coeficiente_porocidad ='{}', Altura='{}',Angulo_rompiente='{}',Indice_rompiente ='{}',Fecha='{}',Resultado='{}')   """    .format (id_tla,ubicacion,dm,da,cp,hb,a,ir,fecha,result)
        #self.cursor().execute(db)
        #a= self.cursor().rowcount
        #self.conexion.commit()
        #self.cursor().close()
        #return a
    

