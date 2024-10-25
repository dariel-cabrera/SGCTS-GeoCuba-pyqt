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