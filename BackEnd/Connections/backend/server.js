import express from 'express';
const app = express();

app.get('/',(req ,res)=>{
    res.send("the server is running...")
})

app.get('/jokes',(req, res)=>{
    const jokes = [
    {
        id: 1,
        title: "Programming Joke",
        content: "Why do programmers prefer dark mode? Because light attracts bugs."
    },
    {
        id: 2,
        title: "JavaScript Joke",
        content: "Why was the JavaScript developer sad? Because he didn’t Node how to Express himself."
    },
    {
        id: 3,
        title: "Database Joke",
        content: "Why did the database admin leave his wife? She had too many relationships."
    },
    {
        id: 4,
        title: "CSS Joke",
        content: "Why did the CSS developer go to therapy? Because he had too many alignment issues."
    },
    {
        id: 5,
        title: "Computer Joke",
        content: "Why did the computer get cold? Because it forgot to close its Windows."
    },
    {
        id: 6,
        title: "React Joke",
        content: "Why did the React component break up with the Redux store? Too many state issues."
    },
    {
        id: 7,
        title: "Backend Joke",
        content: "Why don’t backend developers like nature? Too many bugs."
    },
    {
        id: 8,
        title: "Git Joke",
        content: "Why did the developer go broke? Because he used up all his cache."
    },
    {
        id: 9,
        title: "AI Joke",
        content: "Why did the AI go to school? To improve its neural network."
    },
    {
        id: 10,
        title: "Debugging Joke",
        content: "Debugging: Being the detective in a crime movie where you are also the murderer."
    }
    ];
    res.send(jokes)
})

const port = process.env.Port || 4000;

app.listen(port ,()=>{
    console.log(`http://localhost:${port}/jokes`)
})