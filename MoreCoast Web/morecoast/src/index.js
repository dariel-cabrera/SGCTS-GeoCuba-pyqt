import React from "react";
import  ReactDOM  from "react-dom/client";
import App from './App.js';
import './index.css';



/* const datosSchema= mongoose.Schema({
   densidad_a:Float64Array,
   densidad_m:Float64Array,
   indice:Float64Array,
   coeficiente:Float64Array,
   altura:Float64Array,
   angulo:Float64Array,
   aceleracion:Float64Array
})

const DatosModel= mongoose.model('datos',datosSchema)

//Mostrar 
const mostrar= async()=>{
  const datos= await DatosModel.find()
  console.log(datos)
}

mostrar()
// Crear
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
} */ 



const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
    <React.StrictMode>
        <App/>
    </React.StrictMode>
);




