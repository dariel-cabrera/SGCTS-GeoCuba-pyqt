import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { User, UserDocument } from './shema/user.shema';
import { PasswordReset, PasswordResetDocument } from './shema/password-reset.schema';

@Injectable()
export class UserService {
  constructor(
    @InjectModel(User.name) private userModel: Model<UserDocument>,
    @InjectModel(PasswordReset.name) private passwordResetModel: Model<PasswordResetDocument>,
  ) {}

  /*** 🚀 FUNCIONES DE USUARIO 🚀 ***/

  // Obtener todos los usuarios
  async findAll(): Promise<User[]> {
    return this.userModel.find().exec();
  }

  // Obtener un usuario por ID
  async findOneById(id: string): Promise<User> {
    const user = await this.userModel.findById(id).exec();
    if (!user) throw new NotFoundException('User not found');
    return user;
  }

  // Crear un nuevo usuario
  async create(userData: Partial<User>): Promise<User> {
    const newUser = new this.userModel(userData);
    return newUser.save();
  }

  // Actualizar un usuario
  async update(id: string, updateData: Partial<User>): Promise<User> {
    const updatedUser = await this.userModel.findByIdAndUpdate(id, updateData, { new: true }).exec();
    if (!updatedUser) throw new NotFoundException('User not found');
    return updatedUser;
  }

  // Eliminar un usuario
  async delete(id: string): Promise<void> {
    const result = await this.userModel.findByIdAndDelete(id).exec();
    if (!result) throw new NotFoundException('User not found');
  }

  /*** 🔐 FUNCIONES DE RESETEO DE CONTRASEÑA 🔐 ***/

  // Crear un nuevo registro de restablecimiento de contraseña
  async createPasswordReset(email: string, token: string): Promise<PasswordReset> {
    const resetEntry = new this.passwordResetModel({ email, token });
    return resetEntry.save();
  }

  // Buscar un token de restablecimiento de contraseña
  async findPasswordResetByEmail(email: string): Promise<PasswordReset | null> {
    return this.passwordResetModel.findOne({ email }).exec();
  }

  // Eliminar un token de restablecimiento de contraseña después de su uso
  async deletePasswordReset(email: string): Promise<void> {
    await this.passwordResetModel.deleteOne({ email }).exec();
  }
}
