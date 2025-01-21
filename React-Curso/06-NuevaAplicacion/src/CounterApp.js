import React from "react"; 
import PropTypes from 'prop-types';
import { useState } from "react";

{/* Event Click 
    const CounterApp = ({value}) =>{

    const handleAdd = (e) => {
        console.log(e)
    }

   return (
     /* 
            <> 
                <h1> CounterApp</h1>
                <h2> { value } </h2>
    
                <button onClick = { (e) => {console.log(e) } }>+1</button> 
            </>
    

    
    //  Otra forma 
        <> 
			<h1> CounterApp</h1> 
			<h2> { value } </h2>

			<button onClick = { handleAdd } >+1</button> 
		</>

    )  

}

CounterApp.propTypes= {
	value: PropTypes.number
    
}
export default CounterApp; */ }

{/* useState 

const CounterApp = ({value}) =>{

// Hoocks no es más que una función.
const [nombre,setNombre]=useState('goku') 
const [counter,setCounter]=useState(value);
// Se realiza la desutructuración y se guardan en el primer argumento, el segundo crgumento es setAlgo.
// handleAdd
    const handleAdd=()=>{
        // setCounter(counter + 1); //No se puede hacer counter++
        //Tambien recibir una función que reciba el valor del counter. Retorna el nuevo valor
        setCounter((c) => c+1);

   }
    return (
            <> 
                <h1> CounterApp</h1>
                <h2> { counter} </h2>

                <button onClick = { handleAdd } >+1</button> 
            </>
    )

}

CounterApp.propTypes= {
	value: PropTypes.number
    
}
*/}
{/*handleSubtract y handleReset */}
const CounterApp = ({ value= 10}) => {
	const [counter,setCounter]=useState(value);

	const handleAdd = () => {
		setCounter(counter +1)
    }
    const handleRect = () => {
	setCounter(counter -1)
    }

    const handleReset = () => {
	setCounter(value)
    }


	return (
		<> 
			<h1> CounterApp</h1>
			<h2> { counter} </h2>

			<button onClick = { handleAdd } >+1</button> 
            <button onClick = { handleRect } >-1</button>
            <button onClick = { handleReset } >Reset</button>
		</>
    )

}

CounterApp.propTypes={
	value:PropTypes.number

}

export default CounterApp;