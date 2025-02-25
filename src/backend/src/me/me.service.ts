import { Injectable } from '@nestjs/common';
import * as bcrypt from 'bcrypt';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { User, UserDocument } from '../user/shema/user.shema';  // ✅ Corrige el import del esquema
import { UpdateProfileDto } from './dto/me.dto';

@Injectable()
export class MeService {
  constructor(@InjectModel(User.name) private userModel: Model<UserDocument>) {}  // ✅ Usa `UserDocument` para asegurar los tipos de Mongoose

  async getProfile(user: UserDocument) {
    const userObj = user.toObject();  // ✅ Asegura que puedes acceder a los virtuals como `id`
    const stringId = userObj.id.toString();
    const decId = stringId.substring(4, 8);
    const intId = parseInt(decId, 16);

    return {
      data: {
        type: 'users',
        id: intId === 1 ? intId : userObj.id,
        attributes: {
          name: userObj.name,
          email: userObj.email,
          profile_image: userObj.profile_image || null,
          createdAt: userObj.createdAt,  // ✅ Accede correctamente a `createdAt`
          updatedAt: userObj.updatedAt,  // ✅ Accede correctamente a `updatedAt`
        },
        links: {
          self: `${process.env.APP_URL_API}/users/${userObj.id}`,
        },
      },
    };
  }

  async updateProfile(user: UserDocument, updateData: UpdateProfileDto) {
    const { name, email, newPassword, confirmPassword } = updateData;
    const foundUser = await this.userModel.findOne({ email: user.email }).exec();  // ✅ Asegura que sea un documento Mongoose

    if (!foundUser) {
      throw new Error('No user matches the credentials');
    }

    if (newPassword && (newPassword.length < 8 || newPassword !== confirmPassword)) {
      throw new Error('The password should have at least 8 characters and match the password confirmation.');
    }

    if (newPassword) {
      const salt = await bcrypt.genSalt(10);
      const hashPassword = await bcrypt.hash(newPassword, salt);
      foundUser.password = hashPassword;
    }

    if (name) foundUser.name = name;
    if (email) foundUser.email = email;

    await foundUser.save();

    return {
      data: {
        type: 'users',
        id: foundUser.id,
        attributes: {
          name: foundUser.name,
          email: foundUser.email,
          profile_image: foundUser.profile_image || null,
        },
      },
    };
  }
}
