import mongoose from 'mongoose';
import {calculo} from './ecuaciones';

const resultado=calculo(3128,2543,16,4,2,25,9.8);
console.log(resultado);

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
    aceleracion: Number,
    resultado: Number,
    ubicacion:String,
    Q: Number,
    P:Number,
    K: Number
}, {versionKey:false})

const DatosModel= mongoose.model('datos',datosSchema)

//Mostrar 
const mostrar= async()=>{
  const datos= await DatosModel.find()
  console.log(datos)
}

// mostrar() 

// Crear 
export const crear = async(den_arena_,den_mar_,indice_,coeficiente_,altura_,angulo_,aceleracion_,ubicacion_,P_,Q_,K_)=>{
  const datos = new DatosModel({
   densidad_a:den_arena_,
   densidad_m: den_mar_,
   indice: indice_,
   coeficiente:coeficiente_,
   altura:altura_,
   angulo:angulo_,
   aceleracion:aceleracion_,
   ubicacion: ubicacion_,
   P:P_,
   Q:Q_,
   K:K_,
  })
  const resultado = await datos.save()
  console.log(resultado)
} 

// crear() 

// Editar
/* const actualizar= async(id)=>{
  const datos= await DatosModel.updateOne({_id:id},
  {
    $set:{


    }
 
  
  })
} */

// Eliminar
export const eliminar= async(id)=>{
  const datos = await DatosModel.deleteOne({_id:id})
} 

   
