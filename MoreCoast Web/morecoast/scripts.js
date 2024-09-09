const mongoose= require("mongoose")
const url= "mongodb://localhost:27017/MoreCoast"

mongoose.connect(url) 
    .then(()=>{
        console.log('Conectado a MongoDB exitosamente');
    })
    .catch((error) => {
      console.error('Error al conectar a MongoDB:', error);
    });

