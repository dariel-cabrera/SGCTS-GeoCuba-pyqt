import mongoose, { Types } from "mongoose"

const datosSchemaUsuario= mongoose.Schema({
    usuario: String,
    nombre:String,
    apellido:String,
    segundoApellido:String,
    ci:Number,
    tipoTrabajador:String,
    sexo:Boolean,
    correo:String,
    constrasena:String

}, {versionKey:false})

export const DatosModel= mongoose.model('datos',datosSchemaUsuario);

// Crear 
export const crearUsuario = async(usuario_,nombre_,apellido_,segundoApellido_,ci_,tipoTrabajador_,sexo_,correo_,constrasena_)=>{
    const datos = new DatosModel({
     usuario:usuario_,
     nombre:nombre_,
     apellido:apellido_,
     segundoApellido:segundoApellido_,
     ci:ci_,
     tipoTrabajador:tipoTrabajador_,
     sexo:sexo_,
     correo:correo_,
     constrasena:constrasena_,
    })
    const resultado = await datos.save()
    console.log(resultado)
  } 

  export const eliminarUsuario= async(id)=>{
    const datos = await DatosModel.deleteOne({_id:id})
  } 

  // Editar
export const actualizarUsuario= async(id,usuario_,nombre_,apellido_,segundoApellido_,ci_,tipoTrabajador_,sexo_,correo_,constrasena_)=>{
  const datos= await DatosModel.updateOne({_id:id},
  {
    $set:{
        usuario:usuario_,
        nombre:nombre_,
        apellido:apellido_,
        segundoApellido:segundoApellido_,
        ci:ci_,
        tipoTrabajador:tipoTrabajador_,
        sexo:sexo_,
        correo:correo_,
        constrasena:constrasena_,

    }
  })
} 