// Desestrututracion o Asignacion Desestructurante

const persona={
    nombre:'Tony',
    edad:45,
    clave:'Iroman'
}

// La forma de imprimir los datos de este objeto puede ser
/* 
    console.log(persona.nombre);
    console.log(persona.edad);
    console.log(persona.clave);

    Para evitar tanto Codigo se realiza la Asignacion Desestructurante

*/

const{nombre,edad,clave}=persona;

console.log(nombre)

/*SI en caso nopmbre ya esta asigando podemos hacer
const{nombre=nombre2,edad,clave}=persona;
console.log(nombre2) // Aca no podemos llamar a nombre porque nombre esta siendo extraido
                      del obj y reasignado a nombre2
*/

/* LA DESTRUCTURACION EN FUNCIONES */
//Puedo Extraer sus propiedades usando {} en argumento de la funcion

const retornaPersona= ({nombre,edad})=>{
    console.log(nombre);
}

retornaPersona(persona);

//Se pueden asignar valores por defecto 

const retornaPersona1= ({nombre,edad,rango=1})=>{
    console.log(nombre,edad,rango);
}

retornaPersona1(persona);

// Tarea Extraer los datos de objeto dentro de la funcion

const useContext=({clave,nombre,edad,rango='Capitan'})=>{
    return {
        nombreClave:clave,
        anios:edad,
    }
}

const {nombreClave,anios} = useContext(persona);
console.log(nombreClave,anios);

// Para extraer los objetos dentro otro objeto 
/* const useContext2=({clave,nombre,edad,rango='Capitan'})=>{
    return {
        nombreClave:clave,
        anios:edad,
        longitud:{
            ln:12.356,
            lat:123.23
        }
    }
}

const {nombreClave,anios,longitud:{ln, lat }} = useContext2(persona);
console.log(nombreClave,anios, ln, lat ); */