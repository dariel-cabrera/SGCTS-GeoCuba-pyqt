import bcrypt from "bcrypt";
import mongoose from "mongoose";
import { userModel } from "../schemas/user.schema.js";
import { dbConnect } from "../mongo/index.js";

export async function seedDB() {
  await dbConnect(); // FIX: Esperar la conexión
   
  // Generacion del hash de la contraseña
  // Genera un "salt" (valor aleatorio) para cifrar la contraseña
  // bcrypt.hash("secret", salt): ifra la contraseña "secret" utilizando el salt generado.
  const salt = await bcrypt.genSalt(10);
  const hashPassword = await bcrypt.hash("secret", salt);

  // Verificar si el usuario ya existe
  const existingUser = await userModel.findOne({ email: "admin@jsonapi.com" });
  if (existingUser) {
    console.log("Admin user already exists.");
    return;
  }

  // Creacion del usuario Administrador 
  const user = {
    _id: mongoose.Types.ObjectId(),
    name: "Admin",
    email: "admin@jsonapi.com",
    password: hashPassword,
    created_at: new Date(),
    profile_image: "../../images/admin.jpg",
  };

  // Guardado del usuario en la base de Datos 
  try {
    const admin = new userModel(user);
    await admin.save();
    console.log("DB seeded with admin user");
  } catch (error) {
    console.error("Error inserting admin user:", error);
  }
}
// Ejecucion de la funcion y cierre de la conexion 
 /* seedDB().then(() => {
  mongoose.connection.close();
}); */
