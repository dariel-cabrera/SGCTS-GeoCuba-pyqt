import axios from 'axios';
import { calculando_K, calculo } from './ecuaciones';


export const fetchData = async (
    den_arena_,
    den_mar_,
    indice_,
    coeficiente_,
    altura_,
    angulo_,
    aceleracion_,
    P_,
    ) => {
    const Q= calculo(den_arena_,
        den_mar_,
        indice_,
        coeficiente_,
        altura_,
        angulo_,
        aceleracion_)

    const K= calculando_K( P_,Q);
   
    try {
        const response = await axios.post('http://localhost:3001/create',{
            densidad_a:den_arena_,
            densidad_m: den_mar_,
            indice: indice_,
            coeficiente:coeficiente_,
            altura:altura_,
            angulo:angulo_,
            aceleracion:aceleracion_,
            Q:Q,
            P:P_,
            K:K

        })
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

export const actualizar = async(
    id,
    den_arena_,
    den_mar_,
    indice_,
    coeficiente_,
    altura_,
    angulo_,
    aceleracion_,
    P_,)=>{
    const Q= calculo(den_arena_,
            den_mar_,
            indice_,
            coeficiente_,
            altura_,
            angulo_,
            aceleracion_)
    const K= calculando_K(P_,Q);
    try {
        const response = await axios.put('http://localhost:3001/update',{
            _id:id,
            densidad_a:den_arena_,
            densidad_m: den_mar_,
            indice: indice_,
            coeficiente:coeficiente_,
            altura:altura_,
            angulo:angulo_,
            aceleracion:aceleracion_,
            Q:Q,
            P:P_,
            K:K

        })
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
} 

export const eliminar =  (id) => {
    axios.delete(`http://localhost:3001/delete/${id}`)
   
}

export const crearUsuario= async(
    usuario,
    nombre,
    apellido,
    segundoApellido,
    ci,
    tipoTrabajador,
    sexo,
    correo,
    constrasena

) =>{
    console.log(usuario,
        nombre,
        apellido,
        segundoApellido,
        ci,
        tipoTrabajador,
        sexo,
        correo,
        constrasena)
    try {
        const response = await axios.post('http://localhost:3001/createUsuario',{
            usuario_:usuario,
            nombre_:nombre,
            apellido_:apellido,
            segundoApellido_:segundoApellido,
            ci_:ci,
            tipoTrabajador_:tipoTrabajador,
            sexo_:sexo,
            correo_:correo,
            constrasena_:constrasena,

        })
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }

}

export const actualizarUsuario = async(
    id,
    usuario,
    nombre,
    apellido,
    segundoApellido,
    ci,
    tipoTrabajador,
    sexo,
    correo,
    constrasena
)=>{
    
    try {
        const response = await axios.put('http://localhost:3001/updateUsuario',{
            _id:id,
            usuario_:usuario,
            nombre_:nombre,
            apellido_:apellido,
            segundoApellido_:segundoApellido,
            ci_:ci,
            tipoTrabajador_:tipoTrabajador,
            sexo_:sexo,
            correo_:correo,
            constrasena_:constrasena,

        })
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
} 

export const eliminarUsuario =  (id) => {
    axios.delete(`http://localhost:3001/deleteUsuario/${id}`)
   
}