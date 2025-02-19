import mongoose from "mongoose";

const calculationSchema = new mongoose.Schema({
    densidad_a: { required: true, type: Number },
    densidad_m: { required: true, type: Number },
    indice: { required: true, type: Number },
    coeficiente:{ required: true, type: Number },
    altura: { required: true, type: Number },
    angulo:{ required: true, type: Number },
    aceleracion:{ required: true, type: Number },
    Q: { required: true, type: Number },
    P:{ required: true, type: Number },
    K: { required: true, type: Number },
});

calculationSchema.virtual("id").get(function () {
  return this._id.toHexString();
});

userSchema.set("toJSON", { virtuals: true });

export const userModel = mongoose.model("calculation", calculationSchema);
