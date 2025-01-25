import { Body, Controller, Delete, Get, Post, Put } from '@nestjs/common';
import { CalculoService } from './calculo.service';
import { CreateCalculoDto } from './dto/createCalculoDto';

@Controller('calculo')
export class CalculoController {
      calculoService: CalculoService;
      constructor(calculoService: CalculoService){
        this.calculoService= calculoService;
      }

      @Get('/calculos')
      getAllCalculos(){
        return this.calculoService.getCalculo();
      }

      @Post('/calculos')
      createCalculos(@Body() calculo:CreateCalculoDto){
        return this.calculoService.createCalculo(calculo);
      }

      @Put('/calculos')
      updateCalculos(){
        return this.calculoService.updateCalculo();
      }

      @Delete('/Calculos')
      deleteCalculos(){
        return this.calculoService.deleteCalculo();
      }

}
