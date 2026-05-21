import mongoose from "mongoose"

const hospitalSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true
  },
  adressLine: {
    type: String,
    required: true
  },
  city: {
    type: String,
    required: true
  },
  pincode: {
    type: String,
    required: true
  },
  specialized: {
    type: String
  },
},{timestamps: true})

exprt const Hospital= mongoose.model(
  "Hospital",hospitalSchema
)