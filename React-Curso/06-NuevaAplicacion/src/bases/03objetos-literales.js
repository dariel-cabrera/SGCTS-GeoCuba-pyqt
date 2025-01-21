// Los objetos literales usan property
const persona= {
   nombre:'Tony', // La llave nombre apunta a Tony 
   apellido:'Stark',
   edad:45,
};

console.log(persona.nombre);


console.log({persona})
// Tambien para visualizarlo mejor 
console.table(persona);

// Se pueden anidar objetos entre objetos 
const persona1= {
    nombre:'Tony',  
    apellido:'Stark',
    edad:45,
    direccion:{
        ciudad:'New York',
        zip:565236,
        lat:14.34,
        lng:34.92,
    },
 };

 // const persona2=persona esta asignacion no se debe hacer jamas se hace una copia de 
 // la refrencia
 
 // Para realizar un clon del objeto debo:
 const persona2={...persona1}