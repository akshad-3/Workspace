import mongoose from "mongoose"

const medicalRecordSchema = new mongoose.Schema({},{timestamps: true})

exprt const medicalRecord= mongoose.model(
  "MedicalRecord",medicalRecordSchema
)