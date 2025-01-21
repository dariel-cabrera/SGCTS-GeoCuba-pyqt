

/* const getImagenPromesa=()=>new Promise(resolve =>
    resolve('http//akknvkdfnig.com'))

getImagenPromesa().then(console.log)  */
/* const getImagen= async () => {    // Esto es una promesa 
    return 'http//akknvkdfnig.com'   
}

getImagen().then(console.log) */

// El await espera que termine la linea de coidgo antes de que pase a la sgte 
// linea de codigo y es obligatorio que este dentro de una func await. El codigo es sincrono 

export const getImagen= async () => {    // Esto es una promesa 
       // Para el  Manejo de Errores con: 
       try {
           const apiKey='Rfh3fDyGyAyv23iAULwLPxFyKxvFBpAZ';
            const resp = await fetch(`api.giphy.com/v1/gifs/random?api_key=${apiKey}`) // Espera que se ejecute la promesa
            const {data}= await resp.json();
            const {url}=data.images.original;
            return url 

       }catch(error){
           return 'No existe'
       
       }

    
    
}




