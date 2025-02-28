import { Module } from "@nestjs/common";
import { CalculoController } from "./calculo.controller";
import { CalculoService } from "./calculo.service";
import { MongooseModule } from '@nestjs/mongoose';
import { Calculation,CalculationSchema } from "./shema/datos.schema";



@Module({
  imports: [
    MongooseModule.forFeature([{ name: Calculation.name, schema:  CalculationSchema }])
  ],
   controllers:[CalculoController],
   providers:[CalculoService],
})

export class CalculoModule{}