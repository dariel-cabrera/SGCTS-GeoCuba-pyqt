import { getHeroeById,getHeroeByOwner } from "../../bases/08Imp-Expor-funcComunesDeArr";
import { heroes } from "../../data/heroes";

describe('Pruebas en funciones de Heroes',()=>{
	test('debe de retornar un heroe por id',() =>{
        const id=1;
        const heroe=getHeroeById(id);
        const heroeData=heroes.find(h => h.id===id);
        expect(heroe).toEqual(heroeData);
		
	});
    // Prueba si se pasa un id que no exista 
    test('debe de retornar un undefined si Heroe no existe',() =>{
        const id=10;
        const heroe=getHeroeById(id);
        expect(heroe).toBe(undefined);
		
	});
    //Debe de retornat un arreglo con los heroesDC
    test('Debe de retornat un arreglo con los heroesDC',() =>{
        const ower='DC';
        const heroe=getHeroeByOwner(ower);
        const heroeData=heroes.find(h => h.id===id);
        expect(heroe).toEqual(heroeData);
		
	});
});
