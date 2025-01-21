import { getUsuarioActivo , getUser } from "../../bases/05Funciones";

describe('Pruebas en 05-funciones',()=>{

	test('getUser debe de retornar un objeto',() =>{
	const userTest={
		Uid:'ABC123',
		Username:'El Papi 1502'
     }
	const user=getUser();
	expect(user).toEqual(userTest)
    });
//ToBe no se puede utilizar para comparar objetos se debe usar toEqual
// Tarea 
	test('getUsuarioActivo debe retornar un objeto',()=>{
	    const nombre='Juan';
		const user=getUsuarioActivo(nombre);
        expect(user).toEqual({
			uid:'ABC567',
			username:nombre
     	});
    });
});
