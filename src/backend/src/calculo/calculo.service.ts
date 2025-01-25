import { Injectable } from '@nestjs/common';

@Injectable()
export class CalculoService {
    getCalculo(){
        return "Retornando Calculos"
    }

    createCalculo(calculo){
        return "Creando Calculos"
    }

    updateCalculo(){
        return 'Actualizando Calculos'
   } 
    deleteCalculo(){
        return 'Eliminado Calculos'    
    }




}
