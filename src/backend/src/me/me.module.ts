import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { User, UserSchema } from '../user/shema/user.shema';
import { MeService } from './me.service';
import { MeController } from './me.controller';

@Module({
  imports: [MongooseModule.forFeature([{ name: User.name, schema: UserSchema }])],
  controllers: [MeController],
  providers: [MeService],
})
export class MeModule {}