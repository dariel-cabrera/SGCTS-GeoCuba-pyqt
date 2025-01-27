import { Body, Controller, Delete, Get, Post, Put } from '@nestjs/common';
import { CalculoService } from './calculo.service';
import { CreateCalculoDto } from './dto/create-Calculo.dto';

@Controller('calculo')
export class CalculoController {
      calculoService: CalculoService;
      constructor(calculoService: CalculoService){
        this.calculoService= calculoService;
      }

      @Get('/mostrarCalculos')
      getAllCalculos(){
        return this.calculoService.getCalculo();
      }

      @Post('/crearCalculos')
      createCalculos(@Body() calculo:CreateCalculoDto){
        return this.calculoService.createCalculo(calculo);
      }

      @Put('/actualizarCalculos')
      updateCalculos(){
        return this.calculoService.updateCalculo();
      }

      @Delete('/eliminarCalculos')
      deleteCalculos(){
        return this.calculoService.deleteCalculo();
      }

}
