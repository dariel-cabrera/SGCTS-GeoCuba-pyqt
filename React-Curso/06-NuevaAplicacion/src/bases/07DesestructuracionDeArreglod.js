// Desestructuracion de Arreglos

const personajes= ['Popi','Lala','Luis'];

const[p1]=personajes;
// console.log(p1) // imprime Popi

//Si quiero extraer a Lala y no a Popi separamos por comas
const[,p2]=personajes;
// console.log(p2) // imprime Lala

// Igual con el tercero las comas omiten la posicion del arreglo.

//Funcion que retorna un Arreglo 
export const retornaArreglo = () =>{
    return ['ABC', 123];
};

// const [letras,numeros]= retornaArreglo();

//Tarea 
const useState = (valor)=>{
    return [valor,()=>{console.log(`Hola Mundo`)}]
}

const [nombre,setNombre] = useState('pipa');
console.log(nombre);
setNombre();