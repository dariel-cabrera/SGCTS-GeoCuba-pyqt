import React,{useState}from 'react'
import AddCategory from './AddCategory'

export const GifExpectApp = () => {
    // const categories= ['Micky','Pluma', 'Escudo'];

    const [categories, setCategories] = useState(['Micky','Pluma', 'Escudo'])

    const handleAdd= () => {
        setCategories([...categories,'Dominicana'])// Forma Correcta se inserta al final
        /* setCategories(['Dominicana',...categories])// Forma Correcta se inserta al inicio
        setCategories(cats => [… cats,' Dominicana'])// Otra forma */
    }
    

    /* return (
		<> 
			<h2>GifExpertApp </h2>
			<hr/>

			<ol>
                {
                    categories.map(category =>{
                        return <li> hola </li>
                    })
                }
{/*Da un error porque necesita un key. Un error es poner el valor del key con el 
índice i categories.map((category,i) => {return <li key=i > hola <li/> })
Nota: El key no puede ser el índice, tiene que ser un id único por lo general 
se pasa el id de la base de datos
                 
            </ol>
		</>
    )
 */ 
      return (
        <>
           <h2>GifExpertApp </h2>
           <AddCategory/>
           <hr/>
           
           <ol>
                {
                    categories.map(category =>{
                        return <li key={category}>{category}</li>
                    })
                }
            </ol>
        </>
    )
}