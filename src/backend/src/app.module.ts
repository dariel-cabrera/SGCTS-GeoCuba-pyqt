import { Module } from '@nestjs/common';
import { AuthModule } from './auth/auth.module';
import { MeModule } from './me/me.module';
import { CalculationModule } from './calculation/calculation.module';
import { DatabaseModule } from './shared/database/database.module';

@Module({
  imports: [AuthModule, MeModule, CalculationModule, DatabaseModule],
})
export class AppModule {}