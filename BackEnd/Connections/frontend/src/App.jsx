import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import axios from 'axios'
import { useEffect } from 'react'
import { response } from 'express'

function App() {
  const [jokes, setJokes] = useState([])
  function jokesDiv(){
    jokes.map((joke)=>{
        <div key={joke.id}>
          <h3>{joke.title}</h3>
          <p>{joke.content}</p>
        </div>
      })
  }
  useEffect(()=>{
    axios.get('http://localhost:4000/jokes')
    .then((response)=>{
      setJokes(response.data)
    })
    .catch((error)=>{
      console.log("ERROR")
    })
  })
  
  return (
    <>
     <h1>hellowwww..........</h1>
     <p>JOKES : {jokes.length}</p>
     {jokesDiv}
    </>
  )
}

export default App
