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

{/* const  PrimeraApp = () => {
	return (
		<>     {/* Nota:Signos vacios react lo toma como  Fragment 
             <h1>Hola Mundo </h1>
   <p>Mi primera aplicacion</p>
		</>
	)
}
export default PrimeraApp; */}

{/* 010 Impresión de variables en el HTML 

const  PrimeraApp = () => {
	const saludo = 'Hola Mundo'; 
	
return (
		<>     
             <h1> {saludo } </h1>
   <p>Mi primera aplicacion</p>
		</>
	)
}
export default PrimeraApp; */}

{/* Nota: Se puede imprimir datos primitivos String,Numeros, Float y Arreglos. 
    Los Booleanos no se muestra, en caso de los Objetos no se puede hacer de la manera anterior.

const  PrimeraApp = () => {
	const saludo ={
		nombre:’Fernando’,
		edad: 34

}	
return (
		<>     
             <h1> {JSON.stringify (saludo) } </h1>
             /*<pre> {JSON.stringify (saludo,null,3) } </pre>  // Lo convierte a string 
                                                               // Te sale en formato código 
   <p>Mi primera aplicacion</p>
		</>
	)
}
export default PrimeraApp; */}

{/*Comunicación entre Componentes  */}
{/* Prop son las propiedades que se envían a los componentes */}

const PrimeraApp = ({ saludo }) => {
	
	return (
		<>
		 	<h1> { saludo } </h1>
			<p> 'MI primera aplicacion '</p>
		</>
    )
} 
export default PrimeraApp;