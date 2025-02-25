import { Module } from '@nestjs/common';
import { CalculoModule } from './calculo/calculo.module';
import { AuthModule } from './auth/auth.module';
import { DatabaseModule } from './shared/database/database.module';
import { MeModule } from './me/me.module';

@Module({
  imports: [AuthModule, MeModule, CalculoModule, DatabaseModule],
})
export class AppModule {}