import reactlogo from "/Users/akshad/GitHub/Workspace/React/first-react/src/assets/react.svg"
export default function Navbar(){
    return(
        <header>
            <nav className="nav-bar">
                <img src={reactlogo} className="nav-bar-logo" alt="react-logo" />
                <span className="React-Facts">ReactFactss</span>
            </nav>
        </header>
    )
}