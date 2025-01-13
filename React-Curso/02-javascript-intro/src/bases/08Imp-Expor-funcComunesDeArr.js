import { heroes } from "../data/heroes";

export const getHeroeById= (id)=>heroes.find((heroe)=>heroe.id===id) ;

console.log(getHeroeById(2));


// find? filter 
const getHeroeByOwner= (ower)=> heroes.filter((heroe) => heroe.owner===owner);
console.log(getHeroeByOwner('Marvel'));