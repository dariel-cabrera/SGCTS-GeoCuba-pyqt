import { getHeroeByIdAsync } from "../../bases/10Promesas";
import { heroes } from "../../data/heroes";

describe('Pruebas con promesas',()=>{
	test('getHeroeByIdAsync debe retornar un Héroe ansync',(done)=>{
		const id= 1
		getHeroeByIdAsync(id)
		//El done siempre es bueno llamarlo determina se ha terminado la prueba se utiliza, principales cuando 
        //hay muchos expert 
		    .then( heroe => {
		     expect(heroe).toBe(heroes[1])
		     done();

		    });
               		
		
	});

	
	
	test('debe de obtener un error si el héroe por id no existe',(done)=>{
		const id=10;
		getHeroeByIdAsync(id)
		    .catch( error => {
			    expect(error).toBe('No se pudo entrar el heroe');
			    done();
		
	         });

	}); 


});