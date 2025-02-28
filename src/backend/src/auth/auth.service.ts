import { Injectable, HttpException, HttpStatus } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import * as bcrypt from 'bcrypt';
import { JwtService } from '@nestjs/jwt';
import { ConfigService } from '@nestjs/config';
import * as nodemailer from 'nodemailer';
import * as randomToken from 'random-token';

import { User } from 'src/user/shema/user.shema';
import { PasswordReset, PasswordResetDocument } from '../user/shema/password-reset.schema';

@Injectable()
export class AuthService {
  private transporter: nodemailer.Transporter;

  constructor(
    @InjectModel(User.name) private readonly userModel: Model<User>,
    @InjectModel(PasswordReset.name) private readonly passwordResetModel: Model<PasswordResetDocument>,
    private readonly jwtService: JwtService,
    private readonly configService: ConfigService
  ) {
    // Configuración del transportador de nodemailer
    this.transporter = nodemailer.createTransport({
      host: this.configService.get<string>('MAILTRAP_HOST'),
      port: this.configService.get<number>('MAILTRAP_PORT'),
      auth: {
        user: this.configService.get<string>('MAILTRAP_USER'),
        pass: this.configService.get<string>('MAILTRAP_PASSWORD'),
      },
    });
  }

  // 🔐 Login de usuario
  async login(email: string, password: string) {
    const user = await this.userModel.findOne({ email });

    if (!user) {
      throw new HttpException('Las credenciales no son válidas', HttpStatus.UNAUTHORIZED);
    }

    const validPassword = await bcrypt.compare(password, user.password);
    if (!validPassword) {
      throw new HttpException('Contraseña incorrecta', HttpStatus.UNAUTHORIZED);
    }

    // Generar token JWT
    const payload = { id: user.id, email: user.email };
    const token = this.jwtService.sign(payload);

    return {
      token_type: 'Bearer',
      expires_in: '24h',
      access_token: token,
      refresh_token: token,
    };
  }

  // 🔓 Registro de usuario
  async register(name: string, email: string, password: string) {
    const existingUser = await this.userModel.findOne({ email });
    if (existingUser) {
      throw new HttpException('El email ya está en uso', HttpStatus.BAD_REQUEST);
    }

    if (!password || password.length < 8) {
      throw new HttpException('La contraseña debe tener al menos 8 caracteres', HttpStatus.BAD_REQUEST);
    }

    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(password, salt);

    const newUser = new this.userModel({ name, email, password: hashPassword });
    await newUser.save();

    // Generar JWT token
    const payload = { id: newUser.id, email: newUser.email };
    const token = this.jwtService.sign(payload);

    return {
      token_type: 'Bearer',
      expires_in: '24h',
      access_token: token,
      refresh_token: token,
    };
  }

  // 🔁 Olvidó su contraseña
  async forgotPassword(email: string) {
    const user = await this.userModel.findOne({ email });
    if (!user) {
      throw new HttpException('El correo no existe', HttpStatus.BAD_REQUEST);
    }

    const token = randomToken(20);

    // Guardar token en DB
    await this.passwordResetModel.create({ email, token, created_at: new Date() });

    // Enviar correo de recuperación
    await this.transporter.sendMail({
      from: 'admin@jsonapi.com',
      to: email,
      subject: 'Recuperar contraseña',
      html: `<p>Para restablecer tu contraseña, haz clic en <a href='${this.configService.get('APP_URL_CLIENT')}/auth/reset-password?token=${token}&email=${email}'>este enlace</a></p>`,
    });

    return { message: 'Correo enviado para restablecer la contraseña' };
  }

  // 🔄 Restablecer contraseña
  async resetPassword(email: string, token: string, password: string, password_confirmation: string) {
    const resetRecord = await this.passwordResetModel.findOne({ email, token });

    if (!resetRecord) {
      throw new HttpException('El token es inválido o ha expirado', HttpStatus.BAD_REQUEST);
    }

    if (password.length < 8) {
      throw new HttpException('La contraseña debe tener al menos 8 caracteres', HttpStatus.BAD_REQUEST);
    }

    if (password !== password_confirmation) {
      throw new HttpException('Las contraseñas no coinciden', HttpStatus.BAD_REQUEST);
    }

    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    await this.userModel.updateOne({ email }, { $set: { password: hashedPassword } });

    // Eliminar token usado
    await this.passwordResetModel.deleteOne({ email });

    return { message: 'Contraseña restablecida correctamente' };
  }
}
