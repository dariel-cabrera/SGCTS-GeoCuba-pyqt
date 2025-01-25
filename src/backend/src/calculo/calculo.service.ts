import { Injectable } from '@nestjs/common';
import { CreateCalculoDto } from './dto/create-Calculo.dto';

@Injectable()
export class CalculoService {
    getCalculo(){
        return "Retornando Calculos"
    }

    createCalculo(calculo:CreateCalculoDto){
        return "Creando Calculos"
    }

    updateCalculo(){
        return 'Actualizando Calculos'
   } 
    deleteCalculo(){
        return 'Eliminado Calculos'    
    }




}
