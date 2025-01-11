const nombre =  "Fernando";
const apellido= "Herrea";

let valorDado=5;
 valorDado=6;

// si hace falta cambiar el valor de una variable no hace falta poner let nuevamente
// Las variables de Scope
if (true){
    let valorDado= 7;
    console.log(valorDado);   
}
console.log(valorDado);
// Ya no se usa var
