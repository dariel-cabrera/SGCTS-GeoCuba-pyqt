import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config(); // Load environment variables
console.log('DB_LINK:', process.env.DB_LINK);

export const dbConnect = async () => {
  try {
    await mongoose.connect(process.env.DB_LINK, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    
    console.log('MongoDB connected successfully');
  } catch (error) {
    console.error('MongoDB connection error:', error.message);
    process.exit(1);
  }
};


