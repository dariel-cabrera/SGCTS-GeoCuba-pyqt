import * as mathjs from 'mathjs';

export const calculo = async(den_arena_,den_mar_,indice_,coeficiente_,altura_,angulo_,aceleracion_)=>{
   
    const N = (den_mar_ * mathjs.sqrt(aceleracion_));
    const D=(16 * mathjs.sqrt(indice_))*(den_arena_-den_mar_)*(1-coeficiente_);

    if ( D==0 ){
        console.log("LA division por 0 no permitida")
    }else{
       const Q= ( N / D ) * mathjs.sqrt(mathjs.pow(altura_,5))*mathjs.sin(2*angulo_);
        console.log(Q);
    }
}

