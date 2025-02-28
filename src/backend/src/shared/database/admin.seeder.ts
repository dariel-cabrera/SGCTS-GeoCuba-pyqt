import { Injectable } from '@nestjs/common';
import { User, UserSchema } from 'src/user/shema/user.shema';
import * as bcrypt from 'bcrypt';
import * as mongoose from 'mongoose';
import { config } from 'dotenv';

config(); // Cargar variables de entorno

@Injectable()
export class SeedService {
  async seedAdminUser() {
    try {
      const connection = await mongoose.connect(process.env.MONGO_URI as string, {
        useNewUrlParser: true,
        useUnifiedTopology: true,
      } as mongoose.ConnectOptions);

      console.log('✅ Conectado a la base de datos.');

      const UserModel = connection.model<User>('User', UserSchema);

      const existingUser = await UserModel.findOne({ email: 'admin@jsonapi.com' });
      if (existingUser) {
        console.log('⚠️ El usuario administrador ya existe.');
        await mongoose.connection.close();
        return;
      }

      const salt = await bcrypt.genSalt(10);
      const hashedPassword = await bcrypt.hash('secret', salt);

      const user = new UserModel({
        _id: new mongoose.Types.ObjectId(),
        name: 'Admin',
        email: 'admin@jsonapi.com',
        password: hashedPassword,
        created_at: new Date(),
      });

      await user.save();
      console.log('✅ Usuario administrador creado con éxito.');
    } catch (error) {
      console.error('❌ Error insertando el usuario administrador:', error);
    } finally {
      await mongoose.connection.close();
      console.log('🔌 Conexión cerrada.');
    }
  }
}
