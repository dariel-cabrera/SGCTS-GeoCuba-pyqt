/* Mi primera Prueba 
test('debe de ser true',()=>{
	const isActive=true;
	if(!isActive){
		throw new Error ('No esta activo' ) ;
	}
}); */

/* 006 Test-Expert-toBe */
/*
test('deben de ser iguales los string',() =>{
	//1.Inicializacion
	const mensaje='Hola Mundo';
	//2.Estimulo 
	const mensaje2='Hola Mundo';
	//3.Observacion del comportamiento
    expect(mensaje).toBe(mensaje2);
	
});*/

describe('Pruebas en el archivo demo.test.js',()=>{
	test('deben de ser iguales los string',() =>{
	//1.Inicializacion
	const mensaje='Hola Mundo'
	//2.Estimulo 
	const mensaje2='Hola Mundo'
	//3.Observacion del comportamiento
    expect(mensaje).toBe(mensaje2);
      });
});
//Nota To Be Compara si son iguales 
//https://jestjs.io -> Documentacion 

