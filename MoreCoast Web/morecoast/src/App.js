import React from 'react';
import { useState } from 'react';
import './App.css';



function App() {


  const [densidad_a,setDensidadA]=useState(0);
  const [densidad_m,setDensidadM]=useState(0);
  const [coeficiente,setCoeficiente]=useState(0);
  const [indice,setIndice]=useState(0);
  const [altura,setAltura]=useState(0);
  const [angulo,setAngulo]=useState(0);
  const [aceleracion,setAcelereacion]=useState(0);

  const mostrarDatos = () => {
    alert(densidad_a);
  }


  return (
    <div className="App">
      <div className="datos_calculos">
      <label>Densidad de Arena: <input 
      onChange={(event)=>{
        setDensidadA(event.target.value);
      }}
      type="number"></input></label>
      <label>Densidad del Mar: <input 
      onChange={(event)=>{
        setDensidadM(event.target.value);
      }}
      type="number"></input></label> 
      <label>Coeficiente de Porocidad: <input 
      onChange={(event)=>{
        setCoeficiente(event.target.value);
      }}
      type="number"></input></label>
      <label>Indice de Rompiente: <input 
      onChange={(event)=>{
        setIndice(event.target.value);
      }}
      type="number"></input></label>
      <label>Altura: <input 
      onChange={(event)=>{
        setAltura(event.target.value);
      }}
      type="number"></input></label>
      <label>Angulo: <input 
      onChange={(event)=>{
        setAngulo(event.target.value);
      }}
      type="number"></input></label>
      <label>Aceleracion Gravedad: <input 
      onChange={(event)=>{
        setAcelereacion(event.target.value);
      }}
      type="number"></input></label>
      <button onClick={mostrarDatos}>Calcular</button>
      </div>
    </div>
  );
 
}

export default App;

