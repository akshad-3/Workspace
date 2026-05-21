import mongoose from "mongoose"

const doctorSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  salary: {
    type: String,
    required: true,
  },
  Qualfication: {
    type: String,
    required: true
  },
  exp: {
    type: Number,
    default: 0
  },
  worksInHospitals: [
  {
    type: mongoose.Schema.Types.      ObjectId,
    ref: "Hospital",
  }
  ],

},{timestamps: true})

exprt const Doctor= mongoose.model(
  "Doctor",doctorSchema
)