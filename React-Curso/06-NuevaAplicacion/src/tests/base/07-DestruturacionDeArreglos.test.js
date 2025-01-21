import { retornaArreglo } from "../../bases/07DesestructuracionDeArreglod";

describe('Pruebas en Desestrucuración',()=>{
	test('debe de retornar un string y un numero',() =>{
        const[letras,numeros]=retornaArreglo();

		expect(letras).toBe('ABC')
		expect(numeros).toBe(123)

		//Tambien se puede probar por el tipo de Dato

		expect(typeof letras).toBe('string')
		expect(typeof numeros).toBe('number') 
		
	});
});
