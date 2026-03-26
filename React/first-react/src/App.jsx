import Main from "./component/main.jsx"
import Navbar from "./component/navbar.jsx"
import Jokes from "./practice/props-2/jokes.jsx"
import jokesdata from "./jokesdata.js"
import counter from "./practice/props-3/counting.jsx"
export default function App(){
  return(
    <>
      <Navbar />
      <Main />
      <AppForJokes />
      <counter />
    </>
  )
}
function AppForJokes(){
  const jokesofelements = jokesdata.map((joke)=>(<Jokes setup ={joke.setup} punchline ={joke.punchline}/>))
  return(
    <main>
      {jokesofelements}
    </main>
  )
}

// function AppForJokes(){
//   return(
//     <>
//       <Jokes 
//         setup="I got my daughter a fridge for her birthday."
//         punchline="I got my daughter a fridge for her birthday."
//         //upvotes={10}
//         isfun={true}
//         comments={[
//           {ID:"akhad" ,likes:23},
//           {ID:"akhada" ,likes:2}
//         ]}
//       />
//       <Jokes 
//         setup="How did the hacker escape the police?"
//         punchline="He just ransomware!"
//         isfun={true}
//         comments={[
//           {ID:"akhad" ,likes:23},
//           {ID:"akhada" ,likes:2}

//         ]}
//       />
//       <Jokes 
//         setup="Why don't pirates travel on mountain roads?"
//         punchline="Scurvy."
//         isfun={true}
//         comments={[
//           {ID:"akhad" ,likes:23},
//           {ID:"akhada", likes:2}
//         ]}
//       />
//       <Jokes 
//         setup="Why do bees stay in the hive in the winter?"
//         punchline="Swarm."
//         isfun={true}
//         comments={[
//           {ID:"akhad" ,likes:23},
//           {ID:"akhada" ,likes:2}
//         ]}
//       />
//     </>
//   )
// }
