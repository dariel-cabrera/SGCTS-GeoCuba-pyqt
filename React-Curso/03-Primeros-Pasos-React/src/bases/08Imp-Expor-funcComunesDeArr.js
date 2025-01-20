import { heroes } from "../data/heroes";

export const getHeroeById= (id)=>heroes.find((heroe)=>heroe.id===id) ;



// find? filter 
const getHeroeByOwner= (ower)=> heroes.filter((heroe) => heroe.owner===owner);
// console.log(getHeroeByOwner('Marvel'));