import { Module } from '@nestjs/common';
import { CalculoModule } from './calculo/calculo.module';
import { MongooseModule } from '@nestjs/mongoose';
import * as dotenv from 'dotenv';

dotenv.config();
@Module({
  imports: [CalculoModule,
   MongooseModule.forRoot(process.env.MONGO_URI)
  ],
  
})
export class AppModule {}
