import { heroes } from "../data/heroes";

const getHeroeById= (id)=>heroes.find((heroe)=>heroe.id===id) ;

console.log(getHeroeById(2));


// find? filter 
const getHeroeByOwner= (ower)=> heroes.filter((heroe) => heroe.owner===owner);
console.log(getHeroeByOwner('Marvel'));


// Multiples Exportaciones 
/* 
    exportaciones por defecto 
    export default [
    
    
    ]
 
    import heroes from "../data/heroes"; -> No es conveniente porque le puedo poner el nombre que queramos 
    
    const heroes = [
    
    
    ]
    export default heores; 

    export const oweners = ['DC','Marvel'] -> Exportacion individual 

     import heroes {oweners} from "../data/heroes";  -> Para importar un exportacion individual se usa {}

*/