import globe from "../assets/globe.png"
export default function header(){
    return(
        <>
        <header>
            <img src={globe} alt="globe" />
            <h1>My Travel Journal</h1>        
        </header>
        </>
    )
}