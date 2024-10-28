import mongoose from "mongoose";
import  express from "express" ;
import {actualizar, crear, eliminar }  from "./models/shema.js";
import cors from 'cors';
import { DatosModel } from "./models/shema.js";
import { DatosModelUsuario } from "./models/shemaUsuario.js";
import { actualizarUsuario,eliminarUsuario,crearUsuario } from "./models/shemaUsuario.js";




const app=express();
app.use(cors());
app.use(express.json());

app.listen(3001,()=>{

    console.log("Corriendo por el puerrto 3001")
})


const url= "mongodb://localhost:27017/MoreCoast";
mongoose.connect(url,{
 }) 
    .then(()=>{
        console.log('Conectado a MongoDB exitosamente');
    })
    .catch((error) => {
      console.error('Error al conectar a MongoDB:', error);
    });




app.post("/create",(req,res)=> {
 
  const densidad_a_= req.body.densidad_a;
  const densidad_m_ = req.body.densidad_m;
  const indice_= req.body.indice;
  const coeficiente_= req.body.coeficiente;
  const altura_ = req.body.altura;
  const angulo_= req.body.angulo;
  const aceleracion_= req.body.aceleracion;
  const Q_= req.body.Q;
  const P_= req.body.P;
  const K_= req.body.K;

  crear(densidad_a_,densidad_m_,indice_,coeficiente_,altura_,angulo_,aceleracion_,Q_,P_,K_);
  console.log("Datos Guardados");

})

app.get("/mostrar",async(req,res)=>{
    const resultado= await DatosModel.find()
    res.json(resultado);

  })
 

  app.put("/update",(req,res)=> {
    const _id= req.body._id
    const densidad_a_= req.body.densidad_a;
    const densidad_m_ = req.body.densidad_m;
    const indice_= req.body.indice;
    const coeficiente_= req.body.coeficiente;
    const altura_ = req.body.altura;
    const angulo_= req.body.angulo;
    const aceleracion_= req.body.aceleracion;
    const Q_= req.body.Q;
    const P_= req.body.P;
    const K_= req.body.K;
  
    actualizar(_id,densidad_a_,densidad_m_,indice_,coeficiente_,altura_,angulo_,aceleracion_,Q_,P_,K_);
    console.log("Datos Guardados",_id);
  
  })
 
 app.delete("/delete/:id",(req,res)=>{
    const id= req.params.id;
    console.log(id);
    eliminar(id);

 })

 app.get("/mostrarUsuario",async(req,res)=>{
  const resultado= await DatosModelUsuario.find()
  res.json(resultado);

})

pp.post("/createUsuario",(req,res)=> {
 
  const usuario_= req.body.usuario;
  const nombre_= req.body.nombre;
  const apellido_=req.body.apellido;
  const segundoApellido_=req.body.segundoApellido;
  const ci_=req.body.ci;
  const tipoTrabajador_=req.body.tipoTrabajador;
  const sexo_= req.body.sexo;
  const correo_=req.body.correo;
  const constrasena_= req.body.constrasena;

  crearUsuario(usuario_,nombre_,apellido_,segundoApellido_,ci_,tipoTrabajador_,sexo_,correo_,constrasena_);
  console.log("Datos Guardados");

})

app.put("/updateUsuario",(req,res)=> {
  const _id= req.body._id;
  const usuario_= req.body.usuario;
  const nombre_= req.body.nombre;
  const apellido_=req.body.apellido;
  const segundoApellido_=req.body.segundoApellido;
  const ci_=req.body.ci;
  const tipoTrabajador_=req.body.tipoTrabajador;
  const sexo_= req.body.sexo;
  const correo_=req.body.correo;
  const constrasena_= req.body.constrasena;
  

  actualizarUsuario(_id,usuario_,nombre_,apellido_,segundoApellido_,ci_,tipoTrabajador_,sexo_,correo_,constrasena_);
  console.log("Datos Guardados",_id);

})








