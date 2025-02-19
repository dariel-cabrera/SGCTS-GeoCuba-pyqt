import express from "express";
import {
  postCalculation
} from "../../services/calculation/index.js";

const router = express.Router();

router.post("/postCalculation", async (req, res, next) => {
  const {datos} = req.body.datos;
  console.log(req.body.datos);
  await postCalculation(req, res, datos);
});




export default router;
