import { getSaludo } from "../../bases/02template-string";

describe('Pruebas en 02-template-string.js',()=>{
	test('prueba en el método getSaludo',() =>{
	const nombre='Ferando';
	const saludo= getSaludo(nombre);
    expect(saludo).toBe('Hola ' +  nombre + ' !');
    });
});

/*Nota 
Importar:  import ’testing-library/jest-dom’ esto me importa todos los métodos de expert

En la consola
SI quiero que me salgan solo las pruebas de una archivo en especifico presiono p o la que la opción de to filter by a filename regex patterm. Escribe el nombre de la prueba y seleccionamos (flecha abajo)
*/
