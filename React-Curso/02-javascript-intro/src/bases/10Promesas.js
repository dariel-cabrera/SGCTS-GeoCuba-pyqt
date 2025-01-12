
// Promesas 
import { heroes } from "../data/heroes";
import { getHeroeById } from "./08Imp-Expor-funcComunesDeArr";

/* const promesa = new Promise((resolve,reject)=> {
    
    setTimeout(()=>{
        // Tarea 
        const h1 = getHeroeById(2);

        resolve(h1); // SI encuentra al heroe lo envia al then
        // reject('No se pudo encontrar el héroe') // Lo envia al .catch
       
    },2000)

});

promesa.then((heroe)=>{
    console.log('heroe',heroe)
})


.catch(err =>console.warn(err)); */

const getHeroeByIdAsync=(id)=>{
    return promesa = new Promise((resolve,reject)=> {
    
        setTimeout(()=>{ 
            const h1 = getHeroeById(id);
            if(h1 === undefined){
                reject('No se pudo encontrar el héroe');
            }
            resolve(h1);
        },2000)

});

}

getHeroeByIdAsync(4)
    .then( console.log)
    .catch(console.warn);