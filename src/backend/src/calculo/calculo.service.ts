import { Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Datos } from './schemas/datos.schema';

@Injectable()
export class DatosService {
  constructor(
    @InjectModel(Datos.name) private readonly datosModel: Model<Datos>,
  ) {}

  // Crear un nuevo registro
  async createCalculo(
    densidad_a: number,
    densidad_m: number,
    indice: number,
    coeficiente: number,
    altura: number,
    angulo: number,
    aceleracion: number,
    Q: number,
    P: number,
    K: number,
  ): Promise<Datos> {
    const nuevoDato = new this.datosModel({
      densidad_a,
      densidad_m,
      indice,
      coeficiente,
      altura,
      angulo,
      aceleracion,
      Q,
      P,
      K,
    });
    return await nuevoDato.save();
  }

  // Actualizar un registro existente
  async updateCalculo(
    id: string,
    densidad_a: number,
    densidad_m: number,
    indice: number,
    coeficiente: number,
    altura: number,
    angulo: number,
    aceleracion: number,
    Q: number,
    P: number,
    K: number,
  ): Promise<Datos> {
    return await this.datosModel.findByIdAndUpdate(
      id,
      {
        $set: {
          densidad_a,
          densidad_m,
          indice,
          coeficiente,
          altura,
          angulo,
          aceleracion,
          Q,
          P,
          K,
        },
      },
      { new: true }, // Retornar el documento actualizado
    );
  }

  // Eliminar un registro
  async deleteCalculo(id: string): Promise<any> {
    return await this.datosModel.deleteOne({ _id: id });
  }

  // Obtener todos los registros
  async getCalculo(): Promise<Datos[]> {
    return await this.datosModel.find().exec();
  }
}
