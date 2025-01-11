import { heroes } from "../data/heroes";

const getHeroeById= (id)=>heroes.find((heroe)=>heroe.id===id) ;

console.log(getHeroeById(2));

const getHeroeByOwner= (ower)=> heroes.find({heroe} => heroe.id===owner);