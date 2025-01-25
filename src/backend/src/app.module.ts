import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CalculoModuleModule } from './calculo-module/calculo-module.module';
import { CalculoModule } from './calculo/calculo.module';
import { CalculoController } from './auth/calculo/calculo.controller';
import { CalculoController } from './–no-spec/calculo/calculo.controller';
import { CalculoController } from './–no-spec/calculo/calculo.controller';
import { CalculoController } from './–no-spec/calculo/calculo.controller';

@Module({
  imports: [CalculoModuleModule, CalculoModule],
  controllers: [AppController, CalculoController],
  providers: [AppService],
})
export class AppModule {}
