
import reactLogo from "/Users/akshad/GitHub/Workspace/React/second-react/src/react.svg"

export default function Hearder(){
    return(
        <header className="header">
            <img src={reactLogo} className="nav-logo" alt="React logo" />
            <nav>
                <ul className="nav-list">
                    <li className="nav-list-itm">pricing</li>
                    <li className="nav-list-itm">about</li>
                    <li className="nav-list-itm">contact</li>
                </ul>
            </nav>
        </header>
    )
}