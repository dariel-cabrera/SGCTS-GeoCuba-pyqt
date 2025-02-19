import dotenv from "dotenv";
dotenv.config(); // Cargar variables de entorno antes de usarlas

import passport from "passport";
import { Strategy as JwtStrategy, ExtractJwt } from "passport-jwt";
import { userModel } from "./schemas/user.schema.js";

console.log("JWT_SECRET:", process.env.JWT_SECRET);
// Verificar que JWT_SECRET está definido
if (!process.env.JWT_SECRET) {
  throw new Error("Falta la variable de entorno JWT_SECRET");
}

const opts = {
  jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
  secretOrKey: process.env.JWT_SECRET,
};

passport.use(
  new JwtStrategy(opts, async (jwtPayload, done) => {
    try {
      const user = await userModel.findOne({ _id: jwtPayload.id });
      if (!user) return done(null, false);
      return done(null, user);
    } catch (err) {
      return done(err, false);
    }
  })
);

export default passport;
