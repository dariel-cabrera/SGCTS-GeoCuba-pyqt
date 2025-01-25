import { Module } from '@nestjs/common';
import { CalculoController } from './calculo.controller';
import { CalculoService } from './calculo.service';
import { CalculoController } from './calculo.controller';

@Module({
  controllers: [CalculoController],
  providers: [CalculoService]
})
export class CalculoModule {}
