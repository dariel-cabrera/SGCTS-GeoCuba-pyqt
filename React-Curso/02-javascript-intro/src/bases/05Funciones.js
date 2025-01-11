//Funciones en JS

/*
function saludar(nombre){
    return `Hola,${nombre}`;
}

saludar=30; 

Existe esta forma pero de esta manera puede ser modificada la funcion 
y puede dar un warning
*/

const saludar= function(nombre){  // De esta forma no podra ser modificado
    return `Hola,${nombre}`;
}

// Funciones de Flecha 
const saludar2= (nombre)=> {  
    return `Hola,${nombre}`;
}

//Si solo tiene un return se puede hacer 
const saludar3= (nombre)=> `Hola,${nombre}`;

// Si no recibe argumentos 
const saludar4= ()=> `Hola,${nombre}`;

// Para retornar un obj de forma implicita sin usar return 
const objeto=()=>({
    id:'ABC1234',
    username:'El_papi'
});

// Tarea 
/* 
    1. Transformar a una funcion de Flecha
    2. Tiene que retornar un objeto implicito
    
    function getUsuarioActivo(nombre){
        return {
            uid:'ABC567',                                         
            username:nombre
        }
    };
*/

const getUsuarioActivo=(nombre)=>(
    {
        uid:'ABC567',
        username:nombre
    }
);