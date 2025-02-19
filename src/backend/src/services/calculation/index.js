import dotenv from "dotenv";
import { calculationModel } from "../../schemas/calculation.schema.js";

dotenv.config();

export const getCalculation = async (req, res) => {
  try {
    const resultado = await calculationModel.find();
    return res.status(200).json(resultado);
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
}

export const postCalculation = async (req, res) => {
  try {
    const newCalculation = new calculationModel({
      densidad_a: req.body.densidad_a,
      densidad_m: req.body.densidad_m,
      indice: req.body.indice,
      coeficiente: req.body.coeficiente,
      altura: req.body.altura,
      angulo: req.body.angulo,
      aceleracion: req.body.aceleracion,
      Q: req.body.Q,
      P: req.body.P,
      K: req.body.K
    });

    await newCalculation.save();
    return res.status(201).json(newCalculation);
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
}

export const putCalculation = async (req, res) => {
  try {
    const updatedCalculation = await calculationModel.updateOne(
      { _id: req.params.id },
      {
        $set: {
          densidad_a: req.body.densidad_a,
          densidad_m: req.body.densidad_m,
          indice: req.body.indice,
          coeficiente: req.body.coeficiente,
          altura: req.body.altura,
          angulo: req.body.angulo,
          aceleracion: req.body.aceleracion,
          Q: req.body.Q,
          P: req.body.P,
          K: req.body.K
        }
      }
    );

    return res.status(200).json(updatedCalculation);
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
}

export const deleteCalculation = async (req, res) => {
  try {
    const deletedCalculation = await calculationModel.deleteOne({ _id: req.params.id });
    return res.status(200).json(deletedCalculation);
  } catch (error) {
    return res.status(500).json({ message: error.message });
  }
}
