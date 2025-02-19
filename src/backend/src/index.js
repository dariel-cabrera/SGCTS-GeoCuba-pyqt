import express from "express";
import bodyParser from "body-parser";
import cors from "cors";
import dotenv from "dotenv";
import "./passport.js";
import { dbConnect } from "./mongo/index.js";
import { meRoutes, authRoutes,calculationRoutes} from "./routes/index.js";
import path from "path";
import * as fs from "fs";
import cron from "node-cron";
import ReseedAction from "./mongo/ReseedAction.js";

dotenv.config();

const PORT = process.env.PORT || 8080;
const app = express();

if (!process.env.APP_URL_CLIENT) {
  console.error("Error: APP_URL_CLIENT no está definido en el .env");
  process.exit(1);
}

const whitelist = [ process.env.APP_URL_CLIENT,  process.env.APP_URL_API];
const corsOptions = {
  origin: function (origin, callback) {
    console.log("Solicitud desde:", origin);
    if (!origin || whitelist.includes(origin.replace(/\/$/, ""))) {
      callback(null, true);
    } else {
      console.log(`Bloqueado por CORS: ${origin}`);
      callback(new Error("Not allowed by CORS"));
    }
  },
  credentials: true,
};

dbConnect();

app.use(cors(corsOptions));
app.use(bodyParser.json({ type: "application/vnd.api+json", strict: false }));

app.get("/", function (req, res) {
  const __dirname = fs.realpathSync(".");
  res.sendFile(path.join(__dirname, "/src/landing/index.html"));
});

app.use("/auth", authRoutes);
app.use("/me", meRoutes);
app.use("/calculation",calculationRoutes);

if (process.env.SCHEDULE_HOUR) {
  cron.schedule(`0 */${process.env.SCHEDULE_HOUR} * * *`, () => {
    ReseedAction();
  });
}

app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));