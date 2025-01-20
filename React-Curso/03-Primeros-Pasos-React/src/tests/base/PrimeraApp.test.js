import React from 'react'
import {render} from '@testing-library/react'
import PrimeraApp from '../../PrimeraApp';

describe('Pruebas en <PrimeraApp/>',()=>{
	test('Debe de mostrar un mensaje Hola,soy Goku',()=>{
		const saludo ='Hola,soy Goku';
		//const wrapper=render(<PrimeraApp saludo={saludo} />);
		// wrapper.getByText() //Una Forma
		//Otra Forma
		const{getByText}=render(<PrimeraApp saludo={saludo} />);
		expect(getByText(saludo) ).toBeTheDocument();   // Mirar en el video
	
	});

});