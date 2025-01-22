import React from 'react';
import ReactDOM from 'react-dom'
import { GifExpectApp } from './GifExpectApp';
import './index.css';

// nota: Para importar el componente PrimeraApp  se escribe la palabra se borra la 
// ultima letra si le sale una referencia se presiona tab  y se importa sola

const divRoot = document.querySelector ('#app');
ReactDOM.render( <GifExpectApp />, divRoot);
