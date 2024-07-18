import mongoose from 'mongoose';
const url= "mongodb://localhost:27017/MoreCoast"; 

mongoose.connect(url,{
}) 
    .then(()=>{
        console.log('Conectado a MongoDB exitosamente');
    })
    .catch((error) => {
      console.error('Error al conectar a MongoDB:', error);
    });

const datosSchema= mongoose.Schema({
    densidad_a: Number,
    densidad_m: Number,
    indice: Number,
    coeficiente:Number,
    altura: Number,
    angulo:Number,
    aceleracion: Number
}, {versionKey:false})

const DatosModel= mongoose.model('datos',datosSchema)

//Mostrar 
const mostrar= async()=>{
  const datos= await DatosModel.find()
  console.log(datos)
}

mostrar() 

const crear = async()=>{
  const datos = new DatosModel({
   densidad_a:3128,
   densidad_m:2653,
   indice:16,
   coeficiente:14,
   altura:23,
   angulo:98,
   aceleracion:98
  })
  const resultado = await datos.save()
} 

crear() 

   
