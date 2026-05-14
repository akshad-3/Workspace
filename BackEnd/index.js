require('dotenv').config()
const express = require('express')

const app = express()
const port = 4000
app.get('/',(req,res)=>{
    res.send('Hello this is the Root /')
})

app.get('/express',(req,res)=>{
    res.send("Hello, this is the root /express")
})

app.get('/login' , (req,res)=>{
    res.send("<h1>This is the login page with H1</h1>")
})


app.listen(process.env.PORT ,()=>{
    console.log(`example app listining on port no - ${port}`)
})