import React from 'react';
import ReactDOM from 'react-dom'
import PrimeraApp from './PrimeraApp';
import './index.css';

// nota: Para importar el componente PrimeraApp  se escribe la palabra se borra la 
// ultima letra si le sale una referencia se presiona tab  y se importa sola

const divRoot = document.querySelector ('#app');
ReactDOM.render( <PrimeraApp  saludo= "Hola,Soy Goku" />, divRoot);
