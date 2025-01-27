
import mongoose, { Types } from "mongoose"


const datosSchema= mongoose.Schema({
    densidad_a: Number,
    densidad_m: Number,
    indice: Number,
    coeficiente:Number,
    altura: Number,
    angulo:Number,
    aceleracion: Number,
    Q: Number,
    P:Number,
    K: Number
}, {versionKey:false})

export const DatosModel= mongoose.model('datos',datosSchema);


// Crear 
export const crear = async(den_arena_,den_mar_,indice_,coeficiente_,altura_,angulo_,aceleracion_,Q_,P_,K_)=>{
    const datos = new DatosModel({
     densidad_a:den_arena_,
     densidad_m: den_mar_,
     indice: indice_,
     coeficiente:coeficiente_,
     altura:altura_,
     angulo:angulo_,
     aceleracion:aceleracion_,
     P:P_,
     Q:Q_,
     K:K_,
    })
    const resultado = await datos.save()
    console.log(resultado)
  } 

  export const eliminar= async(id)=>{
    const datos = await DatosModel.deleteOne({_id:id})
  } 

  // Editar
export const actualizar= async(id,den_arena_,den_mar_,indice_,coeficiente_,altura_,angulo_,aceleracion_,Q_,P_,K_)=>{
  const datos= await DatosModel.updateOne({_id:id},
  {
    $set:{
     densidad_a:den_arena_,
     densidad_m: den_mar_,
     indice: indice_,
     coeficiente:coeficiente_,
     altura:altura_,
     angulo:angulo_,
     aceleracion:aceleracion_,
     P:P_,
     Q:Q_,
     K:K_,

    }
 
  
  })
} 