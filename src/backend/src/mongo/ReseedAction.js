import mongoose from "mongoose";
import bcrypt from "bcrypt";
import { userModel } from "../schemas/user.schema.js";
import { dbConnect } from "./index.js";
import { seedDB } from "./seedData.js";


// ReseedAction:
/* Es una función que encapsula las operaciones de 
limpieza y siembra de la base de datos. */

const ReseedAction = () => {
  //Funcion Clear 
  /*await userModel.deleteMany({}):
    Elimina todos los documentos de la colección de usuarios. */
  async function clear() {
    dbConnect();
    await userModel.deleteMany({});
    console.log("DB cleared");
  }

  seedDB();
};

export default ReseedAction;
