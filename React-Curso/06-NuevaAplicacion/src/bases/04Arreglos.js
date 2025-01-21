// Arreglos en JS 

// const arreglo = new Array(100);
//arreglo.push(1)

const arreglo= [];
// arreglo.push(1) NO es recomendable usar el push 

// Tarea Realizar un clon del arreglo Agg 5 sin usar push
let arreglo2=[...arreglo,5];

// Map 
const arreglo3= arreglo2.map(function(numero){
     return numero*2; // Si no retornamos nada retorna undefine 
})
console.log(arreglo); 
console.log(arreglo2); 