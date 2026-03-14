import {createRoot} from "react-dom/client"
import reactLogo from "/Users/akshad/GitHub/Workspace/React/second-react/src/react.svg"

const root = createRoot(document.getElementById('root'))
function Hearder(){
    return(
        <header>
            <img src={reactLogo} width="50px" alt="React logo" />
        </header>
    )
}
function Maincontent(){
    return(
        <main>
            <h1>Fun facts about React!</h1>
            <ul>
                <li>Was first release in 2013</li>
                <li>Was originally created by Jordan Walke</li>
                <li>Has well over 200K stars on GitHub</li>
                <li>Is maintained by Meta</li>
                <li>Powers thousands of enterprise apps, including mobile apps</li>
            </ul>
        </main>
    )
}
function Footer(){
    return(
        <footer>
            <small>this page is @reserver by this man here all the Rights</small>
        </footer>
    )
}
function Page() {
    return (
        <>
        <Hearder />
        <Maincontent />
        <Footer />
        </>
    )
}
root.render(
    <Page />
)

