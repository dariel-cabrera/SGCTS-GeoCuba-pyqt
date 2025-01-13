import React from 'react';
import PropTypes from 'prop-types';
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

{/*011 Comunicación entre Componentes  */}
{/* Prop son las propiedades que se envían a los componentes 

const PrimeraApp = ({ saludo }) => {
	
	return (
		<>
		 	<h1> { saludo } </h1>
			<p> 'MI primera aplicacion '</p>
		</>
    )
} 
export default PrimeraApp; 

Hay que tener en cuenta que si la propiedad no se manda del componente padre(index.js) voy a tener un undefine
Existe varias formas una de ellas es poner un valor por defecto 


*/}

{/* 012 PropTypes */}
{/* Se utiliza para realizar validaciones a los componentes. Los PropTypes 
son los tipos de Prop que va a recibir el componente.  */}

const PrimeraApp = ({ saludo }) => {
	
	return (
		<>
		 	<h1> { saludo } </h1>
			<p>MI primera aplicacion</p>
		</>
    )
} 
PrimeraApp.propTypes= {
	saludo: PropTypes.string 
    /*  // Le estoy diciendo que saludo tiene que ser un string pero no es obligatorio */
}
export default PrimeraApp;

{/* 
    Si quiero mandar un numero
React.render(<PrimeraApp /> saludo=[1,2,3] , divRoot);
Sale un error 

Si quiero que el saludo sea obligatorio
PrimeraApp.propTypes= {
	saludo: PropTypes.string.isRequired
     // Le estoy diciendo que saludo tiene que ser obligatorio 
}

*/}

