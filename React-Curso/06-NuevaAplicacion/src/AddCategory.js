
import PropTypes from 'prop-types'
import React, { useState} from 'react'

const AddCategory = ((props) => {
    const [inputValue,setInputValue]=useState('Hola Mundo')

	const handleInputChange=(e) => {
		setInputValue(e.target.value);
	}
	return (
		<form>
			<h1>{inputValue}</h1>
			<input 
				Type="text"
				Value={inputValue}
				onChange={handleInputChange}
            />
		</form>
        /*// Comportamiento de la Tecla enter se elimina el Fragment porque 
        le form agrupa los elementos. No es necesario usarlo */

    )

})

AddCategory.propTypes = {}

export default AddCategory