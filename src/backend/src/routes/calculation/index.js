import express from "express";
import {
  getCalculation,
  postCalculation,
  putCalculation,
  deleteCalculation
} from "../../services/calculation/index.js";

const router = express.Router();

// Ruta para obtener todos los cálculos
router.get("/getCalculation", async (req, res) => {
  await getCalculation(req, res);
});

// Ruta para crear un nuevo cálculo
router.post("/postCalculation", async (req, res) => {
  await postCalculation(req, res);
});

// Ruta para actualizar un cálculo existente
router.put("/putCalculation/:id", async (req, res) => {
  const { id } = req.params;
  await putCalculation(req, res, id);
});

// Ruta para eliminar un cálculo existente
router.delete("/deleteCalculation/:id", async (req, res) => {
  const { id } = req.params;
  await deleteCalculation(req, res, id);
});

export default router;
