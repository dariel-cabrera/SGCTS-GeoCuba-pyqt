import { Module, Global } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { ReseedAction } from './reseed-action';



@Global()
@Module({
  imports: [
    MongooseModule.forRoot(process.env.MONGO_URI), 
  ],
  providers: [ReseedAction],
  exports: [MongooseModule],
})
export class DatabaseModule {}
