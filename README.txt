carpeta gui:
inicio.py esta programada la interfaz Login
principal.py esta prgramada la interfaz Principal de la Aplicacion
nuevoCalculo.py esta programada la interfaz Nuevo Calculo donde se entran los datos

carpeta model:
conexion.py se conecta con la base de datos tla.db , crea la tabla Usuarios y el usuario Administrador ,
retorna la conexion de la base de Datos
usuarios.py tiene la clase Usuario 
ecuaciones.py esta la funcion transporte_logitudinal_arena : Ecuacion para calcular

carpeta data 
tla.py esta la clase TLAData() donde estan los metodos para crear la tabla calculo, insertar los datos a 
tabla etc
usuario.py esta la clase UsuarioData se le pasa un objeto de tipo usuario Va a verificar que exita el 
usuario en la Base de Datos

carpeta database
Va estar la base de Datos 

SGCTS-Geocuba.py llama a inicio.py para ejecutar la aplicacion 

FORMAS EN QUE SE LLAMAN LAS VENTANAS
SGCTS-Geocuba.py llama a inicio.py
inicio.py llama a model.usuario para crear un objeto de tipo Usuario
inicio.py llama a data.usuario para verificar que el usuario es correcto
inicio.py llama a principal.py es la ventana que va despues del Login
principal.py llama a nuevoCalculo.py al presionar el boton Nuevo
nuevo.py llama a ecuaciones.py para realizar el Calculo
nuevo.py llama a tla.py para crear la tabla y guardar los datos 

ERRORES: 
 'TLAData' object has no attribute 'cursor'