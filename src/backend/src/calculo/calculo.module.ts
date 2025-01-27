import { Module } from '@nestjs/common';
import { CalculoController } from './calculo.controller';
import { CalculoService } from './calculo.service';


@Module({
  controllers: [CalculoController],
  providers: [CalculoService],
})
export class CalculoModule {}
