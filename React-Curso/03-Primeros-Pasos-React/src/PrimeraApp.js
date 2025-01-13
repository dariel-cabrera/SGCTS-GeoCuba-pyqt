import React from 'react'
// import { Fragment } from 'react';

{/* } 008 Nuestro Primer COmponente  
const  PrimeraApp = () => {
	return <h1>Hola Mundo </h1>
}
export default PrimeraApp;  */}

{/* 009 Retornar elementos en el componente Fragment  
Hay que importar el Fragment  import { Fragment } from 'react';
 


const  PrimeraApp = () => {
	return (
		<Fragment>    {/* Nota: Fragment + tab te lo importa solo 
            <h1>Hola Mundo </h1>
            <p>Mi primera aplicacion</p>
		</Fragment>
	)
}
export default PrimeraApp;   */}


{/* Existe una forma de hacer un Fragment más corta*/}

const  PrimeraApp = () => {
	return (
		<>     {/* Nota:Signos vacios react lo toma como  Fragment */}
             <h1>Hola Mundo </h1>
   <p>Mi primera aplicacion</p>
		</>
	)
}
export default PrimeraApp;
