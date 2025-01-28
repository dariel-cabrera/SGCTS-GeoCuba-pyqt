import { Body, Controller, Delete, Get, Post, Put,Param } from '@nestjs/common';
import { CalculoService } from './calculo.service';
import { CreateCalculoDto } from './dto/create-Calculo.dto';
import { UpdateCalculoDto } from './dto/update-Calculo.dto';

@Controller('calculo')
export class CalculoController {
      calculoService: CalculoService;
      constructor(calculoService: CalculoService){
        this.calculoService= calculoService;
      }

      @Get('/mostrarCalculos')
      async getAllCalculos(){
        return this.calculoService.getCalculo();
      }

      @Post('/crearCalculos')
      async createCalculos(@Body() calculo: CreateCalculoDto){
        const {
          densidad_a,
          densidad_m,
          indice,
          coeficiente,
          altura,
          angulo,
          aceleracion,
          Q,
          P,
          K,
        } = calculo;
        return this.calculoService.createCalculo(
          densidad_a,
          densidad_m,
          indice,
          coeficiente,
          altura,
          angulo,
          aceleracion,
          Q,
          P,
          K,
        );
      }
      @Put('/actualizarCalculos/:id')
      async updateCalculos(@Param('id') id:string, @Body() calculo:UpdateCalculoDto){
        const {
          densidad_a,
          densidad_m,
          indice,
          coeficiente,
          altura,
          angulo,
          aceleracion,
          Q,
          P,
          K,
        } = calculo;
        return this.calculoService.updateCalculo(
          id,
          densidad_a,
          densidad_m,
          indice,
          coeficiente,
          altura,
          angulo,
          aceleracion,
          Q,
          P,
          K,
        );
      }

     

      @Delete('/eliminarCalculos/:id')
      async deleteCalculos(@Param('id') id: string){
        return this.calculoService.deleteCalculo(id);
      }
}

