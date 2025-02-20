import * as bcrypt from 'bcrypt';
import * as mongoose from 'mongoose';
import { User,UserDocument,UserSchema } from 'src/user/shema/user.shema';
import { config } from 'dotenv';

config(); // Cargar variables de entorno

export async function seedAdminUser() {
  try {
    // Conectar a MongoDB usando la URI de entorno
    const connection = await mongoose.connect(process.env.MONGO_URI as string, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    } as mongoose.ConnectOptions);

    console.log('✅ Conectado a la base de datos.');

    // Registrar el modelo de usuario en la conexión actual
    const UserModel = connection.model<UserDocument>('User', UserSchema);

    // Verificar si el usuario administrador ya existe
    const existingUser = await UserModel.findOne({ email: 'admin@jsonapi.com' });
    if (existingUser) {
      console.log('⚠️ El usuario administrador ya existe.');
      await mongoose.connection.close();
      return;
    }

    // Generar hash de la contraseña
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash('secret', salt);

    // Crear usuario administrador
    const user = new UserModel({
      _id: new mongoose.Types.ObjectId(),
      name: 'Admin',
      email: 'admin@jsonapi.com',
      password: hashedPassword,
      created_at: new Date(),
      profile_image: '../../images/admin.jpg',
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

// Ejecutar la función manualmente cuando se desee poblar la base de datos
if (require.main === module) {
  seedAdminUser();
}
