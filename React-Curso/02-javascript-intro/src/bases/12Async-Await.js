

/* const getImagenPromesa=()=>new Promise(resolve =>
    resolve('http//akknvkdfnig.com'))

getImagenPromesa().then(console.log)  */
/* const getImagen= async () => {    // Esto es una promesa 
    return 'http//akknvkdfnig.com'   
}

getImagen().then(console.log) */

// El await espera que termine la linea de coidgo antes de que pase a la sgte 
// linea de codigo y es obligatorio que este dentro de una func await. El codigo es sincrono 

const getImagen= async () => {    // Esto es una promesa 
    const apiKey= 'ESTO ES UN EJEMPLO';
    const resp = await fetch(`http//akknvkdfnig.com ${apiKey}`) // Espera que se ejecute la promesa
    const {data}= await resp.json();
    
    const {url}=data.images.original;
    const img = document.createElement('img');
    img.src=url;
    document.body.append(img);

    /*
       Para el  Manejo de Errores con: 
       try {
       

       }catch(error){
       
       
       }

    */
    
}

getImagen();


